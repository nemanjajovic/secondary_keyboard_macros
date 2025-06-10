import os
import threading
import time
import tkinter as tk
from tkinter import simpledialog

import keyboard
import pyautogui
import pygetwindow as gw
import pymsgbox
import pyperclip
from clipboard_modifier import modify_copied_content  # Make sure this exists
from functions import check_panda_svc
from tray import run_tray_icon

# === CONFIGURATION ===
path = "C://Users/nj250196/OneDrive - NCR Corporation/Desktop/secondary_keyboard_macros"
keyboard_selector = "'2FE3714A'"
cord_x, cord_y = 593, 211
cmd_position = (757, 111)
icon_path = f"{path}/res/icon.png"  # Tray icon

# === CLICK COMMANDS ===
positions = {
    "st": [(493, 114), (564, 144)],
    "fl": [(493, 114), (559, 172)],
    "conf": [(493, 114), (579, 229)],
    "check": [(412, 108), (482, 241)],
    "svc": [(576, 113)],
    "rl": [(1901, 582)],
}
command_actions = {
    key: lambda first=pos[0], second=pos[1] if len(pos) > 1 else None: (
        (pyautogui.click(first), time.sleep(0.2), pyautogui.click(second))
        if second
        else pyautogui.click(first)
    )
    for key, pos in positions.items()
}
command_actions.update(
    {
        "cmd": lambda: pyautogui.click(cmd_position),
        "del": lambda: (
            os.remove("c:/users/nj250196/downloads/WatchGuard Agent.msi")
            if os.path.exists("c:/users/nj250196/downloads/WatchGuard Agent.msi")
            else print("File not found.")
        ),
    }
)
path_commands = {
    "lp": "%IBERDIR%/LANProxy/LanProxy",
    "temp": "c:\\temp",
    "panda": "c:\\ProgramData\\Panda Security\\Panda Aether Agent\\Downloads",
    "proxyboh": "c:\\CMCLanDesk\\NSS LANProxy",
    "proxyterm": "c:\\CMCLanDesk\\NSS LANProxy Handler",
    "programdata": "c:\\ProgramData",
    "programfiles": "c:\\program files (x86)",
}
shell_commands = {
    "ip": "ipconfig /all",
    "wginst": 'msiexec /i "c:\\temp\\WatchGuard Agent.msi" /qn /L*V "c:\\temp\\WatchGuardAgent.log"',
    "setproxy": "c:\\temp\\setproxyallusers.bat ",
    "wgproxy": "c:\\temp\\wgsetproxyallusers.bat",
    "mkdir": "mkdir c:\\temp",
    "sys": "systeminfo",
    "arp": "arp -a",
    "certinst": "C:\\Temp\\CertCheck\\CertCheck /add /ca && C:\\Temp\\CertCheck\\WESCertcheck /add /ca",
    "lpinst": "%IBERDIR%\\LANProxy\\LANProxy\\InstallLANProxy.bat",
    "ps": 'C:\\temp\\psinfo.exe -d:"[AETHERUPDATE FULL | LITE]" /nogui',
    "tls": "c:\\temp\\tlsfix.exe",
    "lpremove": 'taskkill /f /im lanproxy.exe && sc config lanproxy start= disabled && sc delete lanproxy & rmdir /s /q "%LOCALDIR%\\EPS" & rmdir /s /q "%LOCALDIR%\\LANProxy"',
    "host": "hostname",
    "restart panda": "net stop PandaAetherAgent && net start PandaAetherAgent",
    "sys": "systeminfo",
    "checkbit": 'systeminfo | findstr /i /c:"System Type"',
    "checksha": "systeminfo | findstr KB3140245 & systeminfo | findstr KB4474419",
    "checktls": 'reg query "HKEY_LOCAL_MACHINE\\SYSTEM\\CurrentControlSet\\Control\\SecurityProviders\\SCHANNEL\\Protocols\\TLS 1.2\\Client"',
    "cleanpanda": 'rmdir /s /q "C:\\Program Files (x86)\\Panda Security" && rmdir /s /q "C:\\ProgramData\\Panda Security"',
    "cleantemp": 'del /q "C:\\temp"',
    "sha1": "wusa.exe c:\\temp\\kb4474419.msu /quiet /norestart /log:c:\\temp\\kb4474419.log",
    "sha2": "wusa.exe c:\\temp\\kb3140245.msu /quiet /norestart /log:c:\\temp\\kb3140245.log",
    "redist32": "C:\\temp\\vcredist2015_2017_2019_2022_x86 /quiet /norestart",
    "redist64": "C:\\temp\\vcredist2015_2017_2019_2022_x64 /quiet /norestart",
    "proxy32term": "c:\\temp\\NSSProxySetup_32bit.exe -device_type=term -host=ALOHABOH -port=9180 -fallback_ip=",
    "proxy64term": "c:\\temp\\NSSProxySetup_64bit.exe -device_type=term -host=ALOHABOH -port=9180 -fallback_ip=",
    "proxy64boh": "c:\\temp\\NSSProxySetup_64bit.exe -device_type=boh -port=9180 -offline",
}


# === FUNCTIONAL CORE ===
def start_lua():
    with open(f"{path}/luascript.lua", "r") as f:
        pyperclip.copy(f.read())
    modify_copied_content("local keyboardIdentifier", keyboard_selector)
    os.startfile(f"{path}/LuaMacros.exe")
    time.sleep(2)
    pyautogui.hotkey("ctrl", "v")
    if keyboard_selector != "'0000AAA'":
        pyautogui.click(cord_x, cord_y)
        gw.getActiveWindow().minimize()


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


def read_macro_file():
    try:
        with open(f"{path}/keypressed.txt", "r") as f:
            key = f.read().strip()
        if key == "1":
            execute_command(command="ip")
        elif key == "up":
            # Check panda services
            check_panda_svc()
        elif key == "left":
            pyautogui.hotkey("ctrl", "shift", "tab")
        elif key == "right":
            pyautogui.hotkey("ctrl", "tab")
        elif key == "q":
            close_program()
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


def close_program(*_):
    try:
        open(f"{path}/keypressed.txt", "w").close()
        os.system("taskkill /f /im luamacros.exe")
    except Exception as e:
        print(f"Error during shutdown: {e}")
    print("Exiting...")
    os._exit(0)


# === RUNTIME ===
if __name__ == "__main__":
    start_lua()
    pymsgbox.alert("Program started", "Alert")

    keyboard.on_press(on_f24)
    threading.Thread(target=ctrl_f_listener, daemon=True).start()
    threading.Thread(
        target=run_tray_icon(icon_path, close_program), daemon=True
    ).start()

    print("Listening for hotkeys...")
    keyboard.wait()  # Keeps script alive
