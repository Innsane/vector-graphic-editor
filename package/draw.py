from PyQt5 import QtGui, Qt
from PyQt5.QtGui import QColor, QPen
from PyQt5.QtWidgets import QLabel, QMainWindow

TOOLBAR_HEIGHT = 21


class MyLabel(QLabel):
    def __init__(self, parent: QMainWindow):
        super().__init__(parent)
        self.setup()
        self.last_x, self.last_y = None, None
        self.old_pixmap = self.pixmap().copy()
        self.undoList = []
        self.redoList = []
        self.ellipse = True



    def setup(self):
        self.setStyleSheet("background-color: lightgreen")
        self.setGeometry(0, 0, self.parent().width(), self.parent().height())
        canvas = QtGui.QPixmap(self.width(), self.height())
        canvas.fill(QColor('#ffffff'))
        self.setPixmap(canvas)
        self.pen = MyPen()
        self.ellipse_canvas_list = [self.pixmap()]

    def draw_ellipse(self, e):
        self.setPixmap(self.ellipse_canvas_list.pop())
        self.ellipse_canvas_list.append(self.pixmap().copy())
        print(f"last x: {self.last_x}")
        print(f"last y: {self.last_y}")
        print(f"e.x: {e.x()}")
        print(f"e.y: {e.y()}")
        print(len(self.ellipse_canvas_list))
        painter = QtGui.QPainter(self.pixmap())
        painter.setRenderHint(QtGui.QPainter.Antialiasing, True)
        painter.setPen(self.pen)
        painter.drawEllipse(self.last_x, self.last_y, e.x()-self.last_x, e.y()+TOOLBAR_HEIGHT-self.last_y)
        painter.end()
        self.update()

    def mouseMoveEvent(self, e):
        if self.last_x is None:  # First event.
            self.last_x = e.x()
            self.last_y = e.y()+TOOLBAR_HEIGHT
            return
        if self.ellipse:
            self.draw_ellipse(e)

        else:
            painter = QtGui.QPainter(self.pixmap())
            painter.setRenderHint(QtGui.QPainter.Antialiasing, True)
            painter.setPen(self.pen)
            painter.drawLine(self.last_x, self.last_y, e.x(), e.y()+TOOLBAR_HEIGHT)
            painter.end()
            self.update()

            self.last_x = e.x()
            self.last_y = e.y()+TOOLBAR_HEIGHT

    def mouseReleaseEvent(self, e):
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

    def redo(self):
        if self.redoList:
            if len(self.redoList) > 0:
                self.undoList.append(self.old_pixmap)
                redo_canvas = self.redoList.pop()
                self.old_pixmap = redo_canvas
                print(f'REDO TEST  redo_canvas {redo_canvas} lenght of canvas list is:{len(self.redoList)}')
                self.setPixmap(redo_canvas)
                self.update()


class MyPen(QPen):
    def __init__(self):
        super().__init__()
        self.setup()

    def setup(self):
        self.setWidth(2)
