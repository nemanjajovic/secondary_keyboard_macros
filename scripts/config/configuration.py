import os
from pathlib import Path

user_profile = os.environ["USERPROFILE"]

# === CONFIGURATION ===
cwd = Path.cwd()  # get current working directory where main.py is
path = cwd / ".."  # set the base path to one directory behind ./scripts/
keyboard_selector = "'0000AAB'"  # Change to "'0000AAA'" if you want manual selection of keyboard every time LuaMacro starts
cmd_position = (757, 111)
icon_path = f"{path}/res/icon.png"  # Tray icon
