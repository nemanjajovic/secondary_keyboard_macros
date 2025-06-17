import threading
import time

import keyboard
import pyautogui

sf_clicker_running = False  # Controls whether the thread should run
click_thread = None


def salesforce_clicker():
    while sf_clicker_running:
        pyautogui.click()
        time.sleep(20)


def toggle_clicker():
    global sf_clicker_running, click_thread
    if sf_clicker_running:
        sf_clicker_running = False
        print("Clicking stopped.")
    else:
        sf_clicker_running = True
        click_thread = threading.Thread(target=salesforce_clicker, daemon=True)
        click_thread.start()
        print("Clicking started.")


keyboard.add_hotkey("f8", toggle_clicker)
