import os
import time

import pyautogui
import pymsgbox
import pyperclip
from on_cursor_change import on_cursor_change

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
    "epdr_disabled": "EPDR Disabled",
    "settings": "Settings",
    "workstations_and_servers": "Workstations and Servers",
    "is_equal_to": "Is equal to",
    "nss_disable_av": "NSS Disable AV Settings",
    "or": "OR",
    "nss_audit_threatdefender_only": "NSS Audit mode - Threat Defender Only",
    "nss_audit_threatdefender_and_av": "NSS Audit mode - Threat Defender and AV",
    "epdr_offline": "EPDR Offline",
    "computer": "Computer",
    "last_connection": "Last connection",
    "not_within_the_last": "Not within the last",
    "30": "30",
    "day": "Day",
    "nemanja": "nemanja.jovic@ncrvoyix.com",
    "sasa": "sasa.kozarcanin@ncrvoyix.com",
    "epdr_disabled_subject": "[EPDR Disabled] - ",
    "epdr_offline_subject": "[EPDR Offline] - ",
    "reports": "Reports",
}

positions = {
    "weekly_x": 976,
    "weekly_y": 493,
    "weekly_second_x": 901,
    "weekly_second_y": 554,
    "reduced_x": 961,
    "reduced_y": 707,
    "to_x": 980,
    "to_y": 776,
    "cc_x": 975,
    "cc_y": 828,
}


def epdr_disabled_report():
    pyperclip.copy(sentences["epdr_disabled"])
    pyautogui.hotkey("ctrl", "v")
    pyautogui.press("tab")
    time.sleep(0.4)
    pyperclip.copy(sentences["settings"])
    pyautogui.hotkey("ctrl", "v")
    time.sleep(0.4)
    pyautogui.press("tab")
    time.sleep(0.4)
    pyperclip.copy(sentences["workstations_and_servers"])
    pyautogui.hotkey("ctrl", "v")
    time.sleep(0.4)
    pyautogui.press("tab")
    time.sleep(0.4)
    pyperclip.copy(sentences["is_equal_to"])
    pyautogui.hotkey("ctrl", "v")
    time.sleep(0.4)
    pyautogui.press("tab")
    time.sleep(0.4)
    pyperclip.copy(sentences["nss_disable_av"])
    pyautogui.hotkey("ctrl", "v")
    time.sleep(0.4)
    pyautogui.press("tab")
    time.sleep(0.4)
    pyautogui.click(1585, 458)
    time.sleep(0.4)
    pyautogui.click(712, 497)
    pyperclip.copy(sentences["or"])
    pyautogui.hotkey("ctrl", "v")
    time.sleep(0.4)
    pyautogui.press("tab")
    time.sleep(0.4)
    pyperclip.copy(sentences["settings"])
    pyautogui.hotkey("ctrl", "v")
    time.sleep(0.4)
    pyautogui.press("tab")
    time.sleep(0.4)
    pyperclip.copy(sentences["workstations_and_servers"])
    pyautogui.hotkey("ctrl", "v")
    time.sleep(0.4)
    pyautogui.press("tab")
    time.sleep(0.4)
    pyperclip.copy(sentences["is_equal_to"])
    pyautogui.hotkey("ctrl", "v")
    time.sleep(0.4)
    pyautogui.press("tab")
    time.sleep(0.4)
    pyperclip.copy(sentences["nss_audit_threatdefender_only"])
    pyautogui.hotkey("ctrl", "v")
    time.sleep(0.4)
    pyautogui.press("tab")
    time.sleep(0.4)
    pyautogui.click(1585, 458)
    time.sleep(0.4)
    pyautogui.click(712, 497)
    pyperclip.copy(sentences["or"])
    pyautogui.hotkey("ctrl", "v")
    time.sleep(0.4)
    pyautogui.press("tab")
    time.sleep(0.4)
    pyperclip.copy(sentences["settings"])
    pyautogui.hotkey("ctrl", "v")
    time.sleep(0.4)
    pyautogui.press("tab")
    time.sleep(0.4)
    pyperclip.copy(sentences["workstations_and_servers"])
    pyautogui.hotkey("ctrl", "v")
    time.sleep(0.4)
    pyautogui.press("tab")
    time.sleep(0.4)
    pyperclip.copy(sentences["is_equal_to"])
    pyautogui.hotkey("ctrl", "v")
    time.sleep(0.4)
    pyautogui.press("tab")
    time.sleep(0.4)
    pyperclip.copy(sentences["nss_audit_threatdefender_and_av"])
    pyautogui.hotkey("ctrl", "v")
    time.sleep(0.4)
    pyautogui.press("tab")
    time.sleep(0.4)
    pyautogui.click(1476, 772)


def epdr_offline_report():
    # print("epdr offline")
    pyautogui.moveTo(571, 895)
    time.sleep(1)
    pyautogui.mouseDown()
    time.sleep(0.2)
    pyautogui.mouseUp()
    time.sleep(0.5)
    pyautogui.moveTo(627, 745)
    time.sleep(1)
    pyautogui.mouseDown()
    time.sleep(0.2)
    pyautogui.mouseUp()
    time.sleep(2)
    pyperclip.copy(sentences["epdr_offline"])
    pyautogui.hotkey("ctrl", "v")
    time.sleep(0.4)
    pyautogui.press("tab")
    time.sleep(0.4)
    pyperclip.copy(sentences["computer"])
    pyautogui.hotkey("ctrl", "v")
    time.sleep(0.4)
    pyautogui.press("tab")
    time.sleep(0.4)
    pyperclip.copy(sentences["last_connection"])
    pyautogui.hotkey("ctrl", "v")
    time.sleep(0.4)
    pyautogui.press("tab")
    time.sleep(0.4)
    pyperclip.copy(sentences["not_within_the_last"])
    pyautogui.hotkey("ctrl", "v")
    time.sleep(0.4)
    pyautogui.press("tab")
    time.sleep(0.4)
    pyperclip.copy(sentences["30"])
    pyautogui.hotkey("ctrl", "v")
    time.sleep(0.4)
    pyautogui.press("tab")
    time.sleep(0.4)
    pyperclip.copy(sentences["day"])
    pyautogui.hotkey("ctrl", "v")
    time.sleep(0.4)
    pyautogui.press("tab")
    time.sleep(0.4)
    pyautogui.click(1476, 772)


def schedule_disabled():
    # print("scheduled disable report")
    pyautogui.moveTo(570, 897)
    time.sleep(1)
    pyautogui.mouseDown()
    time.sleep(0.2)
    pyautogui.mouseUp()
    time.sleep(0.5)
    pyautogui.moveTo(647, 872)
    time.sleep(1)
    pyautogui.mouseDown()
    time.sleep(0.2)
    pyautogui.mouseUp()
    time.sleep(2)
    pyautogui.hotkey("ctrl", "a")
    time.sleep(0.5)
    pyperclip.copy(sentences["epdr_disabled"])
    pyautogui.hotkey("ctrl", "v")
    time.sleep(0.5)
    pyautogui.press("tab")
    time.sleep(0.5)
    pyautogui.press("tab")
    time.sleep(0.5)
    pyautogui.press("enter")
    time.sleep(0.5)
    pyautogui.press("up")
    time.sleep(0.5)
    pyautogui.press("enter")
    time.sleep(0.5)
    pyautogui.click(positions["reduced_x"], positions["reduced_y"])
    time.sleep(0.5)
    pyautogui.click(positions["to_x"], positions["to_y"])
    time.sleep(0.5)
    pyperclip.copy(sentences["nemanja"])
    pyautogui.hotkey("ctrl", "v")
    time.sleep(0.5)
    pyautogui.press("tab")
    time.sleep(0.5)
    pyautogui.press("tab")
    time.sleep(0.5)
    pyperclip.copy(sentences["sasa"])
    pyautogui.hotkey("ctrl", "v")
    time.sleep(0.5)
    pyautogui.press("tab")
    time.sleep(0.5)
    pyautogui.press("tab")
    time.sleep(0.5)
    pyautogui.press("tab")
    time.sleep(0.5)
    pyperclip.copy(sentences["epdr_disabled_subject"])
    pyautogui.hotkey("ctrl", "v")
    time.sleep(0.5)
    pyautogui.hotkey("ctrl", "tab")
    time.sleep(0.5)
    pyautogui.hotkey("ctrl", "c")
    time.sleep(0.5)
    pyautogui.hotkey("ctrl", "shift", "tab")
    time.sleep(0.5)
    pyautogui.hotkey("ctrl", "v")
    pyautogui.click(1306, 946)


def schedule_offline():
    # print("scheduled offline report")
    pyautogui.moveTo(572, 931)
    time.sleep(1)
    pyautogui.mouseDown()
    time.sleep(0.2)
    pyautogui.mouseUp()
    time.sleep(0.5)
    pyautogui.moveTo(647, 907)
    time.sleep(1)
    pyautogui.mouseDown()
    time.sleep(0.2)
    pyautogui.mouseUp()
    time.sleep(2)
    pyautogui.hotkey("ctrl", "a")
    time.sleep(0.5)
    pyperclip.copy(sentences["epdr_offline"])
    pyautogui.hotkey("ctrl", "v")
    time.sleep(0.5)
    pyautogui.press("tab")
    time.sleep(0.5)
    pyautogui.press("tab")
    time.sleep(0.5)
    pyautogui.press("enter")
    time.sleep(0.5)
    pyautogui.press("up")
    time.sleep(0.5)
    pyautogui.press("enter")
    time.sleep(0.5)
    pyautogui.click(positions["reduced_x"], positions["reduced_y"])
    time.sleep(0.5)
    pyautogui.click(positions["to_x"], positions["to_y"])
    time.sleep(0.5)
    pyperclip.copy(sentences["nemanja"])
    pyautogui.hotkey("ctrl", "v")
    time.sleep(0.5)
    pyautogui.press("tab")
    time.sleep(0.5)
    pyautogui.press("tab")
    time.sleep(0.5)
    pyperclip.copy(sentences["sasa"])
    pyautogui.hotkey("ctrl", "v")
    time.sleep(0.5)
    pyautogui.press("tab")
    time.sleep(0.5)
    pyautogui.press("tab")
    time.sleep(0.5)
    pyautogui.press("tab")
    time.sleep(0.5)
    pyperclip.copy(sentences["epdr_offline_subject"])
    pyautogui.hotkey("ctrl", "v")
    time.sleep(0.5)
    pyautogui.hotkey("ctrl", "tab")
    time.sleep(0.5)
    pyautogui.hotkey("ctrl", "c")
    time.sleep(0.5)
    pyautogui.hotkey("ctrl", "shift", "tab")
    time.sleep(0.5)
    pyautogui.hotkey("ctrl", "v")
    pyautogui.click(1306, 946)


def use_epdr_dialogue():
    return pymsgbox.confirm(
        text="Does the account use EPDR?", title="Confirmation", buttons=["Yes", "No"]
    )


def switch_epdr_account():
    pyautogui.hotkey("ctrl", "c")
    time.sleep(0.5)
    pyautogui.hotkey("ctrl", "shift", "tab")
    time.sleep(0.5)
    pyautogui.hotkey("ctrl", "v")
    time.sleep(1.5)
    pyautogui.press("down")
    time.sleep(0.5)
    pyautogui.press("enter")
    if use_epdr_dialogue() == "No":
        time.sleep(0.5)
        pyautogui.hotkey("ctrl", "tab")
        time.sleep(0.5)
        pyautogui.hotkey("ctrl", "shift", "-")
        time.sleep(0.5)
        pyautogui.press("down")
        time.sleep(0.5)
        pyautogui.press("down")
    else:
        time.sleep(0.5)
        pyautogui.click(446, 286)
        time.sleep(1)
        pyautogui.moveTo(570, 438)
        time.sleep(1)
        pyautogui.mouseDown()
        time.sleep(0.2)
        pyautogui.mouseUp()
        time.sleep(0.5)
        pyautogui.moveTo(621, 454)
        time.sleep(1)
        pyautogui.mouseDown()
        time.sleep(0.2)
        pyautogui.mouseUp()
        time.sleep(1)
        pyperclip.copy(sentences["reports"])
        pyautogui.hotkey("ctrl", "v")
        time.sleep(0.5)
        pyautogui.click(1303, 430)
        time.sleep(0.5)
        pyautogui.moveTo(571, 929)
        time.sleep(1)
        pyautogui.mouseDown()
        time.sleep(0.2)
        pyautogui.mouseUp()
        time.sleep(0.5)
        pyautogui.moveTo(627, 785)
        time.sleep(1)
        pyautogui.mouseDown()
        time.sleep(0.2)
        pyautogui.mouseUp()
        time.sleep(0.5)
