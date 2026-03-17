import asyncio, time, copy, sys
from typing import Optional

# AP imports
import Utils
from CommonClient import get_base_parser, gui_enabled, server_loop

import dolphin_memory_engine as dme

from .client.context.base_context import BaseContext, BaseCommandProcessor, logger
from .Items import *
from .Locations import *
from .client.constants import *
from .Helpers import StringByteFunction as sbf, PCLocType
from .iso_helper.colo_rom import PCUSAPPatch

warned_locs = []
warned_items = []

def read_byte(console_addr: int):
    return int.from_bytes(dme.read_bytes(console_addr, 1))

def read_short(console_addr: int):
    return int.from_bytes(dme.read_bytes(console_addr, 2))

def read_word(console_addr: int) -> int:
    return int.from_bytes(dme.read_bytes(console_addr, 4))

def ptr_addr(console_addr: int, ptr_offset: int) -> int:
    return dme.follow_pointers(console_addr, [ptr_offset])

def write_short(console_addr: int, value: int):
    dme.write_bytes(console_addr, value.to_bytes(2))

def read_string(console_addr: int, strlen: int):
    return sbf.byte_string_strip_null_terminator(dme.read_bytes(console_addr, strlen))

async def write_bytes_and_validate(addr: int, value: bytes) -> None:
    dme.write_bytes(addr, value)

def bits(byte: int):
    return [byte >> i & 1 for i in range(8)]

class PCCommandProcessor(BaseCommandProcessor):
    def _cmd_dolphin(self):
        """Prints current Dolphin status to the client."""
        if isinstance(self.ctx, PCContext):
            logger.info(f"Dolphin Status: {self.ctx.dolphin_status}")

    def _cmd_debug(self):
        """Provide debug information fro Dolphin's RAM addresses while playing Pokemon Colosseum if requested"""
        if isinstance(self.ctx, PCContext):
            Utils.async_start(self.ctx.get_debug_info(), name="Get Pokemon Colosseum's debug info")

class PCContext(BaseContext):
    command_processor = PCCommandProcessor
    game = "Pokemon Colosseum"
    items_handling = 0b111

    def __init__(self, server_address, password):
        """
        Initialize the PC Context.
        
        :param server_address: Address of AP server.
        :param password: Password for server authentication.
        """
        super().__init__(server_address, password)

        # Dolphin related tasks (connection)
        self.instance_id = None
        self.dolphin_sync_task: Optional[asyncio.Task[None]] = None
        self.rom_loaded = False
        self.password_required = False
        self.dolphin_status = CONNECTION_INITIAL

        # Handle recieved items
        self.game_clear = False
        self.last_not_ingame = time.time()
        self.arg_seed = ""
        self.idx_check = 0

        # Slot options for unlocks
        self.goal = None
        self.tower_unlock = None
        self.purify_unlock = None
        self.trainer_win = False

    async def disconnect(self, allow_autoreconnect: bool = False):
        """
        Disconnect the client from the server and reset game state variables.
        
        :param allow_autoreconnect: Allow the client to auto-reconnect to the server. Defaults to `False`.
        """
        await super().disconnect(allow_autoreconnect)
        self.auth = None
        dme.un_hook()
        self.dolphin_status = CONNECTION_LOST
        self.rom_loaded = False

    def on_package(self, cmd: str, args: dict):
        """
        Package handler to handle packages from the server.
        
        :param cmd: The command recieved from the server.
        :param args: The command arguments.
        """
        super().on_package(cmd, args)
        match cmd:
            case "Connected": # On Connect
                super().on_connected(args)
                slot_data = args["slot_data"]
                # World version needs to match
                if not slot_data["Version"] == CLIENT_VERSION:
                    local_version = str(slot_data["Version"]) if (str(slot_data["Version"])) else "N/A"
                    raise Utils.VersionException("Error - Server was generated with a different Pokemon Colosseum " +
                        f"APWorld version.\nThe client version is {CLIENT_VERSION}.\nPlease verify you are using the " +
                        f"same APWorld as the generator, which is '{local_version}'")

                self.arg_seed = str(slot_data["Seed"])
                self.goal = slot_data["Goal"]
                self.tower_unlock = slot_data["RealgamTowerUnlock"]
                self.purify_unlock = slot_data["PurifyUnlockAmount"]

            case "Bounced":
                if not hasattr(self, "instance_id"):
                    self.instance_id = time.time()

            case "ConnectionRefused":
                self.dolphin_status = AP_REFUSED
                logger.error(self.dolphin_status)

            case "RoomInfo":
                self.password_required = bool(args['password'])

    async def server_auth(self, password_requested: bool = False):
        """
        Authenticate with the AP server. Called as part of the init RoomInfo call in CommonClient

        :param password_requested: Whether the server requires a password. Defaults to `False`.
        """
        if not self.rom_loaded:
            logger.info("ROM not loaded, waiting for dolphin to be connected before trying to connect.")
            return

        if password_requested and not self.password:
            logger.info('Enter the password required to join this game:')
            self.password = await self.console_input()
        await self.send_connect()

    async def get_debug_info(self):
        logger.error("Command not implemented - Currently gathering required debugging addresses")
        return

    def hex_to_dec(self, hex) -> int:
        return int(hex, 16)

    def in_playable_state(self, byte1: int = 0x0, byte2: int = 0x0, byte3: int = 0x0, byte4: int = 0x0) -> bool:
        # Read all four bytes individuallym if not swt from the function call
        if byte1 == 0x0:
            byte1 = read_byte(MAP_ID_ADDR)
            byte2 = read_byte(MAP_ID_ADDR + 1)
            byte3 = read_byte(MAP_ID_ADDR + 2)
            byte4 = read_byte(MAP_ID_ADDR + 3)
        # Check if we are in either splash screen, title screen or main menu, and return the opposite of the result (True if we are not, False if we are)
        return not (byte1 == 0x80 and byte2 == 0x7F and ((byte3 == 0x25 and (byte4 == 0x5c or byte4 == 0xA8)) or (byte3 == 0x1F and byte4 == 0xB8) or (byte3 == 0x36 and byte4 == 0xE0)))

    def get_map_id(self) -> int:
        """
        Reads the bytes of the current map address in memory then returns what map we are on as an int.
        This is also what is mapped to the location data's map_id

        Return values
        -------------
        -1 - Not important to us

        0 - Title Screen

        1 - Outskirt Stand

        2 - Phenac City

        3 - Mayor's House

        4 - Pregym
        """
        # Read all four bytes individually 
        byte1 = read_byte(MAP_ID_ADDR)
        byte2 = read_byte(MAP_ID_ADDR + 1)
        byte3 = read_byte(MAP_ID_ADDR + 2)
        byte4 = read_byte(MAP_ID_ADDR + 3)
        
        map: int = -1
        if not self.in_playable_state(byte1, byte2, byte3, byte4):
            map = MENU_ID
        elif byte1 == 0x80 and byte2 == 0x7E and byte3 == 0xFD and byte4 == 0xE0:
            map = OUTSKIRT_STAND_ID
        elif byte1 == 0x80 and byte2 == 0x7E and byte3 == 0xFE and byte4 == 0x78:
            map = PHENAC_CITY_ID
        elif byte1 == 0x80 and byte2 == 0x7F and byte3 == 0x10 and byte4 == 0x94:
            map = MAYOR_HOUSE_ID
        elif byte1 == 0x80 and byte2 == 0x7F and byte3 == 0x12 and byte4 == 0x5C:
            map = PREGYM_ID
        elif byte1 == 0x80 and byte2 == 0x7F and byte3 == 0x13 and byte4 == 0xD8:
            map = CONSTRUCTION_LOT_ID
        elif byte1 == 0x80 and byte2 == 0x7F and byte3 == 0xFE and byte4 == 0xC4:
            map = PYRITE_ID
        return map

    async def pc_check_locations(self):
        current_map: int = self.get_map_id()
        local_missing = copy.deepcopy(self.missing_locations)
        for loc in local_missing:
            local_loc = self.location_names.lookup_in_game(loc)
            pc_loc_data: PCLocData = all_locations[local_loc]
            if pc_loc_data is None:
                if loc not in warned_locs:
                    logger.warning(f"WARNING: Location {loc} does not have any location data to it! Please inform the Pokemon Colosseum AP devs.")
                    warned_locs.append(loc)
                continue
            # If the location's map is not the current map or location's type has not been set yet, do not check
            try:
                if pc_loc_data.type is PCLocType.NONE:
                    if loc not in warned_locs:
                        logger.warning(f"WARNING: The type of the location is set to NONE for location {loc}. Please inform the Pokemon Colosseum AP devs.")
                        warned_locs.append(loc)
                    continue
                if current_map not in pc_loc_data.map_id:
                    continue
            except:
                # Should never happen, but just in case
                raise Exception(f"ERROR: {loc} passed previous check but is not able to provice type or map_id. Please inform the Pokemon Colosseum AP devs.")


            if self.check_ram(pc_loc_data, pc_loc_data.ram_info.ram_addr, current_map):
                self.locations_checked.add(loc)

        await self.check_locations(self.locations_checked)
        # Special stuff to check if game has been cleared

    def check_ram(self, loc_data: PCLocData, addr: int, cur_map) -> bool:
        # Get intitial RAM data from address
        ram_data = 0x0
        if loc_data.ram_info.ptr:
            ram_data = read_byte(ptr_addr(addr, loc_data.ram_info.ptr_offset))
        else:
            ram_data = read_byte(addr)

        if loc_data.debug is not None:
            logger.info(f"{loc_data.debug.loc_name}|{hex(loc_data.debug.ptr_offset)}|{bits(ram_data)[loc_data.debug.bit]}")

        match loc_data.type:
            case PCLocType.START:
                if cur_map == OUTSKIRT_STAND_ID:
                    logger.info("Until either it is patched out or a new area in memory is found, item checks will only be given after the first save of the game.")
                    logger.info("The quickest save point is the Pokemon Center right after Shady Guy Folly.")
                    return True
            case PCLocType.TRAINER:
                if self.trainer_win:
                    bit = bits(ram_data)
                    if (bit[loc_data.ram_info.bit_pos]):
                        self.trainer_win = False
                        return True
                if not self.trainer_win and read_byte(IN_BATTLE) and read_byte(BATTLE_WIN_CHECK) == 0x02:
                        self.trainer_win = True # Enable a flag to keep checking after the fight is over to get the trainer check
            case PCLocType.SHADOW:
                if read_byte(IN_BATTLE):
                    bit = bits(ram_data)
                    if (bit[loc_data.ram_info.bit_pos]):
                        return True
            case PCLocType.CHEST | PCLocType.EVENT:
                bit = bits(ram_data)
                if (bit[loc_data.ram_info.bit_pos]):
                    return True
        return False

    async def give_pc_items(self):
        last_recv_idx = read_short(ptr_addr(PRIMARY_POINTER, AP_ITEM_INDEX_OFFSET))
        save_count = read_short(ptr_addr(PRIMARY_POINTER, SAVE_COUNT_OFFSET))
        if len(self.items_received) == last_recv_idx or save_count == 0:
            return

        recv_items = self.items_received[last_recv_idx:]
        for item in recv_items:
            last_recv_idx += 1
            self.idx_check = last_recv_idx
            pc_item_name = self.item_names.lookup_in_game(item.item)
            pc_item: ItemDesc = None

            for tmp_item in all_items:
                if pc_item_name == tmp_item["name"]:
                    pc_item = tmp_item
                    break

            if pc_item["data"] is None:
                if pc_item not in warned_items:
                    logger.error(f"Item {pc_item["name"]} does not have any data associated with it! Please inform the Pokemon Colosseum AP devs.")
                    warned_items.append(pc_item)
                continue

            if pc_item["data"].item_type == PCItemType.ITEM:
                success = await self.write_into_bag(ITEMS_BAG_START_OFFSET, 0x50, pc_item)
            
            if pc_item["data"].item_type == PCItemType.POKEBALL:
                success = await self.write_into_bag(BALLS_BAG_START_OFFSET, 0x40, pc_item)
            
            if pc_item["data"].item_type == PCItemType.BERRY:
                success = await self.write_into_bag(BERRIES_BAG_START_OFFSET, 0xA0, pc_item)
            
            if pc_item["data"].item_type == PCItemType.TM:
                success = await self.write_into_bag(TMS_BAG_START_OFFSET, 0x100, pc_item)

            elif pc_item["data"].item_type == PCItemType.KEYITEM:
                success = await self.write_item_into_list(pc_item, KEY_ITEMS_BAG_START_OFFSET, 0xAC)
                
                if not success:                    
                    logger.error(f"Item {pc_item["name"]} could not be added to Key Items because its full! Please inform the Pokemon Colosseum AP devs.")

            elif pc_item["data"].item_type == PCItemType.POKEMON:
                # Handle adding a pokemon to the PC
                use_addr = 0x0
                amount_to_increase = 0x0
                while use_addr == 0x0:
                    offset = B1_S1_OFFSET + amount_to_increase
                    pc_poke_id = read_short(ptr_addr(PRIMARY_POINTER, offset))
                    if pc_poke_id == 0:
                        use_addr = ptr_addr(PRIMARY_POINTER, offset)
                        break
                    amount_to_increase += SLOT_OFFSET
                await write_bytes_and_validate(use_addr, int.to_bytes(pc_item["data"].item_id, 2))
                await write_bytes_and_validate(use_addr + UNKNOWN_REQUIRED, int.to_bytes(0x0B030202, 4))
        
        await write_bytes_and_validate(ptr_addr(PRIMARY_POINTER, AP_ITEM_INDEX_OFFSET), int.to_bytes(last_recv_idx, 2))
        await write_bytes_and_validate(ptr_addr(PRIMARY_POINTER, SAVE_COUNT_OFFSET), int.to_bytes(1, 1))

    async def write_into_bag(self, bag_offset, max_items, pc_item: ItemDesc) -> bool:
        success = await self.write_item_into_list(pc_item, bag_offset, max_items)

        if not success:
            logger.info(f"Item {pc_item["name"]} could not be placed in list. No more space available. Placing in PC storage instead.")
            success = await self.write_into_pc_storage(pc_item)

        return success    

    async def write_into_pc_storage(self, pc_item: ItemDesc) -> bool:
        return await self.write_item_into_list(pc_item, 0x7974, 0x200) #TODO How Much space in the storage?
    
    async def write_item_into_list(self, pc_item: ItemDesc, start_offset, max_list_space) -> bool:        
        use_addr = 0x0
        use_addr_amount = 0x0
        amount_to_increase = 0x0
        while use_addr == 0x0:
            if amount_to_increase >= max_list_space:
                return False            

            ptr_offset = start_offset + amount_to_increase
            pc_item_id = read_short(ptr_addr(PRIMARY_POINTER, ptr_offset))
            if pc_item_id == pc_item["data"].item_id or pc_item_id == 0:
                use_addr = ptr_addr(PRIMARY_POINTER, ptr_offset)
                use_addr_amount = ptr_addr(PRIMARY_POINTER, ptr_offset + 0x2)
                break
            amount_to_increase += 0x4
        cur_item_amount = read_short(use_addr_amount) + pc_item["data"].amount
        await write_bytes_and_validate(use_addr, int.to_bytes(pc_item["data"].item_id, 2))
        await write_bytes_and_validate(use_addr_amount, int.to_bytes(cur_item_amount, 2))

        return True
 
    async def dolphin_sync_main_task(self):
        logger.info(f"Using Pokemon Colosseum client {CLIENT_VERSION}")
        logger.info("Starting Dolphin connector. Use /dolphin for status information.")

        try:
            while not self.exit_event.is_set():
                try:
                    # If DME is not hooked/connected already
                    if not dme.is_hooked():
                        dme.hook()
                        if dme.get_status() == dme.get_status().noEmu or dme.get_status() == dme.get_status().notRunning:
                            dme.un_hook()
                            self.dolphin_status = CONNECTION_INITIAL
                            logger.info(self.dolphin_status)
                            await self.wait_for_next_loop(WAIT_TIMER_LONG)
                            continue

                    if not self.dolphin_status == CONNECTION_CONNECTED:
                        # If game ID is the same as standard, it is not randomized
                        game_id = read_string(0x80000000, 6)
                        if game_id == "GC6E01":
                            self.dolphin_status = CONNECTION_REFUSED
                            logger.info(self.dolphin_status)
                            dme.un_hook()
                            await self.wait_for_next_loop(WAIT_TIMER_LONG)
                            continue

                        # If not connected to the server, check for player name in RAM address (not done, getting slot name from console input)
                        if not self.auth:
                            # self.auth = read_string(SLOT_NAME_ADDR, SLOT_NAME_STR_LENGTH)
                            logger.info('Enter slot name:')
                            self.auth = await self.console_input()

                            # No player name found, disconnect DME and inform player
                            if not self.auth:
                                self.auth = None
                                self.dolphin_status = NO_SLOT_NAME
                                logger.info(self.dolphin_status)
                                dme.un_hook()
                                await self.wait_for_next_loop(WAIT_TIMER_LONG)
                                continue

                            # Reset locations_checked while we wait
                            self.locations_checked = set()

                            # Inform player we are ready and waiting to connect
                            if not self.rom_loaded:
                                self.dolphin_status = CONNECTION_VERIFY
                                logger.info(self.dolphin_status)
                                self.rom_loaded = True
                                await self.server_auth(self.password_required)

                        if not self.slot:
                            await self.wait_for_next_loop(WAIT_TIMER_LONG)
                            continue

                        arg_seed = read_string(0x80000001, 3)
                        if not self.arg_seed.startswith(arg_seed):
                            raise Exception(
                                "Incorrected Randomized Pokemon Colosseum ISO file selected. The seed does not match." +
                                "Please verify that you are using the right ISO/seed/APPC file.")

                        self.dolphin_status = CONNECTION_CONNECTED
                        logger.info(self.dolphin_status)

                    # At this point, we are connected. Update UI elements in the PCClient tab (when one is made)

                    # Lastly check any locations
                    if self.get_map_id() != MENU_ID:
                        await self.pc_check_locations()
                        await self.give_pc_items()
                    await self.wait_for_next_loop(WAIT_TIMER_SHORT)
                except Exception as ex:
                    dme.un_hook()
                    logger.error(str(ex))
                    logger.info("Connection to Dolphin failed, attempting again in 5 seconds...")
                    self.dolphin_status = CONNECTION_LOST
                    await self.disconnect()
                    await self.wait_for_next_loop(WAIT_TIMER_LONG)
                    continue
        except Exception as threadEx:
            logger.error("Something went horribly wrong with the Pokemon Colosseum client. Details: " + str(threadEx))

def main(*launch_args: str):
    # Import dolphin<->Colosseum class
    import colorama

    server_addr: str = ""
    rom_path: str = ""

    Utils.init_logging(CLIENT_NAME)
    logger.info(f"Starting PC Client {CLIENT_VERSION}")
    #dolphin_launcher: DolphinLauncher = DolphinLauncher()

    parser = get_base_parser()
    parser.add_argument('apcolo_file', default="", type=str, nargs="?", help='Path of an APCOLO file')
    args = parser.parse_args(launch_args)

    if args.apcolo_file:
        pc_usa_patch = PCUSAPPatch()
        try:
            pc_usa_manifest = pc_usa_patch.read_contents(args.apcolo_file)
            server_addr = pc_usa_manifest["server"]
            rom_path = pc_usa_patch.patch(args.apcolo_file)
        except Exception as ex:
            logger.error("Unable to patch the Pokemon Colosseum ROM as expected. Additional details:\n" + str(ex))
            Utils.messagebox("Cannot Patch Pokemon Colosseum", "Unable to patch your Pokemon Colosseum ROM as " +
                "expected. Additional details:\n" + str(ex), True)
            raise ex

    async def _main(connect, password):
        ctx = PCContext(server_addr if server_addr else connect, password)
        ctx.server_task = asyncio.create_task(server_loop(ctx), name="ServerLoop")

        ctx._main()

        if gui_enabled:
            ctx.run_gui()
        ctx.run_cli()
        await ctx.wait_for_next_loop(WAIT_TIMER_LONG)

        ctx.dolphin_sync_task = asyncio.create_task(ctx.dolphin_sync_main_task(), name="DolphinSync")

        await ctx.exit_event.wait()
        await ctx.shutdown()

        if ctx.dolphin_sync_task:
            await ctx.dolphin_sync_task

    # Open dolphin and run the program

    colorama.just_fix_windows_console()
    asyncio.run(_main(args.connect, args.password))
    colorama.deinit()

if __name__ == "__main__":
    Utils.init_logging(CLIENT_NAME, exception_logger="Client")
    main(*sys.argv[1:])
