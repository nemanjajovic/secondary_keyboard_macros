import os
import time
from threading import Thread

import keyboard
import pyautogui
import pygetwindow
import pyperclip
import pystray
from clipboard_modifier import modify_copied_content
from PIL import Image

# Change this depending if im using this at home or at work
# Home: "C://Users/User/Desktop/luamacros"
# Work: ""
path = "C://Users/User/Desktop/luamacros"

# Also change this
# Home: "'14C79465'"
# Work: "'2FE3714A'"
keyboard_selector = "'14C79465'"


def start_lua():
    with open(f"{path}/luascript.lua", "r") as file:
        pyperclip.copy(file.read())
    # Change KeyboardSelection to either home_keyboard or work_keyboard
    modify_copied_content("local keyboardIdentifier", keyboard_selector)
    os.startfile(f"{path}/LuaMacros.exe")
    time.sleep(2)
    pyautogui.hotkey("ctrl", "v")
    pyautogui.click(473, 169)
    pygetwindow.getActiveWindow().minimize()


def close_program():
    open(
        f"{path}/keypressed.txt", "w"
    ).close()  # clear the contents of keypressed.txt file before terminating the script
    os.system("taskkill /f /im luamacros.exe")
    print("Closing the Python script...")
    time.sleep(1)
    print("SUCCESS: Python process has been terminated")
    os._exit(0)


start_lua()


def read_file():
    try:
        with open(f"{path}/keypressed.txt", "r") as file:
            content = file.read().strip()
            if content == "k":
                close_program()  # I will not keep this as a macro since I have a tray icon to kill this program, leaving for testing purposes for now
            elif content == "b":
                os.startfile(
                    "C://ProgramData/Microsoft/Windows/Start Menu/Programs/Brave.lnk"
                )
            else:
                print(f"Keyboard 2: {content}")
    except FileNotFoundError:
        print("File not found.")


def on_press(event):
    if event.name == "f24" and event.event_type == "down":  # Ensure it's an F24 press
        read_file()


keyboard.on_press(on_press)

print("Listening for macro key press...")


def create_icon():
    icon_image = Image.open(f"{path}/res/icon.png")
    menu = (pystray.MenuItem("Exit", close_program),)
    icon = pystray.Icon("LuaMacros", icon_image, "LuaMacros Manager", menu)
    icon.run()


# Start tray icon in a separate thread
tray_thread = Thread(target=create_icon, daemon=True)
tray_thread.start()

keyboard.wait()
