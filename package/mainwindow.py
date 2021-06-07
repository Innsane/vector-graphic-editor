from enum import Enum
from re import match

from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtWidgets import QMainWindow, QColorDialog

from package.draw import MyLabel, Shapes
from package.pensizewidget import PenSizeWidget

from designer.MainWindow import Ui_MainWindow

WIDTH = 1000
HEIGHT = 700


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.customize_ui()
        self.connect_actions()

    def customize_ui(self):
        self.setObjectName("MainWindow")
        self.resize(WIDTH, HEIGHT)
        self.setMouseTracking(True)

        # add Label with Pixmap as workspace to draw on
        self.label = MyLabel(self)
        self.setCentralWidget(self.label)

        self.pen_size_widget = PenSizeWidget(self)

        self.color_picker = QColorDialog(self)

    def connect_actions(self):
        self.actionOpen.triggered.connect(self.file_open)
        self.actionSave.triggered.connect(self.file_save)
        self.menuSize.triggered.connect(self.show_change_size_dialog)
        self.menuColor.triggered.connect(self.show_color_picker)
        self.pen_size_widget.PenSizeScroll.valueChanged.connect(self.set_pen_size)
        self.pen_size_widget.PenSizeScroll.valueChanged.connect(self.set_label_size)
        self.actionUndo.triggered.connect(self.undo_function)
        self.actionRedo.triggered.connect(self.redo_function)
        self.actionLine.triggered.connect(lambda: self.change_shape(Shapes.LINE))
        self.actionCircle.triggered.connect(lambda: self.change_shape(Shapes.CIRCLE))
        self.actionEllipse.triggered.connect(lambda: self.change_shape(Shapes.ELLIPSE))
        self.actionSquare.triggered.connect(lambda: self.change_shape(Shapes.SQUARE))
        self.actionRectangle.triggered.connect(lambda: self.change_shape(Shapes.RECTANGLE))
        self.actionTriangle.triggered.connect(lambda: self.change_shape(Shapes.TRIANGLE))
        self.actionStar.triggered.connect(lambda: self.change_shape(Shapes.STAR))

    def show_color_picker(self):
        color = self.color_picker.getColor()
        if color.isValid():
            self.set_pen_color(color)

    def set_pen_color(self, color):
        self.label.pen.setColor(color)

    def show_change_size_dialog(self):
        self.pen_size_widget.move(self.menuSize.x(), self.menuSize.y())
        self.pen_size_widget.show()

    def set_pen_size(self, value):
        self.label.pen.setWidth(value)

    def set_label_size(self, value):
        self.pen_size_widget.PenSizeLabel.setText(str(value))

    def file_save(self):
        filepath = QtWidgets.QFileDialog.getSaveFileName(self, 'Save File', '', '*.jpg')
        if filepath[0] == '':
            return False
        else:
            file = open(filepath[0], 'w')
            self.label.pixmap().save(filepath[0], "JPG")
            file.close()

    def file_open(self):
        filepath = QtWidgets.QFileDialog.getOpenFileName(self, 'Open File')
        if filepath[0] == '':
            return False
        else:
            file = open(filepath[0], 'r')
            pixmap = QtGui.QPixmap(filepath[0])
            self.label.setPixmap(pixmap)
            self.resize(pixmap.size())
            self.adjustSize()
            self.label.undoList.append(self.label.old_pixmap)  #redo and undo up
            self.label.old_pixmap = self.label.pixmap().copy()
            self.label.redoList.clear()
            file.close()

    def undo_function(self):
        self.label.undo()

    def redo_function(self):
        self.label.redo()

    def change_shape(self, shape):
        self.label.shape = shape

