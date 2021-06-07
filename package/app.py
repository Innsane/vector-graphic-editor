import sys

from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication
from package.mainwindow import MainWindow


def run():
    app = QApplication(sys.argv)
    app.setWindowIcon(QtGui.QIcon('icons/logo.png'))
    main_window = MainWindow()
    main_window.show()
    app.exec_()
