from path_manager.bild_file_path import bild_path


TESS_CMD_PATH = bild_path(("tesseract_data", "Tesseract-OCR", "tesseract.exe"))
ENG_CONFIG = config = bild_path(("tesseract_configs", "сyrillic_eng_config.txt"))

WIDTH, HEIGHT = "width", "height"
TOP, LEFT = "top", "left"
TEXT = "text"
LEFT_INDENT = "left_ident"
TOP_LEVEL = "top_level"
START_POINT = "start_point"
