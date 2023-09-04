import dearpygui.dearpygui as dpg

from typing import Callable


class WindowControl:

    @staticmethod
    def show_items(*args: int | str) -> None:
        for item in args:
            dpg.show_item(item)

    @staticmethod
    def hide_items(*args: int | str) -> None:
        for item in args:
            dpg.hide_item(item)

    @staticmethod
    def change_color(item: int | str,
                     color: tuple[int] | list[int]) -> None:
        dpg.configure_item(item, color=color)

    @staticmethod
    def hide_window(func: Callable) -> Callable:
        def wrapper(*args, **kwargs) -> None:
            width, height = tuple(dpg.get_viewport_pos())
            dpg.minimize_viewport()
            func(*args, **kwargs)
            dpg.maximize_viewport()
            dpg.set_viewport_pos([float(width), float(height)])
        return wrapper
