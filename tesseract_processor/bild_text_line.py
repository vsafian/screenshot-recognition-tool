from tesseract_processor.dict_keys import Keys
from tesseract_processor.use_cases import BildLineCase


def find_spaces_between_words(words_sizes: list[tuple[int, int]],
                              width: int) -> list[int]:
    words_sizes.reverse()
    spaces_between_words = []
    for index, length in enumerate(words_sizes):
        fist_word_start_point = length[0]
        next_word_index = index + 1
        if next_word_index < len(words_sizes):
            next_word_end_point = words_sizes[next_word_index][1]
            space_count = (fist_word_start_point - next_word_end_point) // width
            spaces_between_words.append(space_count if space_count >= 0 else 0)
    spaces_between_words.reverse()
    return spaces_between_words


def bild_text_line(group: list[dict],
                   pixel_width: int) -> str:
    order = [
        word_info[Keys.START_POINT]
        for word_info in group]
    order = sorted(order)
    sizes = [
        word_info[Keys.WIDTH]
        for point in order
        for word_info in group
        if word_info[Keys.START_POINT] == point
    ]
    spaces = find_spaces_between_words(sizes, pixel_width)
    text_line = ""
    for index, point in enumerate(order):
        for word_info in group:
            if word_info[Keys.START_POINT] == point:
                if index == 0:
                    left_ident = word_info[Keys.START_POINT] // pixel_width
                    text_line += " " * left_ident
                text_line += word_info[Keys.TEXT]
        if index < len(spaces):
            text_line += " " * spaces[index]
    text_line += "\n"
    return text_line


if __name__ == "__main__":
    case = BildLineCase
    print(bild_text_line(case.group, case.pixel_width))





