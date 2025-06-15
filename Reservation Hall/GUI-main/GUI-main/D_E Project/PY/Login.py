# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Login.ui'
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
    QLineEdit, QPushButton, QSizePolicy, QWidget)

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
        self.loginCard.setGeometry(QRect(210, 49, 400, 361))
        self.loginCard.setStyleSheet(u"QFrame#loginCard {\n"
"    background-color: #23272A;\n"
"    border-radius: 20px;\n"
"}\n"
"")
        self.loginCard.setFrameShape(QFrame.Shape.StyledPanel)
        self.loginCard.setFrameShadow(QFrame.Shadow.Raised)
        self.titleLabel = QLabel(self.loginCard)
        self.titleLabel.setObjectName(u"titleLabel")
        self.titleLabel.setGeometry(QRect(0, 0, 400, 50))
        self.titleLabel.setStyleSheet(u"font: 900 16pt \"Segoe UI\"; color: white;")
        self.titleLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label = QLabel(self.loginCard)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 110, 401, 31))
        self.label.setStyleSheet(u"font: 700 10pt \"Segoe UI\"; color: rgb(255, 255, 255);")
        self.label_2 = QLabel(self.loginCard)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(0, 200, 400, 31))
        self.label_2.setStyleSheet(u"font: 700 10pt \"Segoe UI\"; color: rgb(255, 255, 255);")
        self.usernameLineEdit = QLineEdit(self.loginCard)
        self.usernameLineEdit.setObjectName(u"usernameLineEdit")
        self.usernameLineEdit.setGeometry(QRect(0, 140, 400, 60))
        self.usernameLineEdit.setStyleSheet(u"QLineEdit {\n"
"    background-color: #1E1F22;\n"
"    border: none;\n"
"    color: white;\n"
"    padding-left: 10px;\n"
"}\n"
"QLineEdit:focus {\n"
"    border: 1px solid #5865F2;\n"
"}\n"
"")
        self.passwordLineEdit = QLineEdit(self.loginCard)
        self.passwordLineEdit.setObjectName(u"passwordLineEdit")
        self.passwordLineEdit.setGeometry(QRect(0, 240, 400, 60))
        self.passwordLineEdit.setStyleSheet(u"QLineEdit {\n"
"    background-color: #1E1F22;\n"
"    border: none;\n"
"    color: white;\n"
"    padding-left: 10px;\n"
"}\n"
"QLineEdit:focus {\n"
"    border: 1px solid #5865F2;\n"
"}\n"
"")
        self.passwordLineEdit.setEchoMode(QLineEdit.EchoMode.Password)
        self.loginButton = QPushButton(self.loginCard)
        self.loginButton.setObjectName(u"loginButton")
        self.loginButton.setGeometry(QRect(0, 300, 401, 61))
        self.loginButton.setStyleSheet(u"QPushButton {\n"
"    font: 700 16pt \"Segoe UI\";\n"
"    color: white;\n"
"    background-color: #5865F2;\n"
"    border-bottom-left-radius: 20px;\n"
"    border-bottom-right-radius: 20px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #4752C4;\n"
"}\n"
"")
        self.titleLabel_2 = QLabel(self.loginCard)
        self.titleLabel_2.setObjectName(u"titleLabel_2")
        self.titleLabel_2.setGeometry(QRect(0, 50, 400, 50))
        self.titleLabel_2.setStyleSheet(u"font: 900 16pt \"Segoe UI\"; color: white;")
        self.titleLabel_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.AdminLoginPageButton = QPushButton(self.widget)
        self.AdminLoginPageButton.setObjectName(u"AdminLoginPageButton")
        self.AdminLoginPageButton.setGeometry(QRect(670, 20, 91, 24))
        self.AdminLoginPageButton.setStyleSheet(u"QPushButton {\n"
"	font: 700 10pt \"Segoe UI\";\n"
"    color: white;\n"
"    background-color: #5865F2;\n"
"border-radius: 12px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #4752C4;\n"
"}")
        icon = QIcon()
        icon.addFile(u"icons/administrator-32.ico", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.AdminLoginPageButton.setIcon(icon)
        self.SignUpPageButton = QPushButton(self.widget)
        self.SignUpPageButton.setObjectName(u"SignUpPageButton")
        self.SignUpPageButton.setGeometry(QRect(490, 420, 91, 24))
        self.SignUpPageButton.setStyleSheet(u"QPushButton {\n"
"	font: 700 10pt \"Segoe UI\";\n"
"    color: white;\n"
"    background-color: #5865F2;\n"
"border-radius: 12px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #4752C4;\n"
"}")
        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(240, 420, 261, 21))
        self.label_3.setStyleSheet(u"font: 10pt \"Segoe UI\"; color: rgb(255, 255, 255);")

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Login", None))
        self.titleLabel.setText(QCoreApplication.translate("Dialog", u"Conference Hall Reservation", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"   USERNAME", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"   PASSWORD", None))
        self.usernameLineEdit.setPlaceholderText(QCoreApplication.translate("Dialog", u"Enter your username", None))
        self.passwordLineEdit.setPlaceholderText(QCoreApplication.translate("Dialog", u"Enter your password", None))
        self.loginButton.setText(QCoreApplication.translate("Dialog", u"LOGIN", None))
        self.titleLabel_2.setText(QCoreApplication.translate("Dialog", u"LOGIN", None))
        self.AdminLoginPageButton.setText(QCoreApplication.translate("Dialog", u"ADMIN", None))
        self.SignUpPageButton.setText(QCoreApplication.translate("Dialog", u"SIGN UP", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"Dont Have An Account ? Make one now", None))
    # retranslateUi

