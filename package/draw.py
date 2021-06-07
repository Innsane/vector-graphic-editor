from enum import Enum

from PyQt5 import QtGui, Qt
from PyQt5.QtGui import QColor, QPen
from PyQt5.QtWidgets import QLabel, QMainWindow

from package.draw_shape import DrawShape, Shapes

TOOLBAR_HEIGHT = 21


class MyLabel(QLabel):
    def __init__(self, parent: QMainWindow):
        super().__init__(parent)
        self.setup()
        self.last_x, self.last_y = None, None
        self.old_pixmap = self.pixmap().copy()
        self.undoList = []
        self.redoList = []
        self.shape_canvas_list = [self.pixmap()]
        self.shape = Shapes.LINE

    def setup(self):
        self.setStyleSheet("background-color: lightgreen")
        self.setGeometry(0, 0, self.parent().width(), self.parent().height())
        canvas = QtGui.QPixmap(self.width(), self.height())
        canvas.fill(QColor('#ffffff'))
        self.setPixmap(canvas)
        self.pen = MyPen()

    def draw_ellipse(self, e):
        painter = QtGui.QPainter(self.pixmap())
        painter.setRenderHint(QtGui.QPainter.Antialiasing, True)
        painter.setPen(self.pen)
        painter.drawEllipse(self.last_x, self.last_y, e.x()-self.last_x, e.y()+TOOLBAR_HEIGHT-self.last_y)
        painter.end()
        self.update()

    def draw_circle(self, e):
        painter = QtGui.QPainter(self.pixmap())
        painter.setRenderHint(QtGui.QPainter.Antialiasing, True)
        painter.setPen(self.pen)
        painter.drawEllipse(self.last_x, self.last_y, e.x()-self.last_x, e.x()-self.last_x)
        painter.end()
        self.update()

    def draw_rectangle(self, e):
        painter = QtGui.QPainter(self.pixmap())
        painter.setRenderHint(QtGui.QPainter.Antialiasing, True)
        painter.setPen(self.pen)
        painter.drawRect(self.last_x, self.last_y, e.x()-self.last_x, e.y()+TOOLBAR_HEIGHT-self.last_y)
        painter.end()
        self.update()

    def draw_square(self, e):
        painter = QtGui.QPainter(self.pixmap())
        painter.setRenderHint(QtGui.QPainter.Antialiasing, True)
        painter.setPen(self.pen)
        painter.drawRect(self.last_x, self.last_y, e.x()-self.last_x, e.x()-self.last_x)
        painter.end()
        self.update()

    def draw_triangle(self, e):
        painter = QtGui.QPainter(self.pixmap())
        painter.setRenderHint(QtGui.QPainter.Antialiasing, True)
        painter.setPen(self.pen)
        painter.drawRect(self.last_x, self.last_y, e.x()-self.last_x, e.x()-self.last_x)
        painter.end()
        self.update()

    def draw_star(self, e):
        painter = QtGui.QPainter(self.pixmap())
        painter.setRenderHint(QtGui.QPainter.Antialiasing, True)
        painter.setPen(self.pen)
        painter.drawRect(self.last_x, self.last_y, e.x()-self.last_x, e.x()-self.last_x)
        painter.end()
        self.update()

    def mouseMoveEvent(self, e):
        # switch on shape
        # if shape == Shapes.LINE:
        #     self.label.line = True
        #     self.label.ellipse = False
        # elif shape == Shapes.CIRCLE:
        #     self.label.line = False
        #     self.label.ellipse = True
        # elif shape == Shapes.ELLIPSE:
        #     self.label.line = False
        #     self.label.ellipse = True
        # elif shape == Shapes.SQUARE:
        #     self.label.line = False
        #     self.label.ellipse = True
        # elif shape == Shapes.RECTANGLE:
        #     self.label.line = False
        #     self.label.ellipse = True
        # elif shape == Shapes.TRIANGLE:
        #     self.label.line = False
        #     self.label.ellipse = True
        # elif shape == Shapes.STAR:
        #     self.label.line = False
        #     self.label.ellipse = True
        # else:
        #     self.label.line = True
        if self.last_x is None:  # First event.
            self.last_x = e.x()
            self.last_y = e.y()+TOOLBAR_HEIGHT
            return

        if self.shape == Shapes.LINE:
            painter = QtGui.QPainter(self.pixmap())
            painter.setRenderHint(QtGui.QPainter.Antialiasing, True)
            painter.setPen(self.pen)
            painter.drawLine(self.last_x, self.last_y, e.x(), e.y() + TOOLBAR_HEIGHT)

            self.last_x = e.x()
            self.last_y = e.y() + TOOLBAR_HEIGHT

            painter.end()
            self.update()

        else:
            self.setPixmap(self.shape_canvas_list.pop())
            self.shape_canvas_list.append(self.pixmap().copy())
            if self.shape == Shapes.ELLIPSE:
                self.draw_ellipse(e)

            elif self.shape == Shapes.CIRCLE:
                self.draw_circle(e)

            elif self.shape == Shapes.SQUARE:
                self.draw_square(e)

            elif self.shape == Shapes.RECTANGLE:
                self.draw_rectangle(e)

            elif self.shape == Shapes.TRIANGLE:
                self.draw_triangle(e)

            elif self.shape == Shapes.STAR:
                self.draw_star(e)



    def mouseReleaseEvent(self, e):
        self.shape_canvas_list = [self.pixmap()]
        self.undoList.append(self.old_pixmap)
        self.old_pixmap = self.pixmap().copy()
        self.redoList.clear()
        self.last_x = None
        self.last_y = None

    def undo(self):
        if self.undoList:
            if len(self.undoList) > 0:
                self.redoList.append(self.old_pixmap)
                undo_canvas = self.undoList.pop()
                self.old_pixmap = undo_canvas
                print(f'UNDO TEST  undo_canvas {undo_canvas} lenght of canvas list is:{len(self.undoList)}')
                self.setPixmap(undo_canvas)
                self.update()

                self.shape_canvas_list = [self.pixmap()]

    def redo(self):
        if self.redoList:
            if len(self.redoList) > 0:
                self.undoList.append(self.old_pixmap)
                redo_canvas = self.redoList.pop()
                self.old_pixmap = redo_canvas
                print(f'REDO TEST  redo_canvas {redo_canvas} lenght of canvas list is:{len(self.redoList)}')
                self.setPixmap(redo_canvas)
                self.update()

                self.shape_canvas_list = [self.pixmap()]


class MyPen(QPen):
    def __init__(self):
        super().__init__()
        self.setup()

    def setup(self):
        self.setWidth(2)
