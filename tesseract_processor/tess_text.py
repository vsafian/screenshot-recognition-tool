from pytesseract import pytesseract
from PIL.Image import Image

from pytesseract.pytesseract import (image_to_data, Output)

from tesseract_processor.bild_text_line import bild_text_line
from tesseract_processor.find_empy_lines_ import find_empty_lines

from tesseract_processor.functions import Functions
from tesseract_processor.constants import (
    TESS_CMD_PATH,
    WIDTH, HEIGHT,
    TOP, LEFT, TEXT,
    TOP_LEVEL,
    START_POINT,
    ENG_CONFIG
)

from screenshot_app.screenshot_tool import get_screenshot


class TesseractText(Functions):
    def __init__(self, image: Image,
                 language: str, config: str) -> None:
        self.text = ""
        pytesseract.tesseract_cmd = TESS_CMD_PATH
        self.original_data = image_to_data(
            image=image, lang=language,
            config=config, output_type=Output.DICT
        )

        self.text_section = self.section(TEXT)
        self.width_section = self.section(WIDTH)
        self.height_section = self.section(HEIGHT)
        self.top_section = self.section(TOP)
        self.left_section = self.section(LEFT)

        self.indexation = [
            index
            for index, word in enumerate(self.text_section)
            if len(str(word).strip())
        ]
        self.heights = []
        self.top_points = []
        self.left_points = []

        self.pixel_width = 0
        self.minimal_height = 0
        self.middle_height = 0
        self.maximal_height = 0
        self.cropped_height = 0
        self.min_left = 0
        self.min_top = 0

        self.word_data = []

        self.top_positions = []

        self.top_groups = {}

        self.top_indents = {}

        if self.indexation:
            self.run_processing()

    def run_processing(self) -> None:
        self.heights = self.get_section_values(self.height_section)

        self.top_points = self.get_section_values(self.top_section)
        self.left_points = self.get_section_values(self.left_section)

        self.pixel_width = self.find_average_pixel_width()

        self.minimal_height = min(self.heights)
        self.middle_height = self.get_average_value(self.heights)
        self.maximal_height = max(self.heights)
        self.cropped_height = self.middle_height - self.minimal_height

        self.min_left = min(self.left_points)
        self.min_top = min(self.top_points)

        self.word_data = self.write_word_data()

        self.top_positions = self.no_duplicates(
            self.get_list_dicts_data(
                data=self.word_data,
                key=TOP_LEVEL,
                sort_it=True
            )
        )

        self.top_groups = self.create_groups_of_top(self.middle_height)

        self.top_indents = find_empty_lines(
            top_groups=self.top_groups,
            word_data=self.word_data,
            height_difference=self.cropped_height,
            middle_pixel_height=self.middle_height,
            max_pixel_height=self.maximal_height
        )
        self.text = self.bild_output_text()

    def section(self, key: str) -> list[int] | list[str]:
        return self.original_data[key]

    def find_average_pixel_width(self) -> int:
        pixels = []
        for index in self.indexation:
            word = str(self.text_section[index])
            width = int(self.width_section[index])
            pixel = width // len(word)
            pixels.append(pixel)
        return self.get_average_value(pixels)

    def get_section_values(self,
                           section: list) -> list[int] | list[str]:
        return [
            section[index]
            for index in self.indexation
        ]

    def write_word_data(self) -> list[dict]:
        word_info = []
        for index in self.indexation:
            word = str(self.text_section[index])
            left_pos = int(self.left_section[index])
            top_pos = int(self.top_section[index])
            width = int(self.width_section[index])
            left = left_pos - self.min_left
            left = self.value_or_zero(left)
            top = top_pos - self.min_top
            top = self.value_or_zero(top)
            word_info.append({
                TEXT: word,
                TOP_LEVEL: top,
                START_POINT: left,
                WIDTH: (left, left + width),
            })
        return word_info

    def create_groups_of_top(self,
                             middle_height: int) -> dict[int: list[int]]:
        """
        This method groped words by a similar TOP indentation.
        It is necessary for determination of
        which words should fall into which group.
        """
        result = {}
        current_group = []
        group_index = 0
        for number in self.top_positions:
            if not current_group or (
                    number - current_group[-1]
                    in range(0, middle_height)
            ):
                current_group.append(number)
            else:
                result[group_index] = current_group
                current_group = [number]
                group_index += 1
        if current_group:
            result[group_index] = current_group
        return result

    def bild_output_text(self) -> str:
        text = ""
        for index, group in self.top_groups.items():
            current_group = []
            for word in self.word_data:
                if word[TOP_LEVEL] in group:
                    current_group.append(word)
            text_line = bild_text_line(group=current_group,
                                       pixel_width=self.pixel_width)
            text += "\n" * self.top_indents[index]
            text += text_line
        return text

    def get_text(self) -> str:
        return self.text


if __name__ == "__main__":
    image = get_screenshot()
    lang = "eng"
    config = ENG_CONFIG
    tess_data = TesseractText(image, lang, config)
    image.close()
