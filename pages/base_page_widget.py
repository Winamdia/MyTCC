from PySide6.QtWidgets import QMainWindow
from pages.base_page import Ui_BasePage
from pages.connect_page_widget import ConnectPage
from pages.home_page_widget import HomePage
from pages.locomotieven_page_widget import LocomotievenPage

class BasePage(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_BasePage()
        self.ui.setupUi(self)

        from PySide6.QtWidgets import QVBoxLayout
        self.ui.contentArea.setLayout(QVBoxLayout())

        self.ui.btnHome.clicked.connect(self.on_home_clicked)
        self.ui.btnLocomotieven.clicked.connect(self.on_locomotieven_clicked)
        self.ui.btnConnectiviteit.clicked.connect(self.on_connect_clicked)

        self.showMaximized()


    def on_home_clicked(self):

        # Eerst contentArea leegmaken
        layout = self.ui.contentArea.layout()
        while layout.count():
            item = layout.takeAt(0)
            widget = item.widget()
            if widget:
                widget.deleteLater()

        self.ui.contentArea.layout().addWidget(HomePage())

    def on_locomotieven_clicked(self):

        # Eerst contentArea leegmaken
        layout = self.ui.contentArea.layout()
        while layout.count():
            item = layout.takeAt(0)
            widget = item.widget()
            if widget:
                widget.deleteLater()

        self.ui.contentArea.layout().addWidget(LocomotievenPage())

    def on_connect_clicked(self):
        layout = self.ui.contentArea.layout()
        while layout.count():
            item = layout.takeAt(0)
            widget = item.widget()
            if widget:
                widget.deleteLater()

        self.ui.contentArea.layout().addWidget(ConnectPage())