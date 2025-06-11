import os
import re
import time

import pyautogui
import pygetwindow as gw
import pyperclip
from clipboard_modifier import modify_copied_content
from config.configuration import cord_x, cord_y, keyboard_selector, path


# With this function we can read the output of luascript and determine what the keyboard ID is
# Then we close luascript, modify the clipboard with the new value and open luascripts and paste and run
def read_output():
    # Read the content of the file
    with open("luaoutput.txt", "r") as f:
        content = f.read()

    # Step 1: Find the block that starts with '0:' and ends before the next number-colon pattern
    block_match = re.search(r"0:\s+(.*?)(?:\n\d+:|$)", content, re.DOTALL)

    if block_match:
        block = block_match.group(1)

        # Step 2: Extract the SystemId within that block
        sysid_match = re.search(r"SystemId\s*=\s*(\S+)", block)

        if sysid_match:
            system_id = sysid_match.group(1)

            # Step 3: Extract the part between the 3rd and 4th '&'
            parts = system_id.split("&")
            if len(parts) >= 4:
                print(parts[3])
                return f"'{parts[3]}'"
            else:
                print("SystemId does not contain enough '&' symbols.")
        else:
            print("SystemId not found in the '0:' block.")
    else:
        print("Block starting with '0:' not found.")


def start_lua():
    with open(f"{path}/luascript.lua", "r") as f:
        pyperclip.copy(f.read())
    # modify_copied_content("local keyboardIdentifier", keyboard_selector)
    os.startfile(f"{path}/LuaMacros.exe")
    time.sleep(2)
    pyautogui.hotkey("ctrl", "v")
    pyautogui.click(cord_x, cord_y)
    time.sleep(2)
    if keyboard_selector != "'0000AAA'":
        os.system("taskkill /f /im luamacros.exe")
        modify_copied_content("local keyboardIdentifier", read_output())
        time.sleep(2)
        os.startfile(f"{path}/LuaMacros.exe")
        time.sleep(2)
        pyautogui.hotkey("ctrl", "v")
        pyautogui.click(cord_x, cord_y)
        gw.getActiveWindow().minimize()
