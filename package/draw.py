from PyQt5 import QtGui
from PyQt5.QtGui import QColor, QPen
from PyQt5.QtWidgets import QLabel, QMainWindow

TOOLBAR_HEIGHT = 21


class MyLabel(QLabel):
    def __init__(self, parent: QMainWindow):
        super().__init__(parent)
        self.setup()
        self.last_x, self.last_y = None, None
        self.old_pixmap = self.pixmap().copy()
        self.canvasList = []
        self.redoList = []

    def setup(self):
        self.setStyleSheet("background-color: white")
        self.setGeometry(0, 0, self.parent().width(), self.parent().height())
        canvas = QtGui.QPixmap(self.width(), self.height())
        canvas.fill(QColor('#ffffff'))
        self.setPixmap(canvas)
        self.pen = MyPen()


    def mouseMoveEvent(self, e):
        if self.last_x is None:  # First event.
            self.last_x = e.x()
            self.last_y = e.y()+TOOLBAR_HEIGHT
            return
        painter = QtGui.QPainter(self.pixmap())
        painter.setRenderHint(QtGui.QPainter.Antialiasing, True)
        painter.setPen(self.pen)
        painter.drawLine(self.last_x, self.last_y, e.x(), e.y()+TOOLBAR_HEIGHT)
        painter.end()
        self.update()

        self.last_x = e.x()
        self.last_y = e.y()+TOOLBAR_HEIGHT

    def mouseReleaseEvent(self, e):
        self.canvasList.append(self.old_pixmap)
        self.old_pixmap = self.pixmap().copy()
        self.redoList.clear()
        self.last_x = None
        self.last_y = None

    def undo(self):
        if self.canvasList:
            if len(self.canvasList) > 0:
                self.redoList.append(self.old_pixmap)
                it = self.canvasList.pop()
                self.old_pixmap = it
                print(f'UNDO TEST  it {it} lenght of canvas list is:{len(self.canvasList)}')
                self.setPixmap(it)
                self.update()

    def redo(self):
        if self.redoList:
            if len(self.redoList) > 0:
                self.canvasList.append(self.old_pixmap)
                it = self.redoList.pop()
                self.old_pixmap = it
                print(f'REDO TEST  it {it} lenght of canvas list is:{len(self.redoList)}')
                self.setPixmap(it)
                self.update()

class MyPen(QPen):
    def __init__(self):
        super().__init__()
        self.setup()

    def setup(self):
        self.setWidth(2)
