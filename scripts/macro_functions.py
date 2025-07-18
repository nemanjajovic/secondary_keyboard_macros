import os
import threading
import time

import pyautogui
import pyperclip
from on_cursor_change import on_cursor_change
from wait_for_program import wait_for_program

# Initialize %USERPROFILE% system variable. eg. user_path = "C:\\Users\\User"
user_path = os.environ["USERPROFILE"]


# Start services and check for Panda service. Must set the mouse manually on starting position
def check_panda_svc():
    pyautogui.doubleClick()  # Double clicks on service query
    time.sleep(0.1)
    pyautogui.press("p")  # Move to services starting with P
    time.sleep(0.5)
    pyautogui.press("esc")  # Exit services query after 0.5 seconds
    pyautogui.moveRel(0, -24)  # Move up 24 pixels relative to current mouse position
    print("Service query finished.")


# Write for generic EPDR reinstall cases
def epdr_installing():
    pyautogui.write(
        "Removed old license form the EPDR console.\nInstalled certificates.\nWaiting for EPDR to finish installing"
    )
    print("EPDR installing message written")


# Transfer NSS folder to host machine (Third file from above in Downloads folder)
def transfer_nss():
    try:
        # Move the agent from downloads to nss folder, replace if it already exists
        os.replace(
            f"{user_path}\\Downloads\\WatchGuard Agent.msi",
            f"{user_path}\\Downloads\\nss\\WatchGuard Agent.msi",
        )
    except FileNotFoundError:
        print(
            "WatchGuard Agent.msi not found in Downloads folder. Skipping the operation."
        )
    pyautogui.click(
        1900, 580
    )  # Click on GO where t:\temp is so we refresh the host machine window
    pyautogui.moveTo(510, 285)  # Move to third file from above in Downloads folder
    pyautogui.mouseDown()  # Click down
    pyautogui.dragTo(1300, 285, 0.3)  # Drag to the host machine window
    pyautogui.mouseUp()  # Release the click
    pyautogui.press("f5")


def epdr_auto_download():
    pyautogui.click(1764, 338)
    time.sleep(1)
    pyautogui.click(732, 444)
    pyautogui.moveTo(1068, 750)
    on_cursor_change(0.5, lambda: pyautogui.click())


def find_site():
    pyautogui.click(188, 971)
    pyautogui.hotkey("ctrl", "a")
    pyautogui.hotkey("ctrl", "v")
    pyautogui.click(446, 971)
    query_services()


def query_services():
    pyautogui.click(578, 111)
    pyautogui.moveTo(678, 811)


sentences = {
    "epdr_update_disabled": "EPDR Update disabled",
    "settings": "Settings",
    "per_computer_settings": "Per-computer settings",
    "is_equal_to": "Is equal to",
}

positions = {
    "search_account_form_x": 200,
    "serach_account_form_y": 280,
    "computers_tab_x": 450,
    "computers_tab_y": 280,
    "filter_three_dots_x": 583,
    "filter_three_dots_y": 439,
    "reports_three_dots_x": 446,
    "reports_three_dots_y": 438,
}

SLEEP_SHORT = 0.2
SLEEP_NORMAL = 0.4
SLEEP_LONG = 0.8
SLEEP_VERY_LONG = 1.2
SLEEP_ULTRA_LONG = 2
CHROME_TAB_FORWARD = "forward"
CHROME_TAB_BACKWARD = "backward"

wiggle_stop_event = threading.Event()


# sleep() easier to write than time.sleep()
def sleep(duration=0.4):
    time.sleep(duration)


# In certain situations pyautogui.click() just wont work
def delicate_click():
    pyautogui.mouseDown()
    time.sleep(0.2)
    pyautogui.mouseUp()
    time.sleep(0.2)


# Switch chrome tab forward or backward
def switch_chrome_tab(direction="forward"):
    if direction == "forward":
        pyautogui.hotkey("ctrl", "tab")
    elif direction == "backward":
        pyautogui.hotkey("ctrl", "shift", "tab")


def copy_past_wait_tab(sentence):
    sleep(SLEEP_NORMAL)
    pyperclip.copy(sentences[sentence])
    sleep(SLEEP_SHORT)
    pyautogui.hotkey("ctrl", "v")
    sleep(SLEEP_NORMAL)


def wiggle_mouse():
    while not wiggle_stop_event.is_set():
        pyautogui.moveRel(0, 2)
        sleep(SLEEP_SHORT)
        pyautogui.moveRel(0, -2)


def start_wiggle():
    # Reset the stop event each time before starting
    wiggle_stop_event.clear()
    threading.Thread(target=wiggle_mouse, daemon=True).start()


def stop_wiggle():
    wiggle_stop_event.set()


def smooth_scroll_down(total_scroll, steps, delay):
    scroll_amount = -total_scroll // steps  # Negative for downward scroll
    for _ in range(steps):
        pyautogui.scroll(scroll_amount)
        time.sleep(delay)


def move_to_center(img_path1, img_path2, confidence=0.9):
    location = pyautogui.locateCenterOnScreen(img_path1, confidence=confidence)
    if not location:
        location = pyautogui.locateCenterOnScreen(img_path2, confidence=confidence)

    if location:
        pyautogui.moveTo(location)
        return True
    else:
        print("Neither image found on screen.")
        return False


def open_account():
    pyautogui.hotkey("ctrl", "c")  # Copy Account Name from the excel sheet
    sleep(SLEEP_SHORT)
    switch_chrome_tab(CHROME_TAB_BACKWARD)  # Switch chrome tab to WG EPDR
    sleep(SLEEP_SHORT)
    pyautogui.click(
        positions["search_account_form_x"], positions["serach_account_form_y"]
    )  # Click on Search Account field
    sleep(SLEEP_NORMAL)
    pyautogui.hotkey("ctrl", "a")  # Select all (if any text is present in the field)
    # Paste the copied text from the excel sheet to the account search form
    pyautogui.hotkey("ctrl", "v")
    sleep(SLEEP_VERY_LONG)
    pyautogui.press("down")  # Select the first item from the dropdown list
    pyautogui.press("enter")  # Enter the selected account
    sleep(SLEEP_NORMAL)
    pyautogui.moveTo(positions["computers_tab_x"], positions["computers_tab_y"])
    sleep(SLEEP_NORMAL)
    start_wiggle()
    on_cursor_change(0.01, lambda: pyautogui.click())
    stop_wiggle()
    pyautogui.moveTo(
        positions["reports_three_dots_x"], positions["reports_three_dots_y"]
    )
    sleep(
        SLEEP_ULTRA_LONG
    )  # There is currently no way to handle this than to wait a fixed amount of time
    smooth_scroll_down(total_scroll=1000, steps=4, delay=0.01)
    sleep(SLEEP_NORMAL)
    if wait_for_program("../res/reports.png", "../res/reports2.png", timeout=10):
        if move_to_center("../res/reports.png", "../res/reports2.png"):
            print("Image found")
            sleep(SLEEP_SHORT)
            pyautogui.moveRel(200, 0)
            sleep(SLEEP_NORMAL)
            delicate_click()

            # TEST
            sleep(SLEEP_NORMAL)
            switch_chrome_tab(CHROME_TAB_FORWARD)
            sleep(SLEEP_NORMAL)
            pyautogui.press("down")
    else:
        print("Cant locate image on screen, abort.....")
        return
