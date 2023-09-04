import mss
import sys
import os

import PIL.Image
from PIL import Image

from PyQt5 import (QtWidgets, QtCore, QtGui)

from screenshot_app.get_monitors_rect import get_monitors_rect
from screenshot_app.show_image import show_image


class SnippingTool(QtWidgets.QWidget):
    output_image = None

    def __init__(self) -> None:
        super().__init__()
        self.monitors_size = get_monitors_rect()
        with mss.mss() as sct:
            self.screenshot = sct.shot(mon=-1)
            self.image = Image.open(self.screenshot)
        self.setGeometry(*self.monitors_size)
        self.setWindowTitle(" ")
        self.begin = QtCore.QPoint()
        self.end = QtCore.QPoint()
        self.setWindowOpacity(0.3)
        QtWidgets.QApplication.setOverrideCursor(
            QtGui.QCursor(QtCore.Qt.CrossCursor)
        )

        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.show()

    def keyPressEvent(self, event) -> None:
        if event.key() == QtCore.Qt.Key_Q:
            self.close()
        event.accept()

    def paintEvent(self, event) -> None:
        qp = QtGui.QPainter(self)
        qp.setPen(QtGui.QPen(QtGui.QColor("black"), 3))
        qp.setBrush(QtGui.QColor(128, 128, 255, 128))
        qp.drawRect(QtCore.QRect(self.begin, self.end))

    def mousePressEvent(self, event) -> None:
        self.begin = event.pos()
        self.end = self.begin
        self.update()

    def mouseMoveEvent(self, event) -> None:
        self.end = event.pos()
        self.update()

    @staticmethod
    def is_rectangle_area_correct(points: tuple[int, int, int, int]) -> bool:
        x1, y1, x2, y2 = points
        return True if x2 > x1 or y2 > y1 else False

    def mouseReleaseEvent(self, event) -> None:
        self.close()
        x1 = min(self.begin.x(), self.end.x())
        y1 = min(self.begin.y(), self.end.y())
        x2 = max(self.begin.x(), self.end.x())
        y2 = max(self.begin.y(), self.end.y())
        area = (x1, y1, x2, y2)
        if self.is_rectangle_area_correct(area):
            self.output_image = self.image.crop(area)

        self.image.close()
        os.remove(self.screenshot)


def get_screenshot() -> Image:
    """
    Screenshot app initiation function.
    """
    app_activator = QtWidgets.QApplication(sys.argv)
    snipping_window = SnippingTool()
    snipping_window.show()
    app_activator.aboutToQuit.connect(app_activator.deleteLater)
    app_activator.exec_()
    return snipping_window.output_image


if __name__ == "__main__":
    screenshot = get_screenshot()
    if isinstance(screenshot, PIL.Image.Image):
        show_image(screenshot)


