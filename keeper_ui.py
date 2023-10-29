# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'keeper.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_SSK(object):
    def setupUi(self, SSK):
        if not SSK.objectName():
            SSK.setObjectName(u"SSK")
        SSK.resize(400, 300)
        SSK.setMinimumSize(QSize(400, 300))
        SSK.setMaximumSize(QSize(800, 600))
        self.widget = QWidget(SSK)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(230, 165, 161, 126))
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.checkSkyrimClose = QCheckBox(self.widget)
        self.checkSkyrimClose.setObjectName(u"checkSkyrimClose")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkSkyrimClose.sizePolicy().hasHeightForWidth())
        self.checkSkyrimClose.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.checkSkyrimClose)

        self.ButtonSave = QPushButton(self.widget)
        self.ButtonSave.setObjectName(u"ButtonSave")
        sizePolicy.setHeightForWidth(self.ButtonSave.sizePolicy().hasHeightForWidth())
        self.ButtonSave.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.ButtonSave)


        self.retranslateUi(SSK)

        QMetaObject.connectSlotsByName(SSK)
    # setupUi

    def retranslateUi(self, SSK):
        SSK.setWindowTitle(QCoreApplication.translate("SSK", u"Skyrim Save Keeper", None))
        self.checkSkyrimClose.setText(QCoreApplication.translate("SSK", u"Save when closing Skyrim", None))
        self.ButtonSave.setText(QCoreApplication.translate("SSK", u"Save", None))
    # retranslateUi

