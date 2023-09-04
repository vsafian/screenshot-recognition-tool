import dearpygui.dearpygui as dpg

from user_interface.window_settings import WindowSettings as WinSet

from text_buffer.buffer import TextBuffer
from user_interface.interface import View
from controller.controller import Controller


def run_app(controller: Controller) -> None:
    # Run app GUI
    dpg.create_viewport(title=WinSet.WINDOW_NAME,
                        width=WinSet.WIN_WIDTH,
                        height=WinSet.WIN_HEIGHT,
                        resizable=False,
                        max_width=WinSet.WIN_WIDTH,
                        max_height=WinSet.WIN_HEIGHT,
                        small_icon=WinSet.SMALL_ICON
                        )
    dpg.setup_dearpygui()
    dpg.show_viewport()
    window = controller.view.WINDOW
    dpg.set_primary_window(window, True)
    dpg.start_dearpygui()
    dpg.destroy_context()


if __name__ == "__main__":
    buffer = TextBuffer()
    view = View()
    controller = Controller(buffer=buffer, view=view)
    run_app(controller)
