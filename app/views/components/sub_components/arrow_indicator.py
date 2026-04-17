# app/views/components/sub_components/arrow_indicator.py
from PySide6.QtCore import Property, QPropertyAnimation, QEasingCurve
from PySide6.QtGui import QPainter, QPen
from PySide6.QtWidgets import QWidget


class ArrowIndicator(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        self._angle = 0

        self.setFixedSize(16, 16)

        self.animation = QPropertyAnimation(self, b"angle")
        self.animation.setDuration(160)
        self.animation.setEasingCurve(QEasingCurve.Type.OutCubic)

    def get_angle(self):
        return self._angle

    def set_angle(self, value):
        self._angle = value
        self.update()

    angle = Property(float, get_angle, set_angle)

    def rotate(self, expanded):

        self.animation.stop()

        start = self._angle
        end = 90 if expanded else 0

        self.animation.setStartValue(start)
        self.animation.setEndValue(end)
        self.animation.start()

    def paintEvent(self, event):

        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)

        pen = QPen(self.palette().color(self.foregroundRole()))
        pen.setWidth(2)

        painter.setPen(pen)

        w = self.width()
        h = self.height()

        painter.translate(w / 2, h / 2)
        painter.rotate(self._angle)
        painter.translate(-w / 2, -h / 2)

        painter.drawLine(w * 0.35, h * 0.25, w * 0.65, h * 0.5)
        painter.drawLine(w * 0.35, h * 0.75, w * 0.65, h * 0.5)