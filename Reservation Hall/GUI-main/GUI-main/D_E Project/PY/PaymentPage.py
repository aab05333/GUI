# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'PaymentPage.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QWidget)

class Ui_PaymentPage(object):
    def setupUi(self, PaymentPage):
        if not PaymentPage.objectName():
            PaymentPage.setObjectName(u"PaymentPage")
        PaymentPage.resize(860, 560)
        PaymentPage.setStyleSheet(u"background-color: #23272A;")
        self.titleLabel = QLabel(PaymentPage)
        self.titleLabel.setObjectName(u"titleLabel")
        self.titleLabel.setGeometry(QRect(20, 20, 820, 40))
        self.titleLabel.setStyleSheet(u"font: 900 18pt \"Segoe UI\"; color: white;")
        self.reservationInfoLabel = QLabel(PaymentPage)
        self.reservationInfoLabel.setObjectName(u"reservationInfoLabel")
        self.reservationInfoLabel.setGeometry(QRect(20, 70, 820, 25))
        self.reservationInfoLabel.setStyleSheet(u"font: 700 12pt \"Segoe UI\"; color: white;")
        self.amountLabel = QLabel(PaymentPage)
        self.amountLabel.setObjectName(u"amountLabel")
        self.amountLabel.setGeometry(QRect(20, 110, 200, 25))
        self.amountLabel.setStyleSheet(u"font: 700 12pt \"Segoe UI\"; color: white;")
        self.amountValueLabel = QLabel(PaymentPage)
        self.amountValueLabel.setObjectName(u"amountValueLabel")
        self.amountValueLabel.setGeometry(QRect(230, 110, 200, 25))
        self.amountValueLabel.setStyleSheet(u"font: 700 14pt \"Segoe UI\"; color: #57F287;")
        self.paymentMethodLabel = QLabel(PaymentPage)
        self.paymentMethodLabel.setObjectName(u"paymentMethodLabel")
        self.paymentMethodLabel.setGeometry(QRect(20, 150, 200, 25))
        self.paymentMethodLabel.setStyleSheet(u"font: 700 12pt \"Segoe UI\"; color: white;")
        self.paymentMethodComboBox = QComboBox(PaymentPage)
        self.paymentMethodComboBox.addItem("")
        self.paymentMethodComboBox.addItem("")
        self.paymentMethodComboBox.addItem("")
        self.paymentMethodComboBox.addItem("")
        self.paymentMethodComboBox.setObjectName(u"paymentMethodComboBox")
        self.paymentMethodComboBox.setGeometry(QRect(20, 180, 300, 35))
        self.paymentMethodComboBox.setStyleSheet(u"\n"
"     QComboBox {\n"
"       background-color: #1E1F22;\n"
"       color: white;\n"
"       border-radius: 8px;\n"
"       padding-left: 10px;\n"
"     }\n"
"     QComboBox:hover {\n"
"       border: 1px solid #5865F2;\n"
"     }\n"
"    ")
        self.cardNumberLabel = QLabel(PaymentPage)
        self.cardNumberLabel.setObjectName(u"cardNumberLabel")
        self.cardNumberLabel.setGeometry(QRect(20, 230, 200, 25))
        self.cardNumberLabel.setStyleSheet(u"font: 700 12pt \"Segoe UI\"; color: white;")
        self.cardNumberLineEdit = QLineEdit(PaymentPage)
        self.cardNumberLineEdit.setObjectName(u"cardNumberLineEdit")
        self.cardNumberLineEdit.setGeometry(QRect(20, 260, 300, 35))
        self.cardNumberLineEdit.setStyleSheet(u"\n"
"     QLineEdit {\n"
"       background-color: #1E1F22;\n"
"       color: white;\n"
"       border-radius: 8px;\n"
"       padding-left: 10px;\n"
"     }\n"
"     QLineEdit:focus {\n"
"       border: 1px solid #5865F2;\n"
"     }\n"
"    ")
        self.expiryLabel = QLabel(PaymentPage)
        self.expiryLabel.setObjectName(u"expiryLabel")
        self.expiryLabel.setGeometry(QRect(20, 310, 200, 25))
        self.expiryLabel.setStyleSheet(u"font: 700 12pt \"Segoe UI\"; color: white;")
        self.expiryLineEdit = QLineEdit(PaymentPage)
        self.expiryLineEdit.setObjectName(u"expiryLineEdit")
        self.expiryLineEdit.setGeometry(QRect(20, 340, 140, 35))
        self.expiryLineEdit.setStyleSheet(u"\n"
"     QLineEdit {\n"
"       background-color: #1E1F22;\n"
"       color: white;\n"
"       border-radius: 8px;\n"
"       padding-left: 10px;\n"
"     }\n"
"     QLineEdit:focus {\n"
"       border: 1px solid #5865F2;\n"
"     }\n"
"    ")
        self.cvvLabel = QLabel(PaymentPage)
        self.cvvLabel.setObjectName(u"cvvLabel")
        self.cvvLabel.setGeometry(QRect(180, 310, 200, 25))
        self.cvvLabel.setStyleSheet(u"font: 700 12pt \"Segoe UI\"; color: white;")
        self.cvvLineEdit = QLineEdit(PaymentPage)
        self.cvvLineEdit.setObjectName(u"cvvLineEdit")
        self.cvvLineEdit.setGeometry(QRect(180, 340, 140, 35))
        self.cvvLineEdit.setStyleSheet(u"\n"
"     QLineEdit {\n"
"       background-color: #1E1F22;\n"
"       color: white;\n"
"       border-radius: 8px;\n"
"       padding-left: 10px;\n"
"     }\n"
"     QLineEdit:focus {\n"
"       border: 1px solid #5865F2;\n"
"     }\n"
"    ")
        self.cvvLineEdit.setEchoMode(QLineEdit.EchoMode.Password)
        self.payButton = QPushButton(PaymentPage)
        self.payButton.setObjectName(u"payButton")
        self.payButton.setGeometry(QRect(20, 400, 300, 50))
        self.payButton.setStyleSheet(u"\n"
"     QPushButton {\n"
"       font: 700 14pt \"Segoe UI\";\n"
"       color: white;\n"
"       background-color: #57F287;\n"
"       border-radius: 12px;\n"
"     }\n"
"     QPushButton:hover {\n"
"       background-color: #3BA55C;\n"
"     }\n"
"    ")
        self.confirmationFrame = QFrame(PaymentPage)
        self.confirmationFrame.setObjectName(u"confirmationFrame")
        self.confirmationFrame.setGeometry(QRect(350, 70, 480, 380))
        self.confirmationFrame.setStyleSheet(u"\n"
"     QFrame {\n"
"       background-color: #1E1F22;\n"
"       border-radius: 15px;\n"
"     }\n"
"    ")
        self.confirmationFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.confirmationFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.confirmationIconLabel = QLabel(self.confirmationFrame)
        self.confirmationIconLabel.setObjectName(u"confirmationIconLabel")
        self.confirmationIconLabel.setGeometry(QRect(190, 50, 100, 100))
        self.confirmationIconLabel.setStyleSheet(u"font: 72 48pt \"Segoe UI\"; color: #57F287;")
        self.confirmationIconLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.confirmationLabel = QLabel(self.confirmationFrame)
        self.confirmationLabel.setObjectName(u"confirmationLabel")
        self.confirmationLabel.setGeometry(QRect(50, 170, 380, 40))
        self.confirmationLabel.setStyleSheet(u"font: 700 16pt \"Segoe UI\"; color: white;")
        self.confirmationLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.confirmationDetailsLabel = QLabel(self.confirmationFrame)
        self.confirmationDetailsLabel.setObjectName(u"confirmationDetailsLabel")
        self.confirmationDetailsLabel.setGeometry(QRect(50, 220, 380, 60))
        self.confirmationDetailsLabel.setStyleSheet(u"font: 10pt \"Segoe UI\"; color: white;")
        self.confirmationDetailsLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.doneButton = QPushButton(self.confirmationFrame)
        self.doneButton.setObjectName(u"doneButton")
        self.doneButton.setGeometry(QRect(150, 300, 180, 50))
        self.doneButton.setStyleSheet(u"\n"
"      QPushButton {\n"
"        font: 700 12pt \"Segoe UI\";\n"
"        color: white;\n"
"        background-color: #5865F2;\n"
"        border-radius: 12px;\n"
"      }\n"
"      QPushButton:hover {\n"
"        background-color: #4752C4;\n"
"      }\n"
"     ")
        self.backButton = QPushButton(PaymentPage)
        self.backButton.setObjectName(u"backButton")
        self.backButton.setGeometry(QRect(20, 460, 300, 50))
        self.backButton.setStyleSheet(u"\n"
"     QPushButton {\n"
"       font: 700 14pt \"Segoe UI\";\n"
"       color: white;\n"
"       background-color: rgb(255, 0, 0);\n"
"       border-radius: 12px;\n"
"     }\n"
"     QPushButton:hover {\n"
"       background-color: rgb(170, 0, 0);\n"
"     }\n"
"    ")

        self.retranslateUi(PaymentPage)

        QMetaObject.connectSlotsByName(PaymentPage)
    # setupUi

    def retranslateUi(self, PaymentPage):
        self.titleLabel.setText(QCoreApplication.translate("PaymentPage", u"Payment", None))
        self.reservationInfoLabel.setText(QCoreApplication.translate("PaymentPage", u"Reservation: Hall A - Jan 1, 2023 - 2 hours", None))
        self.amountLabel.setText(QCoreApplication.translate("PaymentPage", u"Amount to Pay:", None))
        self.amountValueLabel.setText(QCoreApplication.translate("PaymentPage", u"$200.00", None))
        self.paymentMethodLabel.setText(QCoreApplication.translate("PaymentPage", u"Payment Method:", None))
        self.paymentMethodComboBox.setItemText(0, QCoreApplication.translate("PaymentPage", u"Credit Card", None))
        self.paymentMethodComboBox.setItemText(1, QCoreApplication.translate("PaymentPage", u"Debit Card", None))
        self.paymentMethodComboBox.setItemText(2, QCoreApplication.translate("PaymentPage", u"PayPal", None))
        self.paymentMethodComboBox.setItemText(3, QCoreApplication.translate("PaymentPage", u"Bank Transfer", None))

        self.cardNumberLabel.setText(QCoreApplication.translate("PaymentPage", u"Card Number", None))
        self.cardNumberLineEdit.setPlaceholderText(QCoreApplication.translate("PaymentPage", u"1234 5678 9012 3456", None))
        self.expiryLabel.setText(QCoreApplication.translate("PaymentPage", u"Expiry Date", None))
        self.expiryLineEdit.setPlaceholderText(QCoreApplication.translate("PaymentPage", u"MM/YY", None))
        self.cvvLabel.setText(QCoreApplication.translate("PaymentPage", u"CVV", None))
        self.cvvLineEdit.setPlaceholderText(QCoreApplication.translate("PaymentPage", u"123", None))
        self.payButton.setText(QCoreApplication.translate("PaymentPage", u"Pay Now", None))
        self.confirmationIconLabel.setText(QCoreApplication.translate("PaymentPage", u"\u2713", None))
        self.confirmationLabel.setText(QCoreApplication.translate("PaymentPage", u"Payment Successful!", None))
        self.confirmationDetailsLabel.setText(QCoreApplication.translate("PaymentPage", u"Transaction ID: CHR-123456789\n"
"Amount: $200.00\n"
"Date: Jan 1, 2023", None))
        self.doneButton.setText(QCoreApplication.translate("PaymentPage", u"Done", None))
        self.backButton.setText(QCoreApplication.translate("PaymentPage", u"Back", None))
        pass
    # retranslateUi

