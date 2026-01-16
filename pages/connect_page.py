# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'connectpage.ui'
##
## Created by: Qt User Interface Compiler version 6.10.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)
from pages import resources_rc

class Ui_ConnectPage(object):
    def setupUi(self, ConnectPage):
        if not ConnectPage.objectName():
            ConnectPage.setObjectName(u"ConnectPage")
        ConnectPage.resize(995, 784)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ConnectPage.sizePolicy().hasHeightForWidth())
        ConnectPage.setSizePolicy(sizePolicy)
        ConnectPage.setMinimumSize(QSize(0, 0))
        ConnectPage.setMaximumSize(QSize(16777215, 16777215))
        self.verticalLayout_2 = QVBoxLayout(ConnectPage)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(6, 6, 6, 6)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(12, 12, 12, 12)
        self.horizontalLayout_1 = QHBoxLayout()
        self.horizontalLayout_1.setObjectName(u"horizontalLayout_1")
        self.frameZ21 = QFrame(ConnectPage)
        self.frameZ21.setObjectName(u"frameZ21")
        self.frameZ21.setFrameShape(QFrame.Shape.StyledPanel)
        self.frameZ21.setFrameShadow(QFrame.Shadow.Raised)
        self.frameZ21.setLineWidth(5)
        self.horizontalLayout = QHBoxLayout(self.frameZ21)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lblZ21Icon = QLabel(self.frameZ21)
        self.lblZ21Icon.setObjectName(u"lblZ21Icon")
        sizePolicy.setHeightForWidth(self.lblZ21Icon.sizePolicy().hasHeightForWidth())
        self.lblZ21Icon.setSizePolicy(sizePolicy)
        self.lblZ21Icon.setMaximumSize(QSize(200, 200))
        self.lblZ21Icon.setPixmap(QPixmap(u":/icons/z21.png"))
        self.lblZ21Icon.setScaledContents(True)

        self.horizontalLayout.addWidget(self.lblZ21Icon)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.lblTitleZ21 = QLabel(self.frameZ21)
        self.lblTitleZ21.setObjectName(u"lblTitleZ21")
        font = QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.lblTitleZ21.setFont(font)
        self.lblTitleZ21.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.lblTitleZ21.setFrameShape(QFrame.Shape.Box)
        self.lblTitleZ21.setFrameShadow(QFrame.Shadow.Plain)
        self.lblTitleZ21.setLineWidth(2)
        self.lblTitleZ21.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_3.addWidget(self.lblTitleZ21)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(20, -1, 20, -1)
        self.lblz21IP = QLabel(self.frameZ21)
        self.lblz21IP.setObjectName(u"lblz21IP")
        font1 = QFont()
        font1.setPointSize(12)
        self.lblz21IP.setFont(font1)
        self.lblz21IP.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_7.addWidget(self.lblz21IP)

        self.lineEdit = QLineEdit(self.frameZ21)
        self.lineEdit.setObjectName(u"lineEdit")

        self.horizontalLayout_7.addWidget(self.lineEdit)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer)

        self.horizontalLayout_7.setStretch(0, 1)
        self.horizontalLayout_7.setStretch(1, 2)
        self.horizontalLayout_7.setStretch(2, 2)

        self.verticalLayout_3.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(10, -1, 20, -1)
        self.lblStatusZ21 = QLabel(self.frameZ21)
        self.lblStatusZ21.setObjectName(u"lblStatusZ21")
        font2 = QFont()
        font2.setPointSize(14)
        self.lblStatusZ21.setFont(font2)
        self.lblStatusZ21.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_8.addWidget(self.lblStatusZ21)

        self.lblStatusIndicatorZ21 = QLabel(self.frameZ21)
        self.lblStatusIndicatorZ21.setObjectName(u"lblStatusIndicatorZ21")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.lblStatusIndicatorZ21.sizePolicy().hasHeightForWidth())
        self.lblStatusIndicatorZ21.setSizePolicy(sizePolicy1)
        self.lblStatusIndicatorZ21.setMinimumSize(QSize(16, 16))
        self.lblStatusIndicatorZ21.setMaximumSize(QSize(16, 16))
        self.lblStatusIndicatorZ21.setStyleSheet(u"background-color: red;\n"
"border-radius: 6px;\n"
"border: 1px solid #333;\n"
"")
        self.lblStatusIndicatorZ21.setMargin(0)

        self.horizontalLayout_8.addWidget(self.lblStatusIndicatorZ21)

        self.horizontalSpacer_2 = QSpacerItem(60, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_2)

        self.horizontalLayout_8.setStretch(0, 1)
        self.horizontalLayout_8.setStretch(1, 1)
        self.horizontalLayout_8.setStretch(2, 4)

        self.verticalLayout_3.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.btnConnectZ21 = QPushButton(self.frameZ21)
        self.btnConnectZ21.setObjectName(u"btnConnectZ21")
        self.btnConnectZ21.setMinimumSize(QSize(150, 0))
        self.btnConnectZ21.setMaximumSize(QSize(250, 16777215))

        self.horizontalLayout_9.addWidget(self.btnConnectZ21)


        self.verticalLayout_3.addLayout(self.horizontalLayout_9)

        self.verticalLayout_3.setStretch(0, 1)
        self.verticalLayout_3.setStretch(1, 2)
        self.verticalLayout_3.setStretch(2, 2)
        self.verticalLayout_3.setStretch(3, 1)

        self.horizontalLayout.addLayout(self.verticalLayout_3)

        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 3)

        self.horizontalLayout_1.addWidget(self.frameZ21)


        self.verticalLayout.addLayout(self.horizontalLayout_1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.frameArduino = QFrame(ConnectPage)
        self.frameArduino.setObjectName(u"frameArduino")
        self.frameArduino.setFrameShape(QFrame.Shape.StyledPanel)
        self.frameArduino.setFrameShadow(QFrame.Shadow.Raised)
        self.frameArduino.setLineWidth(5)
        self.horizontalLayout_5 = QHBoxLayout(self.frameArduino)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.lblArduinoIcon = QLabel(self.frameArduino)
        self.lblArduinoIcon.setObjectName(u"lblArduinoIcon")
        sizePolicy.setHeightForWidth(self.lblArduinoIcon.sizePolicy().hasHeightForWidth())
        self.lblArduinoIcon.setSizePolicy(sizePolicy)
        self.lblArduinoIcon.setMaximumSize(QSize(200, 200))
        self.lblArduinoIcon.setPixmap(QPixmap(u":/icons/Arduino.png"))
        self.lblArduinoIcon.setScaledContents(True)

        self.horizontalLayout_5.addWidget(self.lblArduinoIcon)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.lblTitleArduino = QLabel(self.frameArduino)
        self.lblTitleArduino.setObjectName(u"lblTitleArduino")
        self.lblTitleArduino.setFont(font)
        self.lblTitleArduino.setFrameShape(QFrame.Shape.Box)
        self.lblTitleArduino.setLineWidth(2)
        self.lblTitleArduino.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_4.addWidget(self.lblTitleArduino)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(20, -1, 20, -1)
        self.lblArduinoCom = QLabel(self.frameArduino)
        self.lblArduinoCom.setObjectName(u"lblArduinoCom")
        self.lblArduinoCom.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.lblArduinoCom)

        self.cmbArduinoPort = QComboBox(self.frameArduino)
        self.cmbArduinoPort.setObjectName(u"cmbArduinoPort")

        self.horizontalLayout_3.addWidget(self.cmbArduinoPort)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)

        self.horizontalLayout_3.setStretch(0, 1)
        self.horizontalLayout_3.setStretch(1, 2)
        self.horizontalLayout_3.setStretch(2, 2)

        self.verticalLayout_4.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(15, -1, 20, -1)
        self.label = QLabel(self.frameArduino)
        self.label.setObjectName(u"label")
        self.label.setFont(font2)
        self.label.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_10.addWidget(self.label)

        self.lblStatusIndicatorArduino = QLabel(self.frameArduino)
        self.lblStatusIndicatorArduino.setObjectName(u"lblStatusIndicatorArduino")
        sizePolicy1.setHeightForWidth(self.lblStatusIndicatorArduino.sizePolicy().hasHeightForWidth())
        self.lblStatusIndicatorArduino.setSizePolicy(sizePolicy1)
        self.lblStatusIndicatorArduino.setMinimumSize(QSize(16, 16))
        self.lblStatusIndicatorArduino.setMaximumSize(QSize(16, 16))
        self.lblStatusIndicatorArduino.setStyleSheet(u"background-color: red;\n"
"border-radius: 6px;\n"
"border: 1px solid #333;\n"
"")

        self.horizontalLayout_10.addWidget(self.lblStatusIndicatorArduino)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_4)

        self.horizontalLayout_10.setStretch(0, 1)
        self.horizontalLayout_10.setStretch(1, 1)
        self.horizontalLayout_10.setStretch(2, 4)

        self.verticalLayout_4.addLayout(self.horizontalLayout_10)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.btnConnectArduino = QPushButton(self.frameArduino)
        self.btnConnectArduino.setObjectName(u"btnConnectArduino")
        self.btnConnectArduino.setMinimumSize(QSize(150, 0))
        self.btnConnectArduino.setMaximumSize(QSize(250, 16777215))

        self.horizontalLayout_11.addWidget(self.btnConnectArduino)


        self.verticalLayout_4.addLayout(self.horizontalLayout_11)

        self.verticalLayout_4.setStretch(0, 1)
        self.verticalLayout_4.setStretch(1, 2)
        self.verticalLayout_4.setStretch(2, 2)
        self.verticalLayout_4.setStretch(3, 1)

        self.horizontalLayout_5.addLayout(self.verticalLayout_4)

        self.horizontalLayout_5.setStretch(0, 1)
        self.horizontalLayout_5.setStretch(1, 3)

        self.horizontalLayout_2.addWidget(self.frameArduino)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.frameRouter = QFrame(ConnectPage)
        self.frameRouter.setObjectName(u"frameRouter")
        self.frameRouter.setFrameShape(QFrame.Shape.StyledPanel)
        self.frameRouter.setFrameShadow(QFrame.Shadow.Raised)
        self.frameRouter.setLineWidth(5)
        self.horizontalLayout_6 = QHBoxLayout(self.frameRouter)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.lblRouterIcon = QLabel(self.frameRouter)
        self.lblRouterIcon.setObjectName(u"lblRouterIcon")
        sizePolicy.setHeightForWidth(self.lblRouterIcon.sizePolicy().hasHeightForWidth())
        self.lblRouterIcon.setSizePolicy(sizePolicy)
        self.lblRouterIcon.setMinimumSize(QSize(0, 0))
        self.lblRouterIcon.setMaximumSize(QSize(200, 200))
        self.lblRouterIcon.setPixmap(QPixmap(u":/icons/Router.png"))
        self.lblRouterIcon.setScaledContents(True)

        self.horizontalLayout_6.addWidget(self.lblRouterIcon)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.lblTitleRouter = QLabel(self.frameRouter)
        self.lblTitleRouter.setObjectName(u"lblTitleRouter")
        self.lblTitleRouter.setFont(font)
        self.lblTitleRouter.setFrameShape(QFrame.Shape.Box)
        self.lblTitleRouter.setLineWidth(2)
        self.lblTitleRouter.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_5.addWidget(self.lblTitleRouter)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(15, -1, 20, -1)
        self.lblRouterIP = QLabel(self.frameRouter)
        self.lblRouterIP.setObjectName(u"lblRouterIP")
        self.lblRouterIP.setFont(font1)
        self.lblRouterIP.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_12.addWidget(self.lblRouterIP)

        self.lineEdit_2 = QLineEdit(self.frameRouter)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.horizontalLayout_12.addWidget(self.lineEdit_2)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_5)

        self.horizontalLayout_12.setStretch(0, 1)
        self.horizontalLayout_12.setStretch(1, 2)
        self.horizontalLayout_12.setStretch(2, 2)

        self.verticalLayout_5.addLayout(self.horizontalLayout_12)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(15, -1, 20, -1)
        self.label_2 = QLabel(self.frameRouter)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font2)
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_13.addWidget(self.label_2)

        self.lblStatusIndicatoRouter = QLabel(self.frameRouter)
        self.lblStatusIndicatoRouter.setObjectName(u"lblStatusIndicatoRouter")
        self.lblStatusIndicatoRouter.setMinimumSize(QSize(16, 16))
        self.lblStatusIndicatoRouter.setMaximumSize(QSize(16, 16))
        self.lblStatusIndicatoRouter.setStyleSheet(u"background-color: red;\n"
"border-radius: 6px;\n"
"border: 1px solid #333;\n"
"")

        self.horizontalLayout_13.addWidget(self.lblStatusIndicatoRouter)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_6)

        self.horizontalLayout_13.setStretch(0, 1)
        self.horizontalLayout_13.setStretch(1, 1)
        self.horizontalLayout_13.setStretch(2, 4)

        self.verticalLayout_5.addLayout(self.horizontalLayout_13)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.btnConnectRouter = QPushButton(self.frameRouter)
        self.btnConnectRouter.setObjectName(u"btnConnectRouter")
        self.btnConnectRouter.setMinimumSize(QSize(150, 0))
        self.btnConnectRouter.setMaximumSize(QSize(250, 16777215))

        self.horizontalLayout_14.addWidget(self.btnConnectRouter)


        self.verticalLayout_5.addLayout(self.horizontalLayout_14)

        self.verticalLayout_5.setStretch(0, 1)
        self.verticalLayout_5.setStretch(1, 2)
        self.verticalLayout_5.setStretch(2, 2)
        self.verticalLayout_5.setStretch(3, 1)

        self.horizontalLayout_6.addLayout(self.verticalLayout_5)

        self.horizontalLayout_6.setStretch(0, 1)
        self.horizontalLayout_6.setStretch(1, 3)

        self.horizontalLayout_4.addWidget(self.frameRouter)

        self.horizontalLayout_4.setStretch(0, 1)

        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 1)
        self.verticalLayout.setStretch(2, 1)

        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.retranslateUi(ConnectPage)

        QMetaObject.connectSlotsByName(ConnectPage)
    # setupUi

    def retranslateUi(self, ConnectPage):
        ConnectPage.setWindowTitle(QCoreApplication.translate("ConnectPage", u"Form", None))
        self.lblZ21Icon.setText("")
        self.lblTitleZ21.setText(QCoreApplication.translate("ConnectPage", u"z21", None))
        self.lblz21IP.setText(QCoreApplication.translate("ConnectPage", u"IP-Adres:", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("ConnectPage", u"192.168.0.111", None))
        self.lblStatusZ21.setText(QCoreApplication.translate("ConnectPage", u"Status:", None))
        self.lblStatusIndicatorZ21.setText("")
        self.btnConnectZ21.setText(QCoreApplication.translate("ConnectPage", u"Connect z21", None))
        self.lblArduinoIcon.setText("")
        self.lblTitleArduino.setText(QCoreApplication.translate("ConnectPage", u"Arduino", None))
        self.lblArduinoCom.setText(QCoreApplication.translate("ConnectPage", u"Com-Poort:", None))
        self.label.setText(QCoreApplication.translate("ConnectPage", u"Status:", None))
        self.lblStatusIndicatorArduino.setText("")
        self.btnConnectArduino.setText(QCoreApplication.translate("ConnectPage", u"Connect Arduino", None))
        self.lblRouterIcon.setText("")
        self.lblTitleRouter.setText(QCoreApplication.translate("ConnectPage", u"Router", None))
        self.lblRouterIP.setText(QCoreApplication.translate("ConnectPage", u"IP-Adres:", None))
        self.lineEdit_2.setPlaceholderText(QCoreApplication.translate("ConnectPage", u"192.168.0.1", None))
        self.label_2.setText(QCoreApplication.translate("ConnectPage", u"Status:", None))
        self.lblStatusIndicatoRouter.setText("")
        self.btnConnectRouter.setText(QCoreApplication.translate("ConnectPage", u"Connect Router", None))
    # retranslateUi

