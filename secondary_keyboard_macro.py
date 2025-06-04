import os
import time
from threading import Thread

import keyboard
import pyautogui
import pygetwindow
import pyperclip
import pystray
from PIL import Image, ImageDraw

from clipboard_modifier import modify_copied_content

# Target line to modify in clipboard
target_variable = "local keyboardIdentifier"


# Keyboard selection will be added later to the tkinter GUI so we can select the keyboard we want
class KeyboardSelection:
    work_keyboard = "'2FE3714A'"
    home_keyboard = "'14C79465'"


def start_lua():
    with open("./luascript.lua", "r") as file:
        pyperclip.copy(file.read())
    # Change KeyboardSelection to either home_keyboard or work_keyboard
    modify_copied_content(target_variable, KeyboardSelection.home_keyboard)
    os.startfile("C://Users/User/Desktop/luamacros/LuaMacros.exe")
    time.sleep(2)
    pyautogui.hotkey("ctrl", "v")
    pyautogui.click(473, 169)
    pygetwindow.getActiveWindow().minimize()


def close_program():
    os.system("taskkill /f /im luamacros.exe")
    print("Closing the Python script...")
    time.sleep(1)
    print("SUCCESS: Python process has been terminated")
    os._exit(0)


start_lua()

file_path = "C:\\Users\\User\\Desktop\\luamacros\\keypressed.txt"


def read_file():
    try:
        with open(file_path, "r") as file:
            content = file.read().strip()
            if content == "k":
                close_program()  # I will not keep this as a macro since I have a tray icon to kill this program, leaving for testing purposes for now
            elif content == "b":
                os.startfile(
                    "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Brave.lnk"
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
    icon_image = Image.open("./res/icon.png")
    menu = (pystray.MenuItem("Exit", close_program),)
    icon = pystray.Icon("LuaMacros", icon_image, "LuaMacros Manager", menu)
    icon.run()


# Start tray icon in a separate thread
tray_thread = Thread(target=create_icon, daemon=True)
tray_thread.start()

keyboard.wait()
