""" Commonly used constants for Pokemon Colosseum """

CLIENT_VERSION = "V0.1.0"
CLIENT_NAME = "Pokemon Colosseum Client"

AP_LOGGER_NAME = "Client"
AP_WORLD_VERSION_NAME = "APWorldVersion"

# Memory constants
IN_BATTLE = 0x8040836F
BATTLE_WIN_CHECK = 0x8046D767
STORY_FLAG_POINTER = 0x8047ADB9
MAP_ID_POINTER = 0x80538DE0

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
