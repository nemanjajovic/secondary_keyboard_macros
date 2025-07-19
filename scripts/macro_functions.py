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
    "computer": "Computer",
    "sha256": "Supports SHA-256 signed",
    "false": "False",
    "sha256_title": "SHA-256 Error",
}

positions = {
    "search_account_form_x": 200,
    "serach_account_form_y": 280,
    "computers_tab_x": 450,
    "computers_tab_y": 280,
    "filters_x": 450,
    "filters_y": 388,
    "rename_filter_x": 913,
    "rename_filter_y": 372,
}

SLEEP_SHORT = 0.2
SLEEP_NORMAL = 0.4
SLEEP_LONG = 0.8
SLEEP_VERY_LONG = 1.2
SLEEP_ULTRA_LONG = 2
CHROME_TAB_FORWARD = "forward"
CHROME_TAB_BACKWARD = "backward"

reports_img_1 = "../res/reports.png"
reports_img_2 = "../res/reports2.png"

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
    pyautogui.press("tab")


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


def confirmation():
    return pyautogui.confirm(
        text="Confirmation", title="Confirmation", buttons=["Yes", "No", "Cancel"]
    )


def click_on_reports():
    if wait_for_program(reports_img_1, reports_img_2, timeout=10):
        if move_to_center(reports_img_1, reports_img_2):
            print("Image found")
            sleep(SLEEP_SHORT)
            pyautogui.moveRel(200, 0)
            sleep(SLEEP_NORMAL)
            delicate_click()
    else:
        print("Reports image not found")
        return


def create_report(type):
    click_on_reports()
    if wait_for_program("../res/add_filter.png", "../res/add_filter2.png", timeout=10):
        print("Add Filter image found")
        move_to_center(
            "../res/add_filter.png", "../res/add_filter2.png", confidence=0.9
        )
        # add_filter = pyautogui.locateCenterOnScreen("../res/add_filter.png")
        # pyautogui.moveTo(add_filter)
        delicate_click()
        pyautogui.moveTo(positions["rename_filter_x"], positions["rename_filter_y"])
        on_cursor_change(0.1, lambda: print("Add filter popup ready"))
        if type == "EPDR Update disabled":
            copy_past_wait_tab("epdr_update_disabled")
            copy_past_wait_tab("settings")
            copy_past_wait_tab("per_computer_settings")
            copy_past_wait_tab("is_equal_to")
            copy_past_wait_tab("epdr_update_disabled")
        elif type == "SHA-256":
            copy_past_wait_tab("sha256_title")
            copy_past_wait_tab("computer")
            copy_past_wait_tab("sha256")
            copy_past_wait_tab("is_equal_to")
            copy_past_wait_tab("false")

    else:
        print("Add Filter image not found")


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
    pyautogui.moveTo(positions["filters_x"], positions["filters_y"])
    if wait_for_program("../res/filters.png", "../res/filters2.png", timeout=10):
        smooth_scroll_down(total_scroll=1000, steps=4, delay=0.01)
        sleep(SLEEP_NORMAL)
        create_report()
        sleep(SLEEP_NORMAL)
        pyautogui.hotkey("ctrl", "tab")
        sleep(SLEEP_NORMAL)
        pyautogui.press("down")
    else:
        print("Filters image not found")
        return
