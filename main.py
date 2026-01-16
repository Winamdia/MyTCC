from PySide6.QtWidgets import QApplication
from pages.base_page_widget import BasePage
import sys

app = QApplication(sys.argv)

window = BasePage()
window.show()

sys.exit(app.exec())