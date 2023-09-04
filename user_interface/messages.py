import dearpygui.dearpygui as dpg

RED = [255, 0, 0]
GREEN = [0, 255, 0]
N = "_"


class TextProperties:
    def __init__(self, text: str,
                 color: tuple[int] | list[int],
                 indent: int) -> None:
        self.text = text
        self.color = color
        self.indent = indent

    def show_message(self, item: int | str,
                     text_count: int = 0) -> None:
        dpg.show_item(item)
        dpg.configure_item(item, color=self.color)
        dpg.set_item_indent(item, self.indent)
        if N in self.text:
            dpg.set_value(item, self.text.replace(N, str(text_count)))
        else:
            dpg.set_value(item, self.text)


class UserTexts:
    # Описати всі можливі стани і пов'язані з ними властивості
    def __init__(self) -> None:
        self.no_text_found = TextProperties(
            text="No text found!",
            color=RED,
            indent=120)

        self.screenshot_not_taken = TextProperties(
            text="Screenshot not taken!",
            color=RED,
            indent=95
        )

        self.combine_first = TextProperties(
            f"You captured 1 fragment!",
            color=GREEN,
            indent=80)

        self.combine_more_than_one = TextProperties(
            text=f"You captured {N} fragments!",
            color=GREEN,
            indent=80,
            )

        self.success_message = TextProperties(
            text="The fragment has been added to the clipboard!",
            color=GREEN,
            indent=10)


