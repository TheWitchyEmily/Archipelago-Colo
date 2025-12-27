""" Commonly used constants for Pokemon Colosseum """

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

# Map constants for get_map_id
OUTSKIRT_STAND_ID = 0
PHENAC_CITY_ID = 1
MAYOR_HOUSE_ID = 2
PREGYM_ID = 3

# Primary pointer addresses
PRIMARY_POINTER = 0x8047ADB8
PARTY_1_ID_OFFSET = 0xA0
ITEM_START_OFFSET = 0x7976

#General addresses
MAP_ID_ADDR = 0x80538DE0
IN_BATTLE = 0x8040836F
BATTLE_WIN_CHECK = 0x8046D767
OPPONENT_ID = 0x80473CA1

# Special location codes
NO_DISABLE = 0x5 # For trainer location type, do not disable the scanning loop as another check relies on the same information