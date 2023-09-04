import dearpygui.dearpygui as dpg

from typing import Callable


class UserInterfaceFunctions:
    @staticmethod
    def hide_window(func: Callable) -> Callable:
        def wrapper(*args, **kwargs) -> None:
            width, height = tuple(dpg.get_viewport_pos())
            dpg.minimize_viewport()
            func(*args, **kwargs)
            dpg.maximize_viewport()
            dpg.set_viewport_pos([float(width), float(height)])
        return wrapper
