from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QMainWindow,
    QMenuBar, QSizePolicy, QSpacerItem, QStatusBar,
    QToolButton, QVBoxLayout, QWidget)
from pages import resources_rc

class Ui_BasePage(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1250, 828)
        MainWindow.setStyleSheet(u"QMainWindow {\n"
"    background-color: #b8e6a1;\n"
"}\n"
"\n"
"#sidebarFrame {\n"
"    background-color: #749c60;\n"
"}\n"
"\n"
"#contentArea {\n"
"    background-color: white;\n"
"}\n"
"\n"
"QPushButton, QToolButton {\n"
"    padding: 6px 12px;\n"
"    font-weight: bold;\n"
"    border: none;\n"
"    background-color: #b8e6a1;\n"
"    color: black;\n"
"    text-align: left;\n"
"}\n"
"\n"
"QPushButton:hover, QToolButton:hover {\n"
"    background-color: #c9f2b5;\n"
"}\n"
"\n"
"QPushButton:pressed, QToolButton:pressed {\n"
"    background-color: #a5d48f;\n"
"}\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.mainContainer = QWidget(self.centralwidget)
        self.mainContainer.setObjectName(u"mainContainer")
        self.horizontalLayout = QHBoxLayout(self.mainContainer)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.sidebarFrame = QFrame(self.mainContainer)
        self.sidebarFrame.setObjectName(u"sidebarFrame")
        self.sidebarFrame.setMinimumSize(QSize(180, 0))
        self.sidebarFrame.setMaximumSize(QSize(200, 16777215))
        self.sidebarFrame.setStyleSheet(u"")
        self.sidebarFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.sidebarFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.sidebarFrame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.btnHome = QToolButton(self.sidebarFrame)
        self.btnHome.setObjectName(u"btnHome")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnHome.sizePolicy().hasHeightForWidth())
        self.btnHome.setSizePolicy(sizePolicy)
        self.btnHome.setMinimumSize(QSize(0, 40))
        self.btnHome.setMaximumSize(QSize(16777215, 40))
        self.btnHome.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        icon = QIcon()
        icon.addFile(u":/icons/Home.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnHome.setIcon(icon)
        self.btnHome.setIconSize(QSize(32, 32))
        self.btnHome.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextBesideIcon)

        self.verticalLayout_2.addWidget(self.btnHome)

        self.btnLocomotieven = QToolButton(self.sidebarFrame)
        self.btnLocomotieven.setObjectName(u"btnLocomotieven")
        sizePolicy.setHeightForWidth(self.btnLocomotieven.sizePolicy().hasHeightForWidth())
        self.btnLocomotieven.setSizePolicy(sizePolicy)
        self.btnLocomotieven.setMinimumSize(QSize(0, 40))
        self.btnLocomotieven.setMaximumSize(QSize(16777215, 40))
        self.btnLocomotieven.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        icon1 = QIcon()
        icon1.addFile(u":/icons/Locomotief.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnLocomotieven.setIcon(icon1)
        self.btnLocomotieven.setIconSize(QSize(32, 32))
        self.btnLocomotieven.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextBesideIcon)

        self.verticalLayout_2.addWidget(self.btnLocomotieven)

        self.btnWissels = QToolButton(self.sidebarFrame)
        self.btnWissels.setObjectName(u"btnWissels")
        sizePolicy.setHeightForWidth(self.btnWissels.sizePolicy().hasHeightForWidth())
        self.btnWissels.setSizePolicy(sizePolicy)
        self.btnWissels.setMinimumSize(QSize(0, 40))
        self.btnWissels.setMaximumSize(QSize(16777215, 40))
        self.btnWissels.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        icon2 = QIcon()
        icon2.addFile(u":/icons/Wissel.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnWissels.setIcon(icon2)
        self.btnWissels.setIconSize(QSize(32, 32))
        self.btnWissels.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextBesideIcon)

        self.verticalLayout_2.addWidget(self.btnWissels)

        self.btnSeinen = QToolButton(self.sidebarFrame)
        self.btnSeinen.setObjectName(u"btnSeinen")
        sizePolicy.setHeightForWidth(self.btnSeinen.sizePolicy().hasHeightForWidth())
        self.btnSeinen.setSizePolicy(sizePolicy)
        self.btnSeinen.setMinimumSize(QSize(0, 40))
        self.btnSeinen.setMaximumSize(QSize(16777215, 40))
        self.btnSeinen.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        icon3 = QIcon()
        icon3.addFile(u":/icons/Sein.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnSeinen.setIcon(icon3)
        self.btnSeinen.setIconSize(QSize(32, 32))
        self.btnSeinen.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextBesideIcon)

        self.verticalLayout_2.addWidget(self.btnSeinen)

        self.btnStraatlicht = QToolButton(self.sidebarFrame)
        self.btnStraatlicht.setObjectName(u"btnStraatlicht")
        sizePolicy.setHeightForWidth(self.btnStraatlicht.sizePolicy().hasHeightForWidth())
        self.btnStraatlicht.setSizePolicy(sizePolicy)
        self.btnStraatlicht.setMinimumSize(QSize(0, 40))
        self.btnStraatlicht.setMaximumSize(QSize(16777215, 40))
        self.btnStraatlicht.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        icon4 = QIcon()
        icon4.addFile(u":/icons/Straatverlichting.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnStraatlicht.setIcon(icon4)
        self.btnStraatlicht.setIconSize(QSize(32, 28))
        self.btnStraatlicht.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextBesideIcon)

        self.verticalLayout_2.addWidget(self.btnStraatlicht)

        self.btnScenerylicht = QToolButton(self.sidebarFrame)
        self.btnScenerylicht.setObjectName(u"btnScenerylicht")
        sizePolicy.setHeightForWidth(self.btnScenerylicht.sizePolicy().hasHeightForWidth())
        self.btnScenerylicht.setSizePolicy(sizePolicy)
        self.btnScenerylicht.setMinimumSize(QSize(0, 40))
        self.btnScenerylicht.setMaximumSize(QSize(16777215, 40))
        self.btnScenerylicht.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        icon5 = QIcon()
        icon5.addFile(u":/icons/BinnenVerlichting.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnScenerylicht.setIcon(icon5)
        self.btnScenerylicht.setIconSize(QSize(32, 32))
        self.btnScenerylicht.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextBesideIcon)

        self.verticalLayout_2.addWidget(self.btnScenerylicht)

        self.btnConnectiviteit = QToolButton(self.sidebarFrame)
        self.btnConnectiviteit.setObjectName(u"btnConnectiviteit")
        sizePolicy.setHeightForWidth(self.btnConnectiviteit.sizePolicy().hasHeightForWidth())
        self.btnConnectiviteit.setSizePolicy(sizePolicy)
        self.btnConnectiviteit.setMinimumSize(QSize(0, 40))
        self.btnConnectiviteit.setMaximumSize(QSize(16777215, 40))
        self.btnConnectiviteit.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        icon6 = QIcon()
        icon6.addFile(u":/icons/Connect.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnConnectiviteit.setIcon(icon6)
        self.btnConnectiviteit.setIconSize(QSize(32, 32))
        self.btnConnectiviteit.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextBesideIcon)

        self.verticalLayout_2.addWidget(self.btnConnectiviteit)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.btnAfsluiten = QToolButton(self.sidebarFrame)
        self.btnAfsluiten.setObjectName(u"btnAfsluiten")
        sizePolicy.setHeightForWidth(self.btnAfsluiten.sizePolicy().hasHeightForWidth())
        self.btnAfsluiten.setSizePolicy(sizePolicy)
        self.btnAfsluiten.setMinimumSize(QSize(0, 40))
        self.btnAfsluiten.setMaximumSize(QSize(16777215, 40))
        self.btnAfsluiten.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        icon7 = QIcon()
        icon7.addFile(u":/icons/Uit.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnAfsluiten.setIcon(icon7)
        self.btnAfsluiten.setIconSize(QSize(32, 32))
        self.btnAfsluiten.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextBesideIcon)

        self.verticalLayout_2.addWidget(self.btnAfsluiten)


        self.horizontalLayout.addWidget(self.sidebarFrame)

        self.contentArea = QWidget(self.mainContainer)
        self.contentArea.setObjectName(u"contentArea")

        self.horizontalLayout.addWidget(self.contentArea)


        self.verticalLayout.addWidget(self.mainContainer)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1250, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        self.statusbar.setStyleSheet(u"background-color: #b8e6a1;\n"
"color: black;\n"
"font-weight: bold;\n"
"padding: 4px 12px;\n"
"")
        self.statusbar.setSizeGripEnabled(False)
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("BasePage", u"MainWindow", None))
        self.btnHome.setText(QCoreApplication.translate("BasePage", u"Home", None))
        self.btnLocomotieven.setText(QCoreApplication.translate("BasePage", u"Locomotieven", None))
        self.btnWissels.setText(QCoreApplication.translate("BasePage", u"Wissels", None))
        self.btnSeinen.setText(QCoreApplication.translate("BasePage", u"Seinen", None))
        self.btnStraatlicht.setText(QCoreApplication.translate("BasePage", u"Straatverlichting", None))
        self.btnScenerylicht.setText(QCoreApplication.translate("BasePage", u"Scenery Verlichting", None))
        self.btnConnectiviteit.setText(QCoreApplication.translate("BasePage", u"Connectiviteit", None))
        self.btnAfsluiten.setText(QCoreApplication.translate("BasePage", u"Afsluiten", None))
    # retranslateUi

