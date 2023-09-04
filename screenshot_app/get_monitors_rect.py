from screeninfo import get_monitors


def get_monitors_rect() -> tuple:
    """This function calculate current monitor size and position"""
    monitors = get_monitors()
    min_x = min(monitor.x for monitor in monitors)
    max_x = max(monitor.x + monitor.width for monitor in monitors)
    min_y = min(monitor.y for monitor in monitors)
    max_y = max(monitor.y + monitor.height for monitor in monitors)
    width = max_x - min_x
    height = max_y - min_y
    return min_x, min_y, width, height


if __name__ == "__main__":
    print(get_monitors_rect())
