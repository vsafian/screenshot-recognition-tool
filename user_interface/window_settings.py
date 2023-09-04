from file_path.bild_file_path import bild_path


class WindowSettings:
    WINDOW_NAME = "OCR Snipping tool"
    SMALL_ICON = bild_path(("data", "surgical-scissors-48 .ico"))
    WIN_WIDTH = 370
    WIN_HEIGHT = 200
    COMBO_WIDTH = 130
    GROUP_TOP_INDENT = 10
    SINGLE_WIDTH = 340
    COMBINE_WIDTH = SINGLE_WIDTH // 2
