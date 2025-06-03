import os
import time

import keyboard
import pyautogui
import pygetwindow
import pyperclip

# pyautogui.mouseInfo()


def start_lua():
    with open("./luascript.lua", "r") as file:
        pyperclip.copy(file.read())
        os.startfile("C://Users/User/Desktop/luamacros/LuaMacros.exe")
        time.sleep(1.5)
        pyautogui.hotkey("ctrl", "v")
        pyautogui.click(473, 169)
        pygetwindow.getActiveWindow().minimize()


def close_program():
    os.system("taskkill /f /im luamacros.exe")
    print("Closing the python script...")
    time.sleep(1)
    print(
        "SUCCESS: Python process has been terminated"
    )  # Lets make our console a little pretty shall we?
    os._exit(0)


start_lua()

file_path = "C:\\Users\\User\\Desktop\\luamacros\\keypressed.txt"


def read_file():
    try:
        with open(file_path, "r") as file:
            content = file.read().strip()
            if content == "k":
                close_program()  # this kills python and lua
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
keyboard.wait()
