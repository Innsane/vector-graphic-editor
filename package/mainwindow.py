from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtWidgets import QMainWindow

from package.draw import MyLabel
from package.pensizewidget import PenSizeWidget

WIDTH = 1000
HEIGHT = 700


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setup_ui()
        self.add_widgets()

    def setup_ui(self):
        # setup main window
        self.setObjectName("MainWindow")
        self.setWindowIcon(QtGui.QIcon('icons/logo.png'))
        self.resize(WIDTH, HEIGHT)
        self.setMouseTracking(True)

        # setup central widget as workspace
        self.label = MyLabel(self)
        self.setCentralWidget(self.label)

        # setup menu bar
        self.menubar = QtWidgets.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1000, 21))
        self.menubar.setDefaultUp(False)
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuSize = QtWidgets.QMenu(self.menubar)
        self.menuSize.setObjectName("menuSize")
        self.menuColor = QtWidgets.QMenu(self.menubar)
        self.menuColor.setObjectName("menuColor")
        self.menuShape = QtWidgets.QMenu(self.menubar)
        self.menuShape.setObjectName("menuShape")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuTools = QtWidgets.QMenu(self.menubar)
        self.menuTools.setObjectName("menuTools")
        self.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)
        self.actionNew = QtWidgets.QAction(self)
        self.actionNew.setObjectName("actionNew")
        self.actionOpen = QtWidgets.QAction(self)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSave = QtWidgets.QAction(self)
        self.actionSave.setObjectName("actionSave")
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
        self.menuEdit.addAction(self.actionRedo)
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
        self.pen_size_widget.PenSizeScroll.valueChanged.connect(self.setPenSize)
        self.pen_size_widget.PenSizeScroll.valueChanged.connect(self.setLabelSize)

    def connect_signal_slot(self):
        self.menuSize.triggered.connect(self.showChangeSizeDialog)

    def showChangeSizeDialog(self):
        self.pen_size_widget.move(self.menuSize.x(), self.menuSize.y())
        self.pen_size_widget.show()

    def setPenSize(self, value):
        self.label.pen.setWidth(value)

    def setLabelSize(self, value):
        self.pen_size_widget.PenSizeLabel.setText(str(value))


