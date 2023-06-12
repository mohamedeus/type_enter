import sys
import time
import pyautogui
import countdown_module

# Check if the FILE_PATH argument is provided
if len(sys.argv) < 2:
    print("Usage: python type_enter.py FILE_PATH")
    print("INVALID arg")
    sys.exit(1)

FILE_PATH = sys.argv[1]

# Open the text file
with open(FILE_PATH, 'r') as file:

    # Wait for 5 seconds
    print("CLICK ON APPROPRIATE FIELD!")
    print("Will begin in 5 seconds")
    countdown_module.countdown(5)

    # Read each line
    for line in file:
        # Remove trailing newline character
        line = line.rstrip('\n')

        # Type the line
        pyautogui.typewrite(line)

        time.sleep(.7)

        # Press Enter
        pyautogui.press('enter')

    print("FINISH type_enter")
