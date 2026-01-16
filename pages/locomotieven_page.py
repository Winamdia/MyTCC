# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'locomotieven.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QListView, QPushButton,
    QSizePolicy, QSpacerItem, QTabWidget, QVBoxLayout,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1202, 766)
        self.verticalLayout_2 = QVBoxLayout(Form)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(20, -1, -1, -1)
        self.btnDelete = QPushButton(Form)
        self.btnDelete.setObjectName(u"btnDelete")
        self.btnDelete.setMinimumSize(QSize(80, 0))

        self.horizontalLayout.addWidget(self.btnDelete)

        self.btnAdd = QPushButton(Form)
        self.btnAdd.setObjectName(u"btnAdd")
        self.btnAdd.setMinimumSize(QSize(80, 0))

        self.horizontalLayout.addWidget(self.btnAdd)

        self.btnEdit = QPushButton(Form)
        self.btnEdit.setObjectName(u"btnEdit")
        self.btnEdit.setMinimumSize(QSize(80, 0))

        self.horizontalLayout.addWidget(self.btnEdit)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.trainList = QListView(Form)
        self.trainList.setObjectName(u"trainList")

        self.horizontalLayout_2.addWidget(self.trainList)

        self.trainTab = QTabWidget(Form)
        self.trainTab.setObjectName(u"trainTab")
        self.TbInfo = QWidget()
        self.TbInfo.setObjectName(u"TbInfo")
        self.trainTab.addTab(self.TbInfo, "")
        self.TbControl = QWidget()
        self.TbControl.setObjectName(u"TbControl")
        self.trainTab.addTab(self.TbControl, "")
        self.TbFunctions = QWidget()
        self.TbFunctions.setObjectName(u"TbFunctions")
        self.trainTab.addTab(self.TbFunctions, "")

        self.horizontalLayout_2.addWidget(self.trainTab)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 10)

        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.retranslateUi(Form)

        self.trainTab.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.btnDelete.setText(QCoreApplication.translate("Form", u"Delete", None))
        self.btnAdd.setText(QCoreApplication.translate("Form", u"Add", None))
        self.btnEdit.setText(QCoreApplication.translate("Form", u"Edit", None))
        self.trainTab.setTabText(self.trainTab.indexOf(self.TbInfo), QCoreApplication.translate("Form", u"Info", None))
        self.trainTab.setTabText(self.trainTab.indexOf(self.TbControl), QCoreApplication.translate("Form", u"Control", None))
        self.trainTab.setTabText(self.trainTab.indexOf(self.TbFunctions), QCoreApplication.translate("Form", u"Functions", None))
    # retranslateUi

