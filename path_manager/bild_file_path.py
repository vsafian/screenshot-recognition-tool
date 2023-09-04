import os


def bild_path(path_and_file: tuple):
    path = os.path.join(*path_and_file)
    return os.path.join(os.path.dirname(__file__), '..', path)


if __name__ == '__main__':
    path_and_file = "data", "сyrillic_eng_config.txt"
    print(bild_path(path_and_file))
