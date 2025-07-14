# import threading
# import time
# import winsound

# import keyboard
# import pyautogui
# import pyperclip
# from on_cursor_change import on_cursor_change

# sf_clicker_running = False  # Controls whether the thread should run
# click_thread = None


# # Check if HOS ENT NSS and NSS Antivirus is present in the clipboard and then play sound if True
# def check_clipboard():
#     # Get text from clipboard
#     clipboard_text = pyperclip.paste()

#     # Check for keywords
#     contains_keywords = (
#         "HOS ENT NSS" in clipboard_text and "NSS Antivirus" in clipboard_text
#     )
#     print(contains_keywords)
#     if contains_keywords:
#         winsound.Beep(450, 300)
#         winsound.Beep(450, 300)


# def salesforce_clicker():
#     while sf_clicker_running:
#         pyautogui.click(403, 430)
#         time.sleep(0.1)
#         pyautogui.click(1769, 342)
#         pyautogui.moveTo(1817, 429)
#         on_cursor_change(0.5, lambda: print("Page loaded"))
#         pyautogui.moveTo(1739, 430)
#         pyautogui.mouseDown()
#         pyautogui.moveTo(97, 430)
#         pyautogui.mouseUp()
#         pyautogui.hotkey("ctrl", "c")
#         check_clipboard()
#         time.sleep(30)


# def toggle_clicker():
#     global sf_clicker_running, click_thread
#     if sf_clicker_running:
#         sf_clicker_running = False
#         print("Clicking stopped.")
#     else:
#         sf_clicker_running = True
#         click_thread = threading.Thread(target=salesforce_clicker, daemon=True)
#         click_thread.start()
#         print("Clicking started.")


# keyboard.add_hotkey("f8", toggle_clicker)
# print("Press F8 to toggle the clicker. Press Esc to exit")
# keyboard.wait("Esc")


# # Start coordinates for drag and copy
# # 1767,433
# # End coordinates for drag and copy
# # 97,430
