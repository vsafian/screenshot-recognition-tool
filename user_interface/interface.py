import dearpygui.dearpygui as dpg

from controller.tesseract_settings import TesseractSettings as TessSet

from user_interface.window_settings import WindowSettings as WinSet
from user_interface.labels import Labels as Label
from user_interface.messages import UserTexts


class View:
    """This is realisation user interface for app"""
    def __init__(self) -> None:
        self.messages = UserTexts()
        self.window_width = WinSet.WIN_WIDTH
        self.window_height = WinSet.WIN_HEIGHT
        dpg.create_context()
        with dpg.handler_registry():
            with dpg.window(
                    width=self.window_width,
                    height=self.window_height) as self.WINDOW:
                dpg.add_spacer(height=5)

                # The Radio buttons for changing work mode
                with dpg.group(horizontal=True) as self.work_modes_panel:
                    dpg.add_text(Label.WORK_MODE_TEXT)
                    single, combine = Label.SINGLE_MODE, Label.COMBINE_MODE
                    self.radio_buttons = dpg.add_radio_button(
                        items=[single, combine],
                        default_value=single,
                        horizontal=True,
                    )

                dpg.add_spacer(height=WinSet.GROUP_TOP_INDENT)

                # The combobox for changing the work language.
                with dpg.group(horizontal=True) as self.languages_panel:
                    self.lang_text = dpg.add_text(Label.LANGUAGES_TEXT)
                    self.snipping_combo_box = dpg.add_combo(
                        items=list(TessSet.TESSERACT_LANGUAGES),
                        default_value=TessSet.ENG,
                        width=WinSet.COMBO_WIDTH)

                dpg.add_spacer(height=WinSet.GROUP_TOP_INDENT)

                # The buttons for activating current work mode.
                with dpg.group(horizontal=True) as self.buttons_panel:
                    self.extract_button = dpg.add_button(
                        label=Label.EXTRACT_BTN_TEXT,
                        width=WinSet.SINGLE_WIDTH)

                    self.end_button = dpg.add_button(
                        label=Label.END_BTN_TEXT,
                        show=False,
                        width=WinSet.COMBINE_WIDTH
                    )

                dpg.add_spacer(height=WinSet.GROUP_TOP_INDENT)

                # Massages part
                with dpg.group(horizontal=True, show=False) as self.messages_panel:
                    self.user_message = dpg.add_text()








