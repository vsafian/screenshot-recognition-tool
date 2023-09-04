import dearpygui.dearpygui as dpg
import pyperclip
from PIL.Image import Image

from controller.tesseract_settings import TesseractSettings as TessSet
from screenshot_app.screenshot_tool import get_screenshot

from user_interface.interface import View

from user_interface.labels import Labels
from user_interface.window_settings import WindowSettings as WinSet
from user_interface.features import UserInterfaceFunctions as Interface


from tesseract_processor.tess_text import TesseractText


from text_buffer.buffer import TextBuffer



class Controller:
    def __init__(self,
                 buffer: TextBuffer,
                 view: View,
                 ) -> None:
        self.buffer = buffer
        self.view = view

        self.mode_selection = {
            Labels.COMBINE_MODE: self.configurate_view_for_combine_mode,
            Labels.SINGLE_MODE: self.configurate_view_for_single_mode
        }

        self.start_mode = {
                Labels.COMBINE_MODE: self.combine_run,
                Labels.SINGLE_MODE: self.single_run
            }

        dpg.set_item_callback(self.view.radio_buttons,
                              self.change_work_mode)

        dpg.set_item_callback(
            self.view.snipping_combo_box,
            self.update_user_combo_choice
        )

        dpg.set_item_callback(
            self.view.extract_button,
            self.activate_extraction
        )

        dpg.set_item_callback(
            self.view.end_button,
            self.combine_end
        )

        self.work_mode = dpg.get_value(
            self.view.radio_buttons
        )

        self.user_combo_language = dpg.get_value(
            self.view.snipping_combo_box)

        self.is_user_massage_visible = False

    def change_work_mode(self) -> None:
        # Зміна режимів роботи по ключу radio button
        mod_key = dpg.get_value(self.view.radio_buttons)
        self.work_mode = mod_key
        self.mode_selection[mod_key]()
        if self.is_user_massage_visible:
            dpg.hide_item(self.view.messages_panel)
            dpg.hide_item(self.view.user_message)
            self.is_user_massage_visible = False

    def configurate_view_for_combine_mode(self) -> None:
        # Змінити розмір кнопки extract та показати кнопку end.
        dpg.set_item_width(self.view.extract_button,
                           width=WinSet.COMBINE_WIDTH)
        dpg.show_item(self.view.end_button)

    def configurate_view_for_single_mode(self) -> None:
        # Приховати кнопку end, та повернути вихідний розмір кнопці
        # extract.
        dpg.hide_item(self.view.end_button)
        dpg.configure_item(self.view.extract_button,
                           width=WinSet.SINGLE_WIDTH)

    def update_user_combo_choice(self) -> None:
        # Отримати та оновити ключ мови з combobox.
        self.user_combo_language = dpg.get_value(
            self.view.snipping_combo_box)

    def get_screenshot_text(self, screenshot: Image) -> None:
        language = TessSet.TESSERACT_LANGUAGES[
            self.user_combo_language]
        config = TessSet.TESSERACT_CONFIGS_PATHS[
            self.user_combo_language]
        text_item = TesseractText(
            image=screenshot,
            config=config,
            language=language
        )
        self.buffer.set_text(text_item.get_text())

    def single_run(self) -> None:
        # Виконання дій в одинарному режимі
        text = self.buffer.get_text()
        pyperclip.copy(text)
        self.view.messages.success_message.show_message(
            item=self.view.user_message
        )
        self.is_user_massage_visible = True

    def combine_run(self) -> None:
        text = self.buffer.get_text()
        self.buffer.update_combine_fill(text)
        count = self.buffer.count
        if count == 1:
            self.view.messages.combine_first.show_message(
                item=self.view.user_message
            )
        else:
            self.view.messages.combine_more_than_one.show_message(
                item=self.view.user_message,
                text_count=count
            )
        self.is_user_massage_visible = True

    def combine_end(self) -> None:
        self.view.messages.success_message.show_message(
            item=self.view.user_message
        )
        text = self.buffer.get_combine_fill()
        pyperclip.copy(text)
        self.buffer.clear_combine_fill()
        self.is_user_massage_visible = True

    def is_screenshot_taken(self, screenshot: Image) -> bool:
        if isinstance(screenshot, Image):
            return True
        else:
            self.view.messages.screenshot_not_taken.show_message(
                item=self.view.user_message
            )
            self.is_user_massage_visible = True
            return False

    def is_text_found(self, text: str) -> bool:
        if text:
            return True
        else:
            self.view.messages.no_text_found.show_message(
                item=self.view.user_message
            )
            self.is_user_massage_visible = True
            return False

    @Interface.hide_window
    def activate_extraction(self) -> None:
        dpg.show_item(self.view.messages_panel)
        screenshot = get_screenshot()
        if self.is_screenshot_taken(screenshot):
            self.get_screenshot_text(screenshot)
            text = self.buffer.get_text()
            if self.is_text_found(text):
                self.start_mode[self.work_mode]()
