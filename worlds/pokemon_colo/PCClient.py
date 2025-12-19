import asyncio, time, copy, sys
from typing import Any

# AP imports
import NetUtils, Utils
from CommonClient import get_base_parser, gui_enabled, server_loop

import dolphin_memory_engine as dme

from .client.context.base_context import BaseContext, BaseCommandProcessor, logger
from .Items import *
from .Locations import *
from .client.constants import *
from .Helpers import StringByteFunction as sbf
from .iso_helper.colo_rom import PCUSAPPatch

def read_byte(console_addr: int):
    return int.from_bytes(dme.read_bytes(console_addr, 1))

def read_short(console_addr: int):
    return int.from_bytes(dme.read_bytes(console_addr, 2))

def write_short(console_addr: int, value: int):
    dme.write_bytes(console_addr, value.to_bytes(2))

def read_string(console_addr: int, strlen: int):
    return sbf.byte_string_strip_null_terminator(dme.read_bytes(console_addr, strlen))

async def write_bytes_and_validate(addr: int, ram_offset: list[str] | None, curr_value: bytes) -> None:
    if not ram_offset:
        dme.write_bytes(addr, curr_value)
    else:
        dme.write_bytes(dme.follow_pointers(addr, ram_offset), curr_value)

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

        # Slot options for unlocks
        self.goal = None
        self.tower_unlock = None
        self.purify_unlock = None

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
                self.goal = slot_data["Options"]["Goal"]
                self.tower_unlock = slot_data["Options"]["RealgamTowerUnlock"]
                self.purify_unlock = slot_data["Options"]["PurifyUnlockAmount"]

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

    def check_trainer_fought(self) -> bool:
        """
        Checks for if a trainers was just recently fought and won against, and what trainer it was
        """
        # IN_BATTLE will only result in 0 (false) or 1 (true)
        if read_byte(IN_BATTLE) and read_byte(BATTLE_WIN_CHECK) == 0x02:
            pass
        logger.error("check_trainer_fought has not been implemented yet")
        return False

    async def pc_check_locations(self):
        pass

    async def give_pc_items(self):
        pass

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
                        # If address 800000009 is not set, random ISO not loaded
                        game_id = read_string(0x80000009, 1)
                        if not game_id:
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

                        arg_seed = read_string(0x80000001, len(str(self.arg_seed)))
                        if arg_seed != self.arg_seed:
                            raise Exception(
                                "Incorrected Randomized Pokemon Colosseum ISO file selected. The seed does not match." +
                                "Please verify that you are using the right ISO/seed/APPC file.")

                        self.dolphin_status = CONNECTION_CONNECTED
                        logger.info(self.dolphin_status)

                    # At this point, we are connected. Update UI elements in the PCClient tab (when one is made)

                    # Lastly check any locations
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
