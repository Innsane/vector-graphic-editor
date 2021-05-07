from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtWidgets import QMainWindow

from package.draw import MyLabel
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
        self.setWindowIcon(QtGui.QIcon('icons/logo.png'))
        self.resize(WIDTH, HEIGHT)
        self.setMouseTracking(True)

        # add Label with Pixmap as workspace to draw on
        self.label = MyLabel(self)
        self.setCentralWidget(self.label)

        self.pen_size_widget = PenSizeWidget(self)

    def connect_actions(self):
        self.actionOpen.triggered.connect(self.file_open)
        self.actionSave.triggered.connect(self.file_save)
        self.menuSize.triggered.connect(self.showChangeSizeDialog)
        self.pen_size_widget.PenSizeScroll.valueChanged.connect(self.setPenSize)
        self.pen_size_widget.PenSizeScroll.valueChanged.connect(self.setLabelSize)

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
            file.close()
