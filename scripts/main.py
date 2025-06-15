import os
import threading
import time
import tkinter as tk
from tkinter import simpledialog

import keyboard
import pyautogui
import pygetwindow as gw
from commands.commands_paths_positions import path_commands, positions, shell_commands
from config.configuration import cmd_position, icon_path, path
from macro_functions import check_panda_svc, epdr_installing
from on_cursor_change import on_cursor_change
from start_lua import start_lua
from tray import run_tray_icon

command_actions = {
    key: lambda first=pos[0], second=pos[1] if len(pos) > 1 else None: (
        # If a second position exists, click both with a slight pause between
        (pyautogui.click(first), time.sleep(0.2), pyautogui.click(second))
        if second
        else pyautogui.click(first)  # Otherwise, click the first position only
    )
    for key, pos in positions.items()
}


def execute_command(command):
    command = command.strip().lower()
    if command in command_actions:
        command_actions[command]()
    elif command in path_commands:
        pyautogui.click(1483, 582)
        time.sleep(0.2)
        pyautogui.hotkey("ctrl", "a")
        time.sleep(0.2)
        pyautogui.write(path_commands[command])
        pyautogui.press("enter")
    elif command in shell_commands:
        pyautogui.click(*cmd_position)
        time.sleep(0.2)
        pyautogui.write(shell_commands[command])
    else:
        print(f"Error: '{command}' is not a recognized command.")


def is_target_window_active():
    active = gw.getActiveWindow()
    return active and active.title == "Command Center Client 20.1 [cmcnua.ncrsaas.com]"


def show_input_window():
    root = tk.Tk()
    root.withdraw()
    command = simpledialog.askstring("Input", "Enter command:")
    if command:
        execute_command(command)


def close_program():
    open(f"{path}/keypressed.txt", "w").close()  # Clear keypressed.txt content
    open(f"{path}/luaoutput.txt", "w").close()  # Clear luaoutput.txt content
    os.system("taskkill /f /im luamacros.exe")  # Kill LUAMacros.exe
    os._exit(0)  # Kill the script, I know its bad but it works


# === MAIN SECOND KEYBOARD MACRO FUNCTIONALITY ===
KEY_ACTIONS = {
    # "up": check_panda_svc,
    # "left": lambda: pyautogui.hotkey("ctrl", "shift", "tab"),
    # "right": lambda: pyautogui.hotkey("ctrl", "tab"),
    "q": close_program,
    "w": lambda: epdr_installing(),
    "e": lambda: on_cursor_change(
        0.5, lambda: pyautogui.click()
    ),  # click on cursor change
    "r": lambda: print("R"),
    "t": lambda: execute_command(command="temp"),
    "y": lambda: print("Y"),
    "u": lambda: print("U"),
    "i": lambda: print("I"),
    "o": lambda: print("O"),
    "p": lambda: print("P"),
    "leftbracket": lambda: print("["),
    "rightbracket": lambda: print("]"),
}


def read_macro_file():
    with open(f"{path}\keypressed.txt", "r") as f:
        key = f.read().strip()
    action = KEY_ACTIONS.get(key)
    # if action key is found within KEY_ACTIONS run it
    if action:
        action()


def on_f24(event):
    if event.name == "f24" and event.event_type == "down":
        read_macro_file()


# Listen for CTRL+F and show input window for commands only if CMC window is active
def ctrl_f_listener():
    while True:
        keyboard.wait("ctrl+f")
        if is_target_window_active():
            show_input_window()
        else:
            print("Target window not active")


# === RUNTIME ===
if __name__ == "__main__":
    start_lua()
    keyboard.on_press(on_f24)
    threading.Thread(target=ctrl_f_listener, daemon=True).start()
    threading.Thread(
        target=run_tray_icon(icon_path, close_program), daemon=True
    ).start()
    print("Listening for hotkeys...")
    keyboard.wait()  # Keeps script alive
