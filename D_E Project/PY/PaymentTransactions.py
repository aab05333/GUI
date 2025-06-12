# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'PaymentTransactions.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QHeaderView,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QTableWidget, QTableWidgetItem, QWidget)

class Ui_PaymentTransactions(object):
    def setupUi(self, PaymentTransactions):
        if not PaymentTransactions.objectName():
            PaymentTransactions.setObjectName(u"PaymentTransactions")
        PaymentTransactions.resize(860, 560)
        PaymentTransactions.setStyleSheet(u"background-color: #23272A;")
        self.titleLabel = QLabel(PaymentTransactions)
        self.titleLabel.setObjectName(u"titleLabel")
        self.titleLabel.setGeometry(QRect(20, 20, 820, 40))
        self.titleLabel.setStyleSheet(u"font: 900 18pt \"Segoe UI\"; color: white;")
        self.searchLineEdit = QLineEdit(PaymentTransactions)
        self.searchLineEdit.setObjectName(u"searchLineEdit")
        self.searchLineEdit.setGeometry(QRect(20, 70, 300, 35))
        self.searchLineEdit.setStyleSheet(u"\n"
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
        self.transactionsTable = QTableWidget(PaymentTransactions)
        if (self.transactionsTable.columnCount() < 5):
            self.transactionsTable.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        self.transactionsTable.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.transactionsTable.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.transactionsTable.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.transactionsTable.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.transactionsTable.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.transactionsTable.setObjectName(u"transactionsTable")
        self.transactionsTable.setGeometry(QRect(20, 120, 820, 350))
        self.transactionsTable.setStyleSheet(u"\n"
"     QTableWidget {\n"
"       background-color: #1E1F22;\n"
"       color: white;\n"
"       gridline-color: #5865F2;\n"
"       border-radius: 10px;\n"
"     }\n"
"     QHeaderView::section {\n"
"       background-color: #5865F2;\n"
"       color: white;\n"
"       font-weight: bold;\n"
"       border: none;\n"
"     }\n"
"    ")
        self.transactionsTable.setRowCount(0)
        self.transactionsTable.setColumnCount(5)
        self.filterComboBox = QComboBox(PaymentTransactions)
        self.filterComboBox.addItem("")
        self.filterComboBox.addItem("")
        self.filterComboBox.addItem("")
        self.filterComboBox.addItem("")
        self.filterComboBox.setObjectName(u"filterComboBox")
        self.filterComboBox.setGeometry(QRect(340, 70, 150, 35))
        self.filterComboBox.setStyleSheet(u"\n"
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
        self.exportButton = QPushButton(PaymentTransactions)
        self.exportButton.setObjectName(u"exportButton")
        self.exportButton.setGeometry(QRect(720, 30, 120, 35))
        self.exportButton.setStyleSheet(u"\n"
"     QPushButton {\n"
"       font: 700 10pt \"Segoe UI\";\n"
"       color: white;\n"
"       background-color: #5865F2;\n"
"       border-radius: 8px;\n"
"     }\n"
"     QPushButton:hover {\n"
"       background-color: #4752C4;\n"
"     }\n"
"    ")
        self.statsFrame = QFrame(PaymentTransactions)
        self.statsFrame.setObjectName(u"statsFrame")
        self.statsFrame.setGeometry(QRect(20, 480, 820, 60))
        self.statsFrame.setStyleSheet(u"\n"
"     QFrame {\n"
"       background-color: #1E1F22;\n"
"       border-radius: 10px;\n"
"     }\n"
"    ")
        self.statsFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.statsFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.totalLabel = QLabel(self.statsFrame)
        self.totalLabel.setObjectName(u"totalLabel")
        self.totalLabel.setGeometry(QRect(20, 15, 200, 30))
        self.totalLabel.setStyleSheet(u"font: 700 12pt \"Segoe UI\"; color: white;")
        self.revenueLabel = QLabel(self.statsFrame)
        self.revenueLabel.setObjectName(u"revenueLabel")
        self.revenueLabel.setGeometry(QRect(300, 15, 200, 30))
        self.revenueLabel.setStyleSheet(u"font: 700 12pt \"Segoe UI\"; color: #57F287;")
        self.exportButton_2 = QPushButton(PaymentTransactions)
        self.exportButton_2.setObjectName(u"exportButton_2")
        self.exportButton_2.setGeometry(QRect(720, 80, 120, 35))
        self.exportButton_2.setStyleSheet(u"\n"
"     QPushButton {\n"
"       font: 700 10pt \"Segoe UI\";\n"
"       color: white;\n"
"       background-color: rgb(255, 0, 0);\n"
"       border-radius: 8px;\n"
"     }\n"
"     QPushButton:hover {\n"
"       background-color: rgb(170, 0, 0);\n"
"     }\n"
"    ")

        self.retranslateUi(PaymentTransactions)

        QMetaObject.connectSlotsByName(PaymentTransactions)
    # setupUi

    def retranslateUi(self, PaymentTransactions):
        self.titleLabel.setText(QCoreApplication.translate("PaymentTransactions", u"Payment Transactions", None))
        self.searchLineEdit.setPlaceholderText(QCoreApplication.translate("PaymentTransactions", u"Search transactions...", None))
        ___qtablewidgetitem = self.transactionsTable.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("PaymentTransactions", u"Transaction ID", None));
        ___qtablewidgetitem1 = self.transactionsTable.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("PaymentTransactions", u"User", None));
        ___qtablewidgetitem2 = self.transactionsTable.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("PaymentTransactions", u"Reservation", None));
        ___qtablewidgetitem3 = self.transactionsTable.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("PaymentTransactions", u"Amount", None));
        ___qtablewidgetitem4 = self.transactionsTable.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("PaymentTransactions", u"Date", None));
        self.filterComboBox.setItemText(0, QCoreApplication.translate("PaymentTransactions", u"All Transactions", None))
        self.filterComboBox.setItemText(1, QCoreApplication.translate("PaymentTransactions", u"Today", None))
        self.filterComboBox.setItemText(2, QCoreApplication.translate("PaymentTransactions", u"This Week", None))
        self.filterComboBox.setItemText(3, QCoreApplication.translate("PaymentTransactions", u"This Month", None))

        self.exportButton.setText(QCoreApplication.translate("PaymentTransactions", u"Export to CSV", None))
        self.totalLabel.setText(QCoreApplication.translate("PaymentTransactions", u"Total Transactions: 125", None))
        self.revenueLabel.setText(QCoreApplication.translate("PaymentTransactions", u"Total Revenue: $12,500", None))
        self.exportButton_2.setText(QCoreApplication.translate("PaymentTransactions", u"Back", None))
        pass
    # retranslateUi

