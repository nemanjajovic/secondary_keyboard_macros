import time

import pyautogui


def is_present(img_path, confidence=0.9):
    return pyautogui.locateOnScreen(img_path, confidence=confidence)


# This function accepts 2 image file paths
def wait_for_program(
    img_path1, img_path2, timeout=30, scan_frequency=1.0, confidence=0.9
):
    time_start = time.time()

    while True:
        if is_present(img_path1, confidence) or is_present(img_path2, confidence):
            return True
        if time.time() - time_start > timeout:
            return False
        time.sleep(scan_frequency - ((time.time() - time_start) % scan_frequency))


# EXAMPLE USAGE
# wg_login_path = "images/wg_login.png"

# if wait_for_program(wg_login_path, timeout=15):
#     print("Found login screen — continuing macro.")
# else:
#     print("Login screen not found — taking alternate action.")
