from PyQt5 import QtGui, Qt
from PyQt5.QtGui import QColor, QPen
from PyQt5.QtWidgets import QLabel, QMainWindow


class MyLabel(QLabel):
    def __init__(self, parent: QMainWindow):
        super().__init__(parent)
        self.setup()
        self.last_x, self.last_y = None, None

    def setup(self):
        self.setStyleSheet("background-color: lightgreen")
        self.setGeometry(0, 0, self.parent().width(), self.parent().height())
        canvas = QtGui.QPixmap(self.width(), self.height())
        canvas.fill(QColor('#ffffff'))
        self.setPixmap(canvas)
        self.pen = MyPen()


    def mouseMoveEvent(self, e):
        if self.last_x is None:  # First event.
            self.last_x = e.x()
            self.last_y = e.y()
            return

        painter = QtGui.QPainter(self.pixmap())
        painter.setPen(self.pen)
        painter.drawLine(self.last_x, self.last_y, e.x(), e.y())
        painter.end()
        self.update()

        self.last_x = e.x()
        self.last_y = e.y()

    def mouseReleaseEvent(self, e):
        self.last_x = None
        self.last_y = None


class MyPen(QPen):
    def __init__(self):
        super().__init__()
        self.setup()

    def setup(self):
        self.setWidth(3)
