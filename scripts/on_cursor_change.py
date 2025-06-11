import time

import win32gui


# Retrieves the current mouse cursor handle
def get_cursor_handle():
    try:
        cursor_info = win32gui.GetCursorInfo()
        return cursor_info[1]  # Returns the handle part of the cursor info
    except Exception as e:
        print(f"Error retrieving cursor info: {e}")
        return None


# Monitors the mouse cursor at intervals and triggers a callback when it changes
def on_cursor_change(interval, callback):
    print("Watching for cursor change...")
    last_cursor = get_cursor_handle()

    while True:
        time.sleep(interval)  # Wait for the specified time before checking again
        current_cursor = get_cursor_handle()
        if current_cursor != last_cursor:
            callback()  # Execute callback function on cursor change
            break


# Example usage:
# on_cursor_change(0.5, callback_func)
