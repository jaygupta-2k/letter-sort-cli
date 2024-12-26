from colorama import Back

# Constants for the game
MAX_STACK_SIZE = 4
QUIT_COMMAND = "Q"
RESET_COMMAND = "R"
HINT_COMMAND = "H"
NEW_COMMAND = "N"
INFO_COMMAND = "I"

# Constants for stack generation
MIN_STACKS = 5
MAX_STACKS = 9
COLORS = [Back.RED+"   "+Back.RESET,Back.GREEN+"   "+Back.RESET,Back.YELLOW+"   "+Back.RESET,Back.BLUE+"   "+Back.RESET,Back.MAGENTA+"   "+Back.RESET,Back.CYAN+"   "+Back.RESET]

# ANSI escape codes for alternate screen
ALT_SCREEN_ON = "\033[?1049h"
ALT_SCREEN_OFF = "\033[?1049l"