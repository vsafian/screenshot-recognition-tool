from tesseract_processor.dict_keys import Keys
from tesseract_processor.use_cases import EmptyLineCase


def find_empty_lines(top_groups: dict[int: tuple[int, int]],
                     word_data: list[dict],
                     height_difference: int,
                     middle_pixel_height: int,
                     max_pixel_height: int) -> dict[int: int]:
    """This function search top indents
    between top position of word groups."""

    height_overlap = max_pixel_height + height_difference
    heights_levels = []
    for index, group in top_groups.items():
        heights = []
        for word in word_data:
            if word[Keys.TOP_LEVEL] in group:
                heights.append(word[Keys.TOP_LEVEL])
        heights_levels.append(min(heights))
    output = {}

    for index, current_level in enumerate(heights_levels):
        indent = 0
        if index:
            previous_top = heights_levels[index - 1]
            previous_end_point = previous_top + middle_pixel_height
            difference = current_level - previous_end_point
            indent = difference // height_overlap
        output[index] = indent
    return output


if __name__ == '__main__':
    case = EmptyLineCase
    print(find_empty_lines(top_groups=case.top_groups, word_data=case.word_data,
                           height_difference=case.height_difference,
                           middle_pixel_height=case.middle_height,
                           max_pixel_height=case.max_height))
