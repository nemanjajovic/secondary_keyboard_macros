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


def close_program(*_):
    try:
        open(f"{path}/keypressed.txt", "w").close()
        os.system("taskkill /f /im luamacros.exe")
    except Exception as e:
        print(f"Error during shutdown: {e}")
    print("Exiting...")
    os._exit(0)


# === MAIN SECOND KEYBOARD MACRO FUNCTIONALITY ===
KEY_ACTIONS = {
    "1": lambda: on_cursor_change(
        0.5, lambda: pyautogui.click()
    ),  # click on cursor change
    "up": check_panda_svc,
    "left": lambda: pyautogui.hotkey("ctrl", "shift", "tab"),
    "right": lambda: pyautogui.hotkey("ctrl", "tab"),
    "t": lambda: execute_command(command="temp"),
    "q": close_program,
    "s": lambda: print("ssss"),
    "w": lambda: epdr_installing(),
}


def read_macro_file():
    file_path = os.path.join(path, "keypressed.txt")
    try:
        with open(file_path, "r") as f:
            key = f.read().strip()
        action = KEY_ACTIONS.get(key)
        if action:
            action()
        else:
            print(f"Keyboard 2: {key}")
    except FileNotFoundError:
        print("keypressed.txt not found.")


def on_f24(event):
    if event.name == "f24" and event.event_type == "down":
        read_macro_file()


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
