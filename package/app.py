import sys

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow

from package.mainwindow import WindowUi


def setup_window():
    main_window = QMainWindow()
    window_ui = WindowUi()
    window_ui.setup_ui(main_window)
    main_window.show()
    return main_window


def run():
    app = QApplication(sys.argv)
    main = setup_window()
    app.exec_()
