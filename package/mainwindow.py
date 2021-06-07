from enum import Enum
from re import match

from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtWidgets import QMainWindow, QColorDialog

from package.draw import MyLabel
from package.pensizewidget import PenSizeWidget

from designer.MainWindow import Ui_MainWindow

WIDTH = 1000
HEIGHT = 700


class Shapes(Enum):
    LINE = 'line'
    CIRCLE = 'circle'
    ELLIPSE = 'ellipse'
    SQUARE = 'square'
    RECTANGLE = 'rectangle'
    TRIANGLE = 'triangle'
    STAR = 'star'


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
        self.menuSize.triggered.connect(self.showChangeSizeDialog)
        self.menuColor.triggered.connect(self.showColorPicker)
        self.pen_size_widget.PenSizeScroll.valueChanged.connect(self.setPenSize)
        self.pen_size_widget.PenSizeScroll.valueChanged.connect(self.setLabelSize)
        self.actionUndo.triggered.connect(self.undo_function)
        self.actionRedo.triggered.connect(self.redo_function)
        self.actionLine.triggered.connect(lambda: self.change_shape('line'))
        self.actionCircle.triggered.connect(lambda: self.change_shape('circle'))
        self.actionCircle.triggered.connect(lambda: self.change_shape('ellipse'))
        self.actionCircle.triggered.connect(lambda: self.change_shape('square'))
        self.actionCircle.triggered.connect(lambda: self.change_shape('rectangle'))
        self.actionCircle.triggered.connect(lambda: self.change_shape('triangle'))
        self.actionCircle.triggered.connect(lambda: self.change_shape('star'))


    def showColorPicker(self):
        color = self.color_picker.getColor()
        if color.isValid():
            self.setPenColor(color)

    def setPenColor(self, color):
        self.label.pen.setColor(color)

    def showChangeSizeDialog(self):
        self.pen_size_widget.move(self.menuSize.x(), self.menuSize.y())
        self.pen_size_widget.show()

    def setPenSize(self, value):
        self.label.pen.setWidth(value)

    def setLabelSize(self, value):
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
        if shape == Shapes.LINE:
            self.label.line = True
            self.label.ellipse = False
        elif shape == Shapes.CIRCLE:
            self.label.line = False
            self.label.ellipse = True
        elif shape == Shapes.ELLIPSE:
            self.label.line = False
            self.label.ellipse = True
        elif shape == Shapes.SQUARE:
            self.label.line = False
            self.label.ellipse = True
        elif shape == Shapes.RECTANGLE:
            self.label.line = False
            self.label.ellipse = True
        elif shape == Shapes.TRIANGLE:
            self.label.line = False
            self.label.ellipse = True
        elif shape == Shapes.STAR:
            self.label.line = False
            self.label.ellipse = True
        else:
            self.label.line = True

