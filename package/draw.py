from PyQt5 import QtGui
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QLabel

from package.mainwindow import MainWindow


class MyLabel(QLabel):
    def __init__(self, parent: MainWindow):
        super().__init__(parent)
        self.setup()
        self.last_x, self.last_y = None, None

    def setup(self):
        self.setGeometry(0, 0, self.parent().width(), self.parent().height())
        canvas = QtGui.QPixmap(self.width(), self.height())
        canvas.fill(QColor('#ffffff'))
        self.setPixmap(canvas)
        self.setStyleSheet("background-color: lightgreen")

    def drawing(self):
        painter = QtGui.QPainter(self.pixmap())
        color = QColor('#001AFF')
        painter.setPen(color)
        painter.drawLine(10, 10, 300, 200)
        painter.drawRect(300, 60, 300, 200)
        painter.end()
        self.update()

    def mouseMoveEvent(self, e):
        if self.last_x is None:  # First event.
            self.last_x = e.x()
            self.last_y = e.y()
            return

        painter = QtGui.QPainter(self.pixmap())
        painter.drawLine(self.last_x, self.last_y, e.x(), e.y())
        painter.end()
        self.update()

        self.last_x = e.x()
        self.last_y = e.y()

    def mouseReleaseEvent(self, e):
        self.last_x = None
        self.last_y = None
