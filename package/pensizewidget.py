from PyQt5.QtWidgets import QMainWindow

from designer.ChangePenSizeWidget import Ui_ChangeSizeWidget
import package.draw as draw


class PenSizeWidget(QMainWindow, Ui_ChangeSizeWidget):
    def __init__(self, *args, obj=None, **kwargs):
        super(PenSizeWidget, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.custom_setup()

    def custom_setup(self):
        self.PenSizeScroll.setMinimum(1)
        self.PenSizeScroll.setMaximum(50)
        self.PenSizeScroll.setValue(draw.MyPen().width())
        self.PenSizeLabel.setText(str(draw.MyPen().width()))
