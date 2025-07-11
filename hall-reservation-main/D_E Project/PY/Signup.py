# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Signup.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
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
    QLineEdit, QPushButton, QRadioButton, QSizePolicy,
    QWidget)

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
        self.loginCard.setGeometry(QRect(200, 20, 400, 431))
        self.loginCard.setStyleSheet(u"QFrame#loginCard {\n"
"    background-color: #23272A;\n"
"    border-radius: 20px;\n"
"}")
        self.loginCard.setFrameShape(QFrame.StyledPanel)
        self.loginCard.setFrameShadow(QFrame.Raised)
        self.titleLabel = QLabel(self.loginCard)
        self.titleLabel.setObjectName(u"titleLabel")
        self.titleLabel.setGeometry(QRect(0, 0, 400, 50))
        self.titleLabel.setStyleSheet(u"font: 900 16pt \"Segoe UI\"; color: white;")
        self.titleLabel.setAlignment(Qt.AlignCenter)
        self.label = QLabel(self.loginCard)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 90, 401, 31))
        self.label.setStyleSheet(u"font: 700 10pt \"Segoe UI\"; color: rgb(255, 255, 255);")
        self.label_2 = QLabel(self.loginCard)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(0, 180, 400, 31))
        self.label_2.setStyleSheet(u"font: 700 10pt \"Segoe UI\"; color: rgb(255, 255, 255);")
        self.usernameLineEdit = QLineEdit(self.loginCard)
        self.usernameLineEdit.setObjectName(u"usernameLineEdit")
        self.usernameLineEdit.setGeometry(QRect(0, 120, 400, 60))
        self.usernameLineEdit.setStyleSheet(u"QLineEdit {\n"
"    background-color: #1E1F22;\n"
"    border: none;\n"
"    color: white;\n"
"    padding-left: 10px;\n"
"}\n"
"QLineEdit:focus {\n"
"    border: 1px solid #5865F2;\n"
"}")
        self.usernameLineEdit.setPlaceholderText(u"Enter your username")
        self.passwordLineEdit = QLineEdit(self.loginCard)
        self.passwordLineEdit.setObjectName(u"passwordLineEdit")
        self.passwordLineEdit.setGeometry(QRect(0, 210, 400, 60))
        self.passwordLineEdit.setStyleSheet(u"QLineEdit {\n"
"    background-color: #1E1F22;\n"
"    border: none;\n"
"    color: white;\n"
"    padding-left: 10px;\n"
"}\n"
"QLineEdit:focus {\n"
"    border: 1px solid #5865F2;\n"
"}")
        self.passwordLineEdit.setEchoMode(QLineEdit.Password)
        self.passwordLineEdit.setPlaceholderText(u"Enter your password")
        self.SignupButton = QPushButton(self.loginCard)
        self.SignupButton.setObjectName(u"SignupButton")
        self.SignupButton.setGeometry(QRect(0, 370, 401, 61))
        self.SignupButton.setStyleSheet(u"QPushButton {\n"
"    font: 700 16pt \"Segoe UI\";\n"
"    color: white;\n"
"    background-color: #5865F2;\n"
"    border-bottom-left-radius: 20px;\n"
"    border-bottom-right-radius: 20px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #4752C4;\n"
"}")
        self.titleLabel_2 = QLabel(self.loginCard)
        self.titleLabel_2.setObjectName(u"titleLabel_2")
        self.titleLabel_2.setGeometry(QRect(0, 50, 400, 50))
        self.titleLabel_2.setStyleSheet(u"font: 900 16pt \"Segoe UI\"; color: white;")
        self.titleLabel_2.setAlignment(Qt.AlignCenter)
        self.label_3 = QLabel(self.loginCard)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(0, 270, 400, 31))
        self.label_3.setStyleSheet(u"font: 700 10pt \"Segoe UI\"; color: rgb(255, 255, 255);")
        self.ConfirmPasswordLineEdit = QLineEdit(self.loginCard)
        self.ConfirmPasswordLineEdit.setObjectName(u"ConfirmPasswordLineEdit")
        self.ConfirmPasswordLineEdit.setGeometry(QRect(0, 310, 400, 60))
        self.ConfirmPasswordLineEdit.setStyleSheet(u"QLineEdit {\n"
"    background-color: #1E1F22;\n"
"    border: none;\n"
"    color: white;\n"
"    padding-left: 10px;\n"
"}\n"
"QLineEdit:focus {\n"
"    border: 1px solid #5865F2;\n"
"}")
        self.ConfirmPasswordLineEdit.setEchoMode(QLineEdit.Password)
        self.ConfirmPasswordLineEdit.setPlaceholderText(u"Enter your password")
        self.AdminSignUpRadioButton = QRadioButton(self.widget)
        self.AdminSignUpRadioButton.setObjectName(u"AdminSignUpRadioButton")
        self.AdminSignUpRadioButton.setGeometry(QRect(330, 460, 141, 20))
        self.AdminSignUpRadioButton.setStyleSheet(u"font: 700 10pt \"Segoe UI\"; color: rgb(255, 255, 255);")

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.titleLabel.setText(QCoreApplication.translate("Dialog", u"Conference Hall Reservation", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"   USERNAME", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"   PASSWORD", None))
        self.SignupButton.setText(QCoreApplication.translate("Dialog", u"SIGN UP", None))
        self.titleLabel_2.setText(QCoreApplication.translate("Dialog", u"SIGN UP", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"   CONFIRM PASSWORD", None))
        self.AdminSignUpRadioButton.setText(QCoreApplication.translate("Dialog", u"SIGN UP AS ADMIN", None))
    # retranslateUi