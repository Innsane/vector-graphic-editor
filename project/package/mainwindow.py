from PyQt5 import QtCore, QtWidgets, QtGui


class WindowUi(object):
    def setup_ui(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowIcon(QtGui.QIcon('icons/logo.png'))
        MainWindow.resize(1000, 700)
        MainWindow.setMinimumSize(QtCore.QSize(300, 200))
        MainWindow.setMouseTracking(False)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(MainWindow)
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
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionNew = QtWidgets.QAction(MainWindow)
        self.actionNew.setObjectName("actionNew")
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionSave_as = QtWidgets.QAction(MainWindow)
        self.actionSave_as.setObjectName("actionSave_as")
        self.actionRectangle = QtWidgets.QAction(MainWindow)
        self.actionRectangle.setObjectName("actionRectangle")
        self.actionSquare = QtWidgets.QAction(MainWindow)
        self.actionSquare.setObjectName("actionSquare")
        self.actionTriangle = QtWidgets.QAction(MainWindow)
        self.actionTriangle.setObjectName("actionTriangle")
        self.actionStar = QtWidgets.QAction(MainWindow)
        self.actionStar.setObjectName("actionStar")
        self.action1 = QtWidgets.QAction(MainWindow)
        self.action1.setObjectName("action1")
        self.action2 = QtWidgets.QAction(MainWindow)
        self.action2.setObjectName("action2")
        self.action4 = QtWidgets.QAction(MainWindow)
        self.action4.setObjectName("action4")
        self.action8 = QtWidgets.QAction(MainWindow)
        self.action8.setObjectName("action8")
        self.action16 = QtWidgets.QAction(MainWindow)
        self.action16.setObjectName("action16")
        self.action32 = QtWidgets.QAction(MainWindow)
        self.action32.setObjectName("action32")
        self.actionBlack = QtWidgets.QAction(MainWindow)
        self.actionBlack.setObjectName("actionBlack")
        self.actionRed = QtWidgets.QAction(MainWindow)
        self.actionRed.setObjectName("actionRed")
        self.actionGreen = QtWidgets.QAction(MainWindow)
        self.actionGreen.setObjectName("actionGreen")
        self.actionYellow = QtWidgets.QAction(MainWindow)
        self.actionYellow.setObjectName("actionYellow")
        self.actionInfo = QtWidgets.QAction(MainWindow)
        self.actionInfo.setObjectName("actionInfo")
        self.actionUndo = QtWidgets.QAction(MainWindow)
        self.actionUndo.setObjectName("actionUndo")
        self.actionRedo = QtWidgets.QAction(MainWindow)
        self.actionRedo.setObjectName("actionRedo")
        self.actionCut = QtWidgets.QAction(MainWindow)
        self.actionCut.setObjectName("actionCut")
        self.actionCopy = QtWidgets.QAction(MainWindow)
        self.actionCopy.setObjectName("actionCopy")
        self.actionPaste = QtWidgets.QAction(MainWindow)
        self.actionPaste.setObjectName("actionPaste")
        self.actionCircle = QtWidgets.QAction(MainWindow)
        self.actionCircle.setObjectName("actionCircle")
        self.actionBrush = QtWidgets.QAction(MainWindow)
        self.actionBrush.setObjectName("actionBrush")
        self.actionFill = QtWidgets.QAction(MainWindow)
        self.actionFill.setObjectName("actionFill")
        self.actionRuber = QtWidgets.QAction(MainWindow)
        self.actionRuber.setShortcutContext(QtCore.Qt.WindowShortcut)
        self.actionRuber.setObjectName("actionRuber")
        self.actionAdd_image = QtWidgets.QAction(MainWindow)
        self.actionAdd_image.setObjectName("actionAdd_image")
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionSave_as)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionAdd_image)
        self.menuSize.addAction(self.action1)
        self.menuSize.addAction(self.action2)
        self.menuSize.addAction(self.action4)
        self.menuSize.addAction(self.action8)
        self.menuSize.addAction(self.action16)
        self.menuSize.addAction(self.action32)
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



        self.retranslate_ui(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

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
        self.action1.setText(_translate("MainWindow", "1"))
        self.action2.setText(_translate("MainWindow", "2"))
        self.action4.setText(_translate("MainWindow", "4"))
        self.action8.setText(_translate("MainWindow", "8"))
        self.action16.setText(_translate("MainWindow", "16"))
        self.action32.setText(_translate("MainWindow", "32"))
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
        self.actionAdd_image.setText(_translate("MainWindow", "Add icons"))
        self.actionAdd_image.setShortcut(_translate("MainWindow", "Ctrl+I"))