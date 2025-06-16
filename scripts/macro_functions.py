import os
import time

import pyautogui

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
