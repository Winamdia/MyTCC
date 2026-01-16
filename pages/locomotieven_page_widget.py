from PySide6.QtWidgets import QWidget
from pages.locomotieven_page import Ui_Form

class LocomotievenPage(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)