""" Commonly used constants for Pokemon Colosseum """

from worlds.pokemon_colo.Helpers import Natures, NatureInfo, StatName


CLIENT_VERSION = "V0.1.0"
CLIENT_NAME = "Pokemon Colosseum Client"

AP_LOGGER_NAME = "Client"
AP_WORLD_VERSION_NAME = "APWorldVersion"

# Dolphin connection messages
CONNECTION_REFUSED = "Detected a non-randomized ROM of Colosseum. Please close and load a different one. Retrying in 5 seconds..."
CONNECTION_LOST = "Connection to Dolphin was lost. Please restart the emulator and load Colosseum."
NO_SLOT_NAME = "No slot name was detected. Ensure a randomized ROM is loaded. Retrying in 5 seconds..."
CONNECTION_VERIFY = "Dolphin has been detected with the correct ROM, connect to server when ready..."
CONNECTION_INITIAL = "Dolphin was not detected to be running. Retrying in 5 seconds..."
CONNECTION_CONNECTED = "Dolphin and AP connected, ready to play!"
AP_REFUSED = "AP refused to connect for one or more reasons, see above for details."

# Loop wait timers
WAIT_TIMER_LONG: float = 5
WAIT_TIMER_SHORT: float = 0.125

# Nature help
ALL_NATURES: dict = {
    Natures.HARDY: NatureInfo(StatName.ATTACK, StatName.ATTACK),
    Natures.LONELY: NatureInfo(StatName.ATTACK, StatName.DEFENSE),
    Natures.ADAMANT: NatureInfo(StatName.ATTACK, StatName.SP_ATTACK),
    Natures.NAUGHTY: NatureInfo(StatName.ATTACK, StatName.SP_DEFENSE),
    Natures.BRAVE: NatureInfo(StatName.ATTACK, StatName.SPEED),
    Natures.BOLD: NatureInfo(StatName.DEFENSE, StatName.ATTACK)
}

# Map constants for get_map_id
MENU_ID = 0
OUTSKIRT_STAND_ID = 1
PHENAC_CITY_ID = 2
MAYOR_HOUSE_ID = 3
PREGYM_ID = 4
CONSTRUCTION_LOT_ID = 5
PYRITE_ID = 6
PYRITE_POLICE_DEPARTMENT_ID = 7
PYRITE_FORTUNE_TELLING_ID = 8
PYRITE_DUKINGS_HOUSE_ID = 9
PYRITE_DUKE_HIDEOUT_ID = 10
PYRITE_GRAND_HOTEL_ID = 11
PYRITE_WINDMILL_ID = 12

# Primary pointer addresses
PRIMARY_POINTER = 0x8047ADB8
AP_ITEM_INDEX_OFFSET = 0xB87
ITEM_START_OFFSET = 0x7974
B1_S1_OFFSET = 0xB9C
SLOT_OFFSET = 0x138 # Only used to add to B1_S1 to check where the next empty slot is for a new shadow pokemon

#Party Offsets
PARTY_1_ID_OFFSET = 0xA1
PARTY_2_ID_OFFSET = 0x1D9
PARTY_3_ID_OFFSET = 0x311
PARTY_4_ID_OFFSET = 0x449
PARTY_5_ID_OFFSET = 0x581
PARTY_6_ID_OFFSET = 0x6B9

# Pokemon stat offset (starting from the first byte of the Pokemon's data)
NATURE_OFFSET = 0x4
MET_LEVEL = 0xE
CAUGHT_POKEBALL = 0xF
OT_NAME_OFFSET = 0x18 # (20-Bytes)
NICKNAME_OFFSET = 0x2F
LEVEL_OFFSET = 0x60
HELD_ITEM_OFFSET = 0x89
SHADOW_RIBBON_OFFSET = 0xC5
SHADOW_ID_OFFSET = 0xD8
SHADOW_CHECK_ONE_OFFSET = 0xDB
SHADOW_CHECK_TWO_OFFSET = 0xDC
# 2 Bytes below this
TRAINER_ID_OFFSET = 0x16
HP_IV_OFFSET = 0xA3
ATTACK_IV_OFFSET = 0xA5
DEFENSE_IV_OFFSET = 0xA7
SP_ATTACK_IV_OFFSET = 0xA9
SP_DEFENSE_IV_OFFSET = 0xB1
SPEED_IV_OFFSET = 0xB3
MET_LOCATION_OFFSET = 0xC
CURRENT_HP_OFFSET = 0x8A
MAX_HP_OFFSET = 0x8C
ATTACK_OFFSET = 0x8E
DEFENSE_OFFSET = 0x90
SP_ATTACK_OFFSET = 0x92
SP_DEFENSE_OFFSET = 0x94
SPEED_OFFSET = 0x96
SHADOW_METER_OFFSET = 0xDD
# 4 Bytes below this
UNKNOWN_REQUIRED = 0x8 # (required to be 0B 03 02 02?)
CURRENT_EXP = 0x5C
MOVE_1_OFFSET = 0x78

# Bag Offsets to add, remove, or manipulate items in the inventory. Items are 4 Bytes, 2 for Id and 2 for quantity
ITEMS_BAG_START_OFFSET = 0x7F0 #Max 20 Item Limit
KEY_ITEMS_BAG_START_OFFSET = 0x840 #Max 43 Items
BALLS_BAG_START_OFFSET = 0x8EC # Max 16 Items
TMS_BAG_START_OFFSET = 0x92C # Max 64 Items
BERRIES_BAG_START_OFFSET = 0xA2C # Max 40 Items

#General addresses
MAP_ID_ADDR = 0x80538DE0
IN_BATTLE = 0x8040836F
BATTLE_WIN_CHECK = 0x8046D767
OPPONENT_ID = 0x80473CA1

#Misc
RUI_NAME = 0x80409632 # Max 7 characters, 2 Byte per character. https://bulbapedia.bulbagarden.net/wiki/GameCube_character_encoding_(Generation_III)#Pok%C3%A9mon_Colosseum_and_XD

# Special location codes
NO_DISABLE = 0x5 # For trainer location type, do not disable the scanning loop as another check relies on the same information