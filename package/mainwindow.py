from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtWidgets import QMainWindow, QColorDialog

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


        self.actionSave_as = QtWidgets.QAction(self)
        self.actionSave_as.setObjectName("actionSave_as")
        self.actionAdd_image = QtWidgets.QAction(self)
        self.actionAdd_image.setObjectName("actionAdd_image")


        # change size
        self.actionChange = QtWidgets.QAction(self)
        self.actionChange.setObjectName("action1")

        # change color
        self.actionBlack = QtWidgets.QAction(self)
        self.actionBlack.setObjectName("actionBlack")
        self.actionRed = QtWidgets.QAction(self)
        self.actionRed.setObjectName("actionRed")
        self.actionGreen = QtWidgets.QAction(self)
        self.actionGreen.setObjectName("actionGreen")
        self.actionYellow = QtWidgets.QAction(self)
        self.actionYellow.setObjectName("actionYellow")

        # edit drawing
        self.actionInfo = QtWidgets.QAction(self)
        self.actionInfo.setObjectName("actionInfo")
        self.actionUndo = QtWidgets.QAction(self)
        self.actionUndo.setObjectName("actionUndo")
        self.actionRedo = QtWidgets.QAction(self)
        self.actionRedo.setObjectName("actionRedo")
        self.actionCut = QtWidgets.QAction(self)
        self.actionCut.setObjectName("actionCut")
        self.actionCopy = QtWidgets.QAction(self)
        self.actionCopy.setObjectName("actionCopy")
        self.actionPaste = QtWidgets.QAction(self)
        self.actionPaste.setObjectName("actionPaste")

        # draw shape
        self.actionRectangle = QtWidgets.QAction(self)
        self.actionRectangle.setObjectName("actionRectangle")
        self.actionSquare = QtWidgets.QAction(self)
        self.actionSquare.setObjectName("actionSquare")
        self.actionTriangle = QtWidgets.QAction(self)
        self.actionTriangle.setObjectName("actionTriangle")
        self.actionStar = QtWidgets.QAction(self)
        self.actionStar.setObjectName("actionStar")
        self.actionCircle = QtWidgets.QAction(self)
        self.actionCircle.setObjectName("actionCircle")

        # tools
        self.actionBrush = QtWidgets.QAction(self)
        self.actionBrush.setObjectName("actionBrush")
        self.actionFill = QtWidgets.QAction(self)
        self.actionFill.setObjectName("actionFill")
        self.actionRuber = QtWidgets.QAction(self)
        self.actionRuber.setShortcutContext(QtCore.Qt.WindowShortcut)
        self.actionRuber.setObjectName("actionRuber")

        # setup menus
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionSave_as)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionAdd_image)
        self.menuSize.addAction(self.actionChange)
        self.menuColor.addAction(self.actionBlack)
        self.menuColor.addAction(self.actionRed)
        self.menuColor.addAction(self.actionGreen)
        self.menuColor.addAction(self.actionYellow)
        self.menuShape.addAction(self.actionCircle)
        self.menuShape.addAction(self.actionSquare)
        self.menuShape.addAction(self.actionRectangle)
        self.menuShape.addAction(self.actionTriangle)
        self.menuShape.addAction(self.actionStar)
        self.menuHelp.addAction(self.actionInfo)
        self.menuEdit.addAction(self.actionUndo)

        self.actionUndo.triggered.connect(self.undo_function)

        self.menuEdit.addAction(self.actionRedo)

        self.actionRedo.triggered.connect(self.redo_function)

        self.menuEdit.addSeparator()
        self.menuEdit.addAction(self.actionCut)
        self.menuEdit.addAction(self.actionCopy)
        self.menuEdit.addAction(self.actionPaste)
        self.menuTools.addAction(self.actionBrush)
        self.menuTools.addAction(self.actionFill)
        self.menuTools.addAction(self.actionRuber)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuTools.menuAction())
        self.menubar.addAction(self.menuSize.menuAction())
        self.menubar.addAction(self.menuColor.menuAction())
        self.menubar.addAction(self.menuShape.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.connect_signal_slot()

        self.retranslate_ui(self)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslate_ui(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Vectoring"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuSize.setTitle(_translate("MainWindow", "Size"))
        self.menuColor.setTitle(_translate("MainWindow", "Color"))
        self.menuShape.setTitle(_translate("MainWindow", "Shapes"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.menuTools.setTitle(_translate("MainWindow", "Tools"))
        self.actionNew.setText(_translate("MainWindow", "New"))
        self.actionNew.setShortcut(_translate("MainWindow", "Ctrl+N"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionOpen.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionSave.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.actionSave_as.setText(_translate("MainWindow", "Save as"))
        self.actionSave_as.setShortcut(_translate("MainWindow", "Ctrl+Shift+S"))
        self.actionRectangle.setText(_translate("MainWindow", "Rectangle"))
        self.actionSquare.setText(_translate("MainWindow", "Square"))
        self.actionTriangle.setText(_translate("MainWindow", "Triangle"))
        self.actionStar.setText(_translate("MainWindow", "Star"))

        self.actionChange.setText(_translate("MainWindow", "Change"))

        self.actionBlack.setText(_translate("MainWindow", "Black"))
        self.actionRed.setText(_translate("MainWindow", "Red"))
        self.actionGreen.setText(_translate("MainWindow", "Green"))
        self.actionYellow.setText(_translate("MainWindow", "Yellow"))
        self.actionInfo.setText(_translate("MainWindow", "Info"))
        self.actionUndo.setText(_translate("MainWindow", "Undo"))
        self.actionUndo.setShortcut(_translate("MainWindow", "Ctrl+Z"))
        self.actionRedo.setText(_translate("MainWindow", "Redo"))
        self.actionRedo.setShortcut(_translate("MainWindow", "Ctrl+Y"))
        self.actionCut.setText(_translate("MainWindow", "Cut"))
        self.actionCut.setShortcut(_translate("MainWindow", "Ctrl+X"))
        self.actionCopy.setText(_translate("MainWindow", "Copy"))
        self.actionCopy.setShortcut(_translate("MainWindow", "Ctrl+C"))
        self.actionPaste.setText(_translate("MainWindow", "Paste"))
        self.actionPaste.setShortcut(_translate("MainWindow", "Ctrl+V"))
        self.actionCircle.setText(_translate("MainWindow", "Circle"))
        self.actionBrush.setText(_translate("MainWindow", "Brush"))
        self.actionBrush.setShortcut(_translate("MainWindow", "Ctrl+B"))
        self.actionFill.setText(_translate("MainWindow", "Fill"))
        self.actionFill.setShortcut(_translate("MainWindow", "Ctrl+F"))
        self.actionRuber.setText(_translate("MainWindow", "Ruber"))
        self.actionRuber.setShortcut(_translate("MainWindow", "Ctrl+R"))
        self.actionAdd_image.setText(_translate("MainWindow", "Add image"))
        self.actionAdd_image.setShortcut(_translate("MainWindow", "Ctrl+I"))


    def add_widgets(self):
        self.pen_size_widget = PenSizeWidget(self)

        self.menuSize.triggered.connect(self.showChangeSizeDialog)
        self.menuColor.triggered.connect(self.showColorPicker)

        self.pen_size_widget.PenSizeScroll.valueChanged.connect(self.setPenSize)
        self.pen_size_widget.PenSizeScroll.valueChanged.connect(self.setLabelSize)

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
            self.label.canvasList.append(self.label.old_pixmap)  #redo and undo up
            self.label.old_pixmap = self.label.pixmap().copy()
            self.label.redoList.clear()

            file.close()


    def undo_function(self):
        self.label.undo()

    def redo_function(self):
        self.label.redo()
