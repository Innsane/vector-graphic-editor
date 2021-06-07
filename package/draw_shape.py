from enum import Enum

from PyQt5 import QtGui
from PyQt5.QtGui import QPen, QPixmap

TOOLBAR_HEIGHT = 21


class Shapes(Enum):
    LINE = 'line'
    CIRCLE = 'circle'
    ELLIPSE = 'ellipse'
    SQUARE = 'square'
    RECTANGLE = 'rectangle'
    TRIANGLE = 'triangle'
    STAR = 'star'


class DrawShape:
    def __init__(self, pixmap: QPixmap, pen: QPen):
        self.last_x = None
        self.last_y = None
        self.shape = Shapes.LINE
        self.pixmap = pixmap
        self.pen = pen

    def draw(self, last_y, last_x, e):
        pass

    def draw_ellipse(self, e):
        painter = QtGui.QPainter(self.pixmap)
        painter.setRenderHint(QtGui.QPainter.Antialiasing, True)
        painter.setPen(self.pen)
        painter.drawEllipse(self.last_x, self.last_y, e.x()-self.last_x, e.y()+TOOLBAR_HEIGHT-self.last_y)
        painter.end()

    def draw_circle(self, e):
        painter = QtGui.QPainter(self.pixmap)
        painter.setRenderHint(QtGui.QPainter.Antialiasing, True)
        painter.setPen(self.pen)
        painter.drawEllipse(self.last_x, self.last_y, e.x()-self.last_x, e.x()-self.last_x)

    def draw_rectangle(self, e):
        painter = QtGui.QPainter(self.pixmap)
        painter.setRenderHint(QtGui.QPainter.Antialiasing, True)
        painter.setPen(self.pen)
        painter.drawRect(self.last_x, self.last_y, e.x()-self.last_x, e.y()+TOOLBAR_HEIGHT-self.last_y)
        painter.end()

    def draw_square(self, e):
        painter = QtGui.QPainter(self.pixmap)
        painter.setRenderHint(QtGui.QPainter.Antialiasing, True)
        painter.setPen(self.pen)
        painter.drawRect(self.last_x, self.last_y, e.x()-self.last_x, e.x()-self.last_x)
        painter.end()

    def draw_triangle(self, e):
        painter = QtGui.QPainter(self.pixmap)
        painter.setRenderHint(QtGui.QPainter.Antialiasing, True)
        painter.setPen(self.pen)
        painter.drawRect(self.last_x, self.last_y, e.x()-self.last_x, e.x()-self.last_x)


    def draw_star(self, e):
        painter = QtGui.QPainter(self.pixmap)
        painter.setRenderHint(QtGui.QPainter.Antialiasing, True)
        painter.setPen(self.pen)
        painter.drawRect(self.last_x, self.last_y, e.x()-self.last_x, e.x()-self.last_x)
        painter.end()

