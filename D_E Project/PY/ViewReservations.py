# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ViewReservations.ui'
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
from PySide6.QtWidgets import (QApplication, QHeaderView, QLabel, QPushButton,
    QSizePolicy, QTableWidget, QTableWidgetItem, QWidget)

class Ui_ViewReservation(object):
    def setupUi(self, ViewReservation):
        if not ViewReservation.objectName():
            ViewReservation.setObjectName(u"ViewReservation")
        ViewReservation.resize(860, 560)
        ViewReservation.setStyleSheet(u"background-color: #23272A;")
        self.titleLabel = QLabel(ViewReservation)
        self.titleLabel.setObjectName(u"titleLabel")
        self.titleLabel.setGeometry(QRect(20, 20, 820, 40))
        self.titleLabel.setStyleSheet(u"font: 900 18pt \"Segoe UI\"; color: white;")
        self.reservationsTable = QTableWidget(ViewReservation)
        if (self.reservationsTable.columnCount() < 4):
            self.reservationsTable.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.reservationsTable.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.reservationsTable.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.reservationsTable.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.reservationsTable.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.reservationsTable.setObjectName(u"reservationsTable")
        self.reservationsTable.setGeometry(QRect(20, 70, 820, 400))
        self.reservationsTable.setStyleSheet(u"\n"
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
        self.reservationsTable.setRowCount(0)
        self.reservationsTable.setColumnCount(4)
        self.btnDeleteReservation = QPushButton(ViewReservation)
        self.btnDeleteReservation.setObjectName(u"btnDeleteReservation")
        self.btnDeleteReservation.setGeometry(QRect(20, 480, 120, 50))
        self.btnDeleteReservation.setStyleSheet(u"\n"
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
        self.btnEditReservation = QPushButton(ViewReservation)
        self.btnEditReservation.setObjectName(u"btnEditReservation")
        self.btnEditReservation.setGeometry(QRect(160, 480, 120, 50))
        self.btnEditReservation.setStyleSheet(u"\n"
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
        self.btnBack = QPushButton(ViewReservation)
        self.btnBack.setObjectName(u"btnBack")
        self.btnBack.setGeometry(QRect(300, 480, 120, 50))
        self.btnBack.setStyleSheet(u"\n"
"     QPushButton {\n"
"       font: 700 12pt \"Segoe UI\";\n"
"       color: white;\n"
"       background-color: rgb(255, 0, 0);\n"
"       border-radius: 12px;\n"
"     }\n"
"     QPushButton:hover {\n"
"       background-color: rgb(170, 0, 0);\n"
"     }\n"
"    ")

        self.retranslateUi(ViewReservation)

        QMetaObject.connectSlotsByName(ViewReservation)
    # setupUi

    def retranslateUi(self, ViewReservation):
        self.titleLabel.setText(QCoreApplication.translate("ViewReservation", u"My Reservations", None))
        ___qtablewidgetitem = self.reservationsTable.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("ViewReservation", u"Hall", None));
        ___qtablewidgetitem1 = self.reservationsTable.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("ViewReservation", u"Date", None));
        ___qtablewidgetitem2 = self.reservationsTable.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("ViewReservation", u"Duration", None));
        ___qtablewidgetitem3 = self.reservationsTable.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("ViewReservation", u"Price", None));
        self.btnDeleteReservation.setText(QCoreApplication.translate("ViewReservation", u"Delete", None))
        self.btnEditReservation.setText(QCoreApplication.translate("ViewReservation", u"Edit", None))
        self.btnBack.setText(QCoreApplication.translate("ViewReservation", u"Back", None))
        pass
    # retranslateUi

