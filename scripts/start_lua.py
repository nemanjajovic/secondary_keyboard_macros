import os
import re
import time

import pyautogui
import pygetwindow as gw
import pyperclip
from clipboard_modifier import modify_copied_content
from config.configuration import cord_x, cord_y, keyboard_selector, path


# Reads and parses the Lua script output to extract the keyboard ID from the block labeled '0:'
def read_output():
    # Open and read the contents of the output file
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


# Automates the LuaMacros workflow: sets up the script, injects the correct keyboard ID, and runs LuaMacros
def start_lua():
    # Read the contents of the Lua script and copy to clipboard
    with open(f"{path}/luascript.lua", "r") as f:
        pyperclip.copy(f.read())

    # Modify the clipboard content by inserting the initial keyboard selector value
    modify_copied_content("local keyboardIdentifier", keyboard_selector)

    # Launch LuaMacros application
    os.startfile(f"{path}/LuaMacros.exe")
    time.sleep(2)

    # Paste the script and click on specified coordinates to run
    pyautogui.hotkey("ctrl", "v")
    pyautogui.click(cord_x, cord_y)
    time.sleep(2)

    # If a different keyboard ID is detected, restart LuaMacros with the new ID
    if keyboard_selector != "'0000AAA'":
        os.system("taskkill /f /im luamacros.exe")  # Force close LuaMacros
        modify_copied_content(
            "local keyboardIdentifier", read_output()
        )  # Update clipboard with new keyboard ID
        time.sleep(2)

        # Relaunch LuaMacros with updated script
        os.startfile(f"{path}/LuaMacros.exe")
        time.sleep(2)
        pyautogui.hotkey("ctrl", "v")
        pyautogui.click(cord_x, cord_y)

        # Minimize the LuaMacros window to keep things clean
        gw.getActiveWindow().minimize()
