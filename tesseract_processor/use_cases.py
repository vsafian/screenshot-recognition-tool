class BildLineCase:
    group = [{'text': 'return', 'top_level': 220, 'start_point': 1, 'width': (2, 80), 'height': 237},
             {'text': 'os.path.normpath(os.path.join(self.target,', 'top_level': 218, 'start_point': 100,
              'width': (100, 646), 'height': 235},
             {'text': 'parent,', 'top_level': 220, 'start_point': 715, 'width': (715, 806), 'height': 237},
             {'text': 'basename)', 'top_level': 218, 'start_point': 830, 'width': (830, 947), 'height': 235},
             {'text': ')', 'top_level': 214, 'start_point': 958, 'width': (958, 971), 'height': 231}]
    pixel_width = 19


class EmptyLineCase:
    top_groups = {0: [0, 1, 9],
                  1: [31, 33, 37, 40],
                  2: [95, 96, 100],
                  3: [126, 131, 134],
                  4: [188, 189, 193],
                  5: [214, 218, 220]}
    word_data = [
        {'text': 'basename', 'top_level': 1, 'start_point': 1, 'width': (1, 112), 'height': 18},
        {'text': '=', 'top_level': 9, 'start_point': 129, 'width': (129, 141), 'height': 26},
        {'text': 'os.path.basename(fileid)', 'top_level': 0, 'start_point': 157, 'width': (157, 496), 'height': 17},
        {'text': 'name,', 'top_level': 37, 'start_point': 1, 'width': (1, 66), 'height': 54},
        {'text': 'ext', 'top_level': 33, 'start_point': 86, 'width': (86, 126), 'height': 50},
        {'text': '=', 'top_level': 40, 'start_point': 143, 'width': (143, 155), 'height': 57},
        {'text': 'os.path.splitext(basename)', 'top_level': 31, 'start_point': 172, 'width': (172, 538), 'height': 48},
        {'text': '#', 'top_level': 96, 'start_point': 0, 'width': (0, 13), 'height': 113},
        {'text': 'Сконструировать', 'top_level': 96, 'start_point': 29, 'width': (29, 241), 'height': 113},
        {'text': 'имя', 'top_level': 100, 'start_point': 258, 'width': (258, 297), 'height': 117},
        {'text': 'файла', 'top_level': 95, 'start_point': 314, 'width': (314, 383), 'height': 112},
        {'text': 'с', 'top_level': 100, 'start_point': 401, 'width': (401, 412), 'height': 117},
        {'text': 'расширением', 'top_level': 100, 'start_point': 429, 'width': (429, 585), 'height': 117},
        {'text': '.pickle', 'top_level': 95, 'start_point': 604, 'width': (604, 698), 'height': 112},
        {'text': 'basename', 'top_level': 126, 'start_point': 1, 'width': (1, 112), 'height': 143},
        {'text': '=', 'top_level': 134, 'start_point': 129, 'width': (129, 141), 'height': 151},
        {'text': 'name', 'top_level': 131, 'start_point': 158, 'width': (158, 212), 'height': 148},
        {'text': '+', 'top_level': 131, 'start_point': 228, 'width': (228, 241), 'height': 148},
        {'text': "'.pickle'", 'top_level': 126, 'start_point': 262, 'width': (262, 379), 'height': 143},
        {'text': '#', 'top_level': 189, 'start_point': 0, 'width': (0, 13), 'height': 206},
        {'text': 'Вернуть', 'top_level': 189, 'start_point': 29, 'width': (29, 126), 'height': 206},
        {'text': 'путь', 'top_level': 193, 'start_point': 144, 'width': (144, 198), 'height': 210},
        {'text': 'к', 'top_level': 193, 'start_point': 215, 'width': (215, 227), 'height': 210},
        {'text': 'файлу', 'top_level': 188, 'start_point': 242, 'width': (242, 313), 'height': 205},
        {'text': 'относительно', 'top_level': 193, 'start_point': 329, 'width': (329, 498), 'height': 210},
        {'text': 'корня', 'top_level': 193, 'start_point': 515, 'width': (515, 583), 'height': 210},
        {'text': 'целевого', 'top_level': 193, 'start_point': 601, 'width': (601, 712), 'height': 210},
        {'text': 'корпуса.', 'top_level': 193, 'start_point': 730, 'width': (730, 837), 'height': 210},
        {'text': 'return', 'top_level': 220, 'start_point': 2, 'width': (2, 83), 'height': 237},
        {'text': 'os.path.normpath(os.path.join(self.target,', 'top_level': 218, 'start_point': 100, 'width': (100, 694), 'height': 235},
        {'text': 'parent,', 'top_level': 220, 'start_point': 715, 'width': (715, 808), 'height': 237},
        {'text': 'basename)', 'top_level': 218, 'start_point': 830, 'width': (830, 967), 'height': 235},
        {'text': ')', 'top_level': 214, 'start_point': 958, 'width': (958, 972), 'height': 231}
    ]
    max_height = 32
    middle_height = 17
    height_difference = 7


