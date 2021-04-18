from PyQt5 import QtWidgets
import sys

from editor import WindowUi


def setup_window():
    app = QtWidgets.QApplication(sys.argv)
    main_window = QtWidgets.QMainWindow()
    window_ui = WindowUi()
    window_ui.setupUi(main_window)
    main_window.show()
    return app


if __name__ == "__main__":
    app = setup_window()
    sys.exit(app.exec_())
