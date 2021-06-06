from PyQt5 import QtGui, QtCore
from PyQt5.QtGui import QColor, QPen, QMouseEvent
from PyQt5.QtWidgets import QLabel, QMainWindow

TOOLBAR_HEIGHT = 21


class MyLabel(QLabel):
    def __init__(self, parent: QMainWindow):
        super().__init__(parent)
        self.setup()
        self.last_x, self.last_y = None, None
        self.painter = QtGui.QPainter(self.pixmap())
        self.pen = MyPen()
        self._do_erase = False
        self._clear_size = 20

    def setup(self):
        self.setStyleSheet("background-color: white")
        self.setGeometry(0, 0, self.parent().width(), self.parent().height())
        canvas = QtGui.QPixmap(self.width(), self.height())
        canvas.fill(QColor('#ffffff'))
        # canvas.fill(QtCore.Qt.transparent)
        self.setPixmap(canvas)

    def mouseMoveEvent(self, e):
        if self.last_x is None:  # First event.
            self.last_x = e.x()
            self.last_y = e.y() + TOOLBAR_HEIGHT
            return
        if self._do_erase:
            self.erase(e)
        else:
            self.draw(e)

        self.painter.end()
        self.update()
        self.last_x = e.x()
        self.last_y = e.y() + TOOLBAR_HEIGHT

    def mouseReleaseEvent(self, e):
        self.last_x = None
        self.last_y = None

    def draw(self, event: QMouseEvent):
        self.painter = QtGui.QPainter(self.pixmap())
        self.painter.setRenderHint(QtGui.QPainter.Antialiasing, True)
        self.painter.setPen(self.pen)
        self.painter.drawLine(self.last_x, self.last_y, event.x(), event.y() + TOOLBAR_HEIGHT)

    def erase(self, event: QMouseEvent):
        self.brushSize = 2
        self._clear_size = 20
        self.brushColor = QtGui.QColor(QtCore.Qt.white)

        self.painter = QtGui.QPainter(self.pixmap())
        self.painter.setPen(QtGui.QPen(self.brushColor, self.brushSize, QtCore.Qt.SolidLine, QtCore.Qt.RoundCap,
                                       QtCore.Qt.RoundJoin))
        r = QtCore.QRect(QtCore.QPoint(), QtCore.QSize(20, 20))
        r.moveCenter(event.pos())
        print(f'center of rect: {r.center()}')
        print(f'width of rect: {r.width()}')
        print(f'height of rect: {r.height()}')
        # self.painter = QtGui.QPainter(self.pixmap())
        self.painter.save()
        # self.pen.setColor(QColor('#ffffff'))
        # self.painter.setPen(self.pen)
        # self.painter.setRenderHint(QtGui.QPainter.Antialiasing, True)
        self.painter.setCompositionMode(QtGui.QPainter.CompositionMode_Clear)
        self.painter.eraseRect(r)
        # self.painter.restore()


class MyPen(QPen):
    def __init__(self):
        super().__init__()
        self.setup()

    def setup(self):
        self.setWidth(2)
