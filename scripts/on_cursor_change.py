import time

import win32gui


def get_cursor_handle():
    try:
        cursor_info = win32gui.GetCursorInfo()
        return cursor_info[1]  # Cursor handle
    except Exception as e:
        print(f"Error retrieving cursor info: {e}")
        return None


def on_cursor_change(interval, callback):
    print("Watching for cursor change...")
    last_cursor = get_cursor_handle()

    while True:
        time.sleep(interval)
        current_cursor = get_cursor_handle()
        if current_cursor != last_cursor:
            callback()
            break


# on_cursor_change(0.5, callback_func)
