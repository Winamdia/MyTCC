from PySide6.QtWidgets import QWidget
from pages.home_page import Ui_HomePage   # dit is jouw gegenereerde .ui-bestand

class HomePage(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_HomePage()
        self.ui.setupUi(self)