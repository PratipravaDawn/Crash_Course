import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def asset(*parts):
    return os.path.join(BASE_DIR, *parts)

FPS = 40
SCREENSIZE = (640, 640)

CAR_IMAGE_PATHS = {
    "forward": asset("sources", "images", "forward.png"),
    "dleft": asset("sources", "images", "drift left.png"),
    "dright": asset("sources", "images", "drift right.png"),
    "sleft": asset("sources", "images", "slide left.png"),
    "sright": asset("sources", "images", "slide right.png"),
    "broke": asset("sources", "images", "brocken.png")
}

FREE_PATH = {
    "block": asset("sources", "images", "road block.png"),
    "money": asset("sources", "images", "money.png")
}

START_SCREEN_PATH = asset("sources", "images", "BG.png")

FONT_PATH = asset("sources", "font", "Caveat-VariableFont_wght.ttf")

MUSIC_PATH = asset(
    "sources", "music",
    "background_music.ogg"
)

MONEY_SOUND_PATH = asset("sources", "music", "cash register.ogg")
CRASH_SOUND_PATH = asset("sources", "music", "crash.ogg")