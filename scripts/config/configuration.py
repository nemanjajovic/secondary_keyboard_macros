import os

user_profile = os.environ["USERPROFILE"]

# === CONFIGURATION ===
path = f"{user_profile}/Desktop/secondary_keyboard_macros"
keyboard_selector = (
    "'0000BBB'"  # Change to "'0000AAA'" if 0000BBB fails for some reason
)
cord_x, cord_y = 593, 211
cmd_position = (757, 111)
icon_path = f"{path}/res/icon.png"  # Tray icon
