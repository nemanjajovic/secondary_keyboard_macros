import pystray
from PIL import Image


def run_tray_icon(icon_path, close_program):
    try:
        icon_img = Image.open(icon_path)
    except:
        icon_img = Image.new("RGB", (64, 64), color="red")
    icon = pystray.Icon(
        "LuaMacrosManager",
        icon_img,
        "LuaMacros Manager",
        menu=pystray.Menu(pystray.MenuItem("Exit", close_program)),
    )
    icon.run()
