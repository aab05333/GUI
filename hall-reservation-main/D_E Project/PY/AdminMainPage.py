# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'AdminMainPage.ui'
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
        self.loginCard.setGeometry(QRect(210, 140, 400, 271))
        self.loginCard.setStyleSheet(u"QFrame#loginCard {\n"
"    background-color: #23272A;\n"
"    border-radius: 20px;\n"
"}\n"
"")
        self.loginCard.setFrameShape(QFrame.Shape.StyledPanel)
        self.loginCard.setFrameShadow(QFrame.Shadow.Raised)
        self.ManageHallsButton = QPushButton(self.loginCard)
        self.ManageHallsButton.setObjectName(u"ManageHallsButton")
        self.ManageHallsButton.setGeometry(QRect(10, 20, 381, 50))
        self.ManageHallsButton.setStyleSheet(u"\n"
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
        self.LogoutButton.setGeometry(QRect(10, 200, 381, 50))
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
        self.VeiwAllReservationsButton = QPushButton(self.loginCard)
        self.VeiwAllReservationsButton.setObjectName(u"VeiwAllReservationsButton")
        self.VeiwAllReservationsButton.setGeometry(QRect(10, 80, 381, 50))
        self.VeiwAllReservationsButton.setStyleSheet(u"\n"
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
        self.ViewTransactionsButton = QPushButton(self.loginCard)
        self.ViewTransactionsButton.setObjectName(u"ViewTransactionsButton")
        self.ViewTransactionsButton.setGeometry(QRect(10, 140, 381, 50))
        self.ViewTransactionsButton.setStyleSheet(u"\n"
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
        self.titleLabel.setAutoFillBackground(False)
        self.titleLabel.setStyleSheet(u"font: 900 16pt \"Segoe UI\"; color: white;")
        self.titleLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.ManageHallsButton.setText(QCoreApplication.translate("Dialog", u"Manage Halls", None))
        self.LogoutButton.setText(QCoreApplication.translate("Dialog", u"Log Out", None))
        self.VeiwAllReservationsButton.setText(QCoreApplication.translate("Dialog", u"Veiw All Reservation", None))
        self.ViewTransactionsButton.setText(QCoreApplication.translate("Dialog", u"Veiw Transactions", None))
        self.titleLabel.setText(QCoreApplication.translate("Dialog", u"Welcome Admin", None))
    # retranslateUi

