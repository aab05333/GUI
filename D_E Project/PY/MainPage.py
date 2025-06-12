# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainPage.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
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
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QLabel,
    QPushButton, QSizePolicy, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(800, 500)
        self.widget = QWidget(Dialog)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(0, 0, 801, 501))
        self.widget.setStyleSheet(u"QWidget#widget{background-color:rgb(44, 47, 51)}")
        self.loginCard = QFrame(self.widget)
        self.loginCard.setObjectName(u"loginCard")
        self.loginCard.setGeometry(QRect(210, 140, 400, 231))
        self.loginCard.setStyleSheet(u"QFrame#loginCard {\n"
"    background-color: #23272A;\n"
"    border-radius: 20px;\n"
"}\n"
"")
        self.loginCard.setFrameShape(QFrame.Shape.StyledPanel)
        self.loginCard.setFrameShadow(QFrame.Shadow.Raised)
        self.MakeReservationPageButton = QPushButton(self.loginCard)
        self.MakeReservationPageButton.setObjectName(u"MakeReservationPageButton")
        self.MakeReservationPageButton.setGeometry(QRect(10, 20, 381, 50))
        self.MakeReservationPageButton.setStyleSheet(u"\n"
"     QPushButton {\n"
"       font: 700 12pt \"Segoe UI\";\n"
"       color: white;\n"
"       background-color: #5865F2;\n"
"       border-radius: 12px;\n"
"     }\n"
"     QPushButton:hover {\n"
"       background-color: #4752C4;\n"
"     }\n"
"    ")
        self.LogoutButton = QPushButton(self.loginCard)
        self.LogoutButton.setObjectName(u"LogoutButton")
        self.LogoutButton.setGeometry(QRect(10, 160, 381, 50))
        self.LogoutButton.setStyleSheet(u"\n"
"     QPushButton {\n"
"       font: 700 12pt \"Segoe UI\";\n"
"       color: white;\n"
"       background-color: rgb(255, 0, 0);\n"
"       border-radius: 12px;\n"
"     }\n"
"     QPushButton:hover {\n"
"       background-color: rgb(199, 0, 0);\n"
"     }\n"
"    ")
        self.ViewReservationPageButton = QPushButton(self.loginCard)
        self.ViewReservationPageButton.setObjectName(u"ViewReservationPageButton")
        self.ViewReservationPageButton.setGeometry(QRect(10, 90, 381, 50))
        self.ViewReservationPageButton.setStyleSheet(u"\n"
"     QPushButton {\n"
"       font: 700 12pt \"Segoe UI\";\n"
"       color: white;\n"
"       background-color: #5865F2;\n"
"       border-radius: 12px;\n"
"     }\n"
"     QPushButton:hover {\n"
"       background-color: #4752C4;\n"
"     }\n"
"    ")
        self.titleLabel = QLabel(self.widget)
        self.titleLabel.setObjectName(u"titleLabel")
        self.titleLabel.setGeometry(QRect(210, 40, 400, 50))
        self.titleLabel.setStyleSheet(u"font: 900 16pt \"Segoe UI\"; color: white;")
        self.titleLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.MakeReservationPageButton.setText(QCoreApplication.translate("Dialog", u"Make Reservation", None))
        self.LogoutButton.setText(QCoreApplication.translate("Dialog", u"Log Out", None))
        self.ViewReservationPageButton.setText(QCoreApplication.translate("Dialog", u"Veiw Reservation", None))
        self.titleLabel.setText(QCoreApplication.translate("Dialog", u"Welcome", None))
    # retranslateUi

