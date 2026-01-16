from PySide6.QtWidgets import QWidget
from pages.connect_page import Ui_ConnectPage

class ConnectPage(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_ConnectPage()
        self.ui.setupUi(self)