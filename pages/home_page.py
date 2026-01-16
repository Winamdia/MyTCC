# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'homepage.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QPushButton, QScrollArea, QSizePolicy, QSlider,
    QSpacerItem, QStackedWidget, QVBoxLayout, QWidget)

class Ui_HomePage(object):
    def setupUi(self, HomePage):
        if not HomePage.objectName():
            HomePage.setObjectName(u"HomePage")
        HomePage.resize(1243, 753)
        self.horizontalLayout_2 = QHBoxLayout(HomePage)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(15, -1, 15, -1)
        self.btnLayerMin1 = QPushButton(HomePage)
        self.btnLayerMin1.setObjectName(u"btnLayerMin1")
        self.btnLayerMin1.setMinimumSize(QSize(80, 0))

        self.horizontalLayout.addWidget(self.btnLayerMin1)

        self.btnLayer0 = QPushButton(HomePage)
        self.btnLayer0.setObjectName(u"btnLayer0")
        self.btnLayer0.setMinimumSize(QSize(80, 0))

        self.horizontalLayout.addWidget(self.btnLayer0)

        self.btnLayer1 = QPushButton(HomePage)
        self.btnLayer1.setObjectName(u"btnLayer1")
        self.btnLayer1.setMinimumSize(QSize(80, 0))

        self.horizontalLayout.addWidget(self.btnLayer1)

        self.horizontalSpacer = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.btnGrid = QPushButton(HomePage)
        self.btnGrid.setObjectName(u"btnGrid")
        self.btnGrid.setMinimumSize(QSize(80, 0))

        self.horizontalLayout.addWidget(self.btnGrid)

        self.horizontalSlider = QSlider(HomePage)
        self.horizontalSlider.setObjectName(u"horizontalSlider")
        self.horizontalSlider.setMinimumSize(QSize(100, 0))
        self.horizontalSlider.setMinimum(5)
        self.horizontalSlider.setMaximum(100)
        self.horizontalSlider.setValue(10)
        self.horizontalSlider.setOrientation(Qt.Orientation.Horizontal)
        self.horizontalSlider.setTickInterval(10)

        self.horizontalLayout.addWidget(self.horizontalSlider)

        self.lblGridSize = QLabel(HomePage)
        self.lblGridSize.setObjectName(u"lblGridSize")
        self.lblGridSize.setMinimumSize(QSize(80, 0))
        self.lblGridSize.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout.addWidget(self.lblGridSize)

        self.horizontalSpacer_2 = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.btnDuplicate = QPushButton(HomePage)
        self.btnDuplicate.setObjectName(u"btnDuplicate")
        self.btnDuplicate.setMinimumSize(QSize(80, 0))

        self.horizontalLayout.addWidget(self.btnDuplicate)

        self.btnDelete = QPushButton(HomePage)
        self.btnDelete.setObjectName(u"btnDelete")
        self.btnDelete.setMinimumSize(QSize(80, 0))

        self.horizontalLayout.addWidget(self.btnDelete)

        self.btnRotate = QPushButton(HomePage)
        self.btnRotate.setObjectName(u"btnRotate")
        self.btnRotate.setMinimumSize(QSize(80, 0))

        self.horizontalLayout.addWidget(self.btnRotate)

        self.btnFront = QPushButton(HomePage)
        self.btnFront.setObjectName(u"btnFront")
        self.btnFront.setMinimumSize(QSize(80, 0))

        self.horizontalLayout.addWidget(self.btnFront)

        self.btnBack = QPushButton(HomePage)
        self.btnBack.setObjectName(u"btnBack")
        self.btnBack.setMinimumSize(QSize(80, 0))

        self.horizontalLayout.addWidget(self.btnBack)

        self.btnDeselect = QPushButton(HomePage)
        self.btnDeselect.setObjectName(u"btnDeselect")
        self.btnDeselect.setMinimumSize(QSize(80, 0))

        self.horizontalLayout.addWidget(self.btnDeselect)

        self.horizontalSpacer_3 = QSpacerItem(120, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_3)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.stackLayers = QStackedWidget(HomePage)
        self.stackLayers.setObjectName(u"stackLayers")
        self.stackLayers.setFrameShape(QFrame.Shape.Box)
        self.stackLayers.setLineWidth(3)
        self.Layer1Page = QWidget()
        self.Layer1Page.setObjectName(u"Layer1Page")
        self.stackLayers.addWidget(self.Layer1Page)
        self.Layer2Page = QWidget()
        self.Layer2Page.setObjectName(u"Layer2Page")
        self.stackLayers.addWidget(self.Layer2Page)
        self.Layer3Page = QWidget()
        self.Layer3Page.setObjectName(u"Layer3Page")
        self.stackLayers.addWidget(self.Layer3Page)

        self.horizontalLayout_4.addWidget(self.stackLayers)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.btnSporen = QPushButton(HomePage)
        self.btnSporen.setObjectName(u"btnSporen")
        self.btnSporen.setMinimumSize(QSize(80, 0))

        self.verticalLayout_2.addWidget(self.btnSporen)

        self.btnSeinen = QPushButton(HomePage)
        self.btnSeinen.setObjectName(u"btnSeinen")
        self.btnSeinen.setMinimumSize(QSize(80, 0))

        self.verticalLayout_2.addWidget(self.btnSeinen)

        self.btnVerlichting = QPushButton(HomePage)
        self.btnVerlichting.setObjectName(u"btnVerlichting")
        self.btnVerlichting.setMinimumSize(QSize(80, 0))

        self.verticalLayout_2.addWidget(self.btnVerlichting)

        self.btnScenery = QPushButton(HomePage)
        self.btnScenery.setObjectName(u"btnScenery")
        self.btnScenery.setMinimumSize(QSize(80, 0))

        self.verticalLayout_2.addWidget(self.btnScenery)

        self.btnMelders = QPushButton(HomePage)
        self.btnMelders.setObjectName(u"btnMelders")
        self.btnMelders.setMinimumSize(QSize(80, 0))

        self.verticalLayout_2.addWidget(self.btnMelders)


        self.horizontalLayout_4.addLayout(self.verticalLayout_2)

        self.horizontalLayout_4.setStretch(0, 8)
        self.horizontalLayout_4.setStretch(1, 1)

        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.scrollObjectBar = QScrollArea(HomePage)
        self.scrollObjectBar.setObjectName(u"scrollObjectBar")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollObjectBar.sizePolicy().hasHeightForWidth())
        self.scrollObjectBar.setSizePolicy(sizePolicy)
        self.scrollObjectBar.setMinimumSize(QSize(0, 80))
        self.scrollObjectBar.setLineWidth(2)
        self.scrollObjectBar.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.scrollObjectBar.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 1219, 78))
        self.scrollObjectBar.setWidget(self.scrollAreaWidgetContents)

        self.horizontalLayout_3.addWidget(self.scrollObjectBar)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 20)
        self.verticalLayout.setStretch(2, 3)

        self.horizontalLayout_2.addLayout(self.verticalLayout)


        self.retranslateUi(HomePage)

        self.stackLayers.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(HomePage)
    # setupUi

    def retranslateUi(self, HomePage):
        HomePage.setWindowTitle(QCoreApplication.translate("HomePage", u"Form", None))
        self.btnLayerMin1.setText(QCoreApplication.translate("HomePage", u"Layer -1", None))
        self.btnLayer0.setText(QCoreApplication.translate("HomePage", u"Layer 0", None))
        self.btnLayer1.setText(QCoreApplication.translate("HomePage", u"Layer 1", None))
        self.btnGrid.setText(QCoreApplication.translate("HomePage", u"Grid", None))
        self.lblGridSize.setText("")
        self.btnDuplicate.setText(QCoreApplication.translate("HomePage", u"Duplicate", None))
        self.btnDelete.setText(QCoreApplication.translate("HomePage", u"Delete", None))
        self.btnRotate.setText(QCoreApplication.translate("HomePage", u"Rotate", None))
        self.btnFront.setText(QCoreApplication.translate("HomePage", u"Bring to Front", None))
        self.btnBack.setText(QCoreApplication.translate("HomePage", u"Send to Back", None))
        self.btnDeselect.setText(QCoreApplication.translate("HomePage", u"Deselect", None))
        self.btnSporen.setText(QCoreApplication.translate("HomePage", u"Sporen", None))
        self.btnSeinen.setText(QCoreApplication.translate("HomePage", u"Seinen", None))
        self.btnVerlichting.setText(QCoreApplication.translate("HomePage", u"Verlichting", None))
        self.btnScenery.setText(QCoreApplication.translate("HomePage", u"Decor", None))
        self.btnMelders.setText(QCoreApplication.translate("HomePage", u"Melders", None))
    # retranslateUi

