from file_path.bild_file_path import bild_path


class TesseractSettings:
    ENG, RUS, UKR = "English", "Russian", "Ukrainian"

    TESSERACT_LANGUAGES = {
       ENG: "eng",
       RUS: "rus+eng",
       UKR: "ukr+eng",
        }

    TESSERACT_CONFIGS_PATHS = {
        ENG: bild_path(("data", "eng_code_config.txt")),
        UKR: bild_path(("data", "сyrillic_eng_config.txt")),
        RUS: bild_path(("data", "сyrillic_eng_config.txt"))
    }

    TRANSLATE_LANGS = {
        ENG: "en",
        RUS: "ru",
        UKR: "uk"
    }
