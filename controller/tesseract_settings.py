from path_manager.bild_file_path import bild_path


class TesseractSettings:
    ENG, UKR, RUS, = "English", "Ukrainian", "Russian"

    TESSERACT_LANGUAGES = {
       ENG: "eng",
       UKR: "ukr+eng",
       RUS: "rus+eng",
       }

    TESSERACT_CONFIGS_PATHS = {
        ENG: bild_path(("tesseract_configs", "eng_code_config.txt")),
        UKR: bild_path(("tesseract_configs", "сyrillic_eng_config.txt")),
        RUS: bild_path(("tesseract_configs", "сyrillic_eng_config.txt"))
    }

