import time

import pyautogui


def check_panda_svc():
    pyautogui.doubleClick()
    time.sleep(0.1)
    pyautogui.press("p")
    time.sleep(0.5)
    pyautogui.press("esc")
    pyautogui.moveRel(0, -24)


def epdr_installing():
    pyautogui.write(
        "Removed old license form the EPDR console.\n Installed certificates.\n Waiting for EPDR to finish installing"
    )
