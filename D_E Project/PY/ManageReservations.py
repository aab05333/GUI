# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ManageReservations.ui'
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

class Ui_MyReservationsView(object):
    def setupUi(self, MyReservationsView):
        if not MyReservationsView.objectName():
            MyReservationsView.setObjectName(u"MyReservationsView")
        MyReservationsView.resize(860, 560)
        MyReservationsView.setStyleSheet(u"background-color: #23272A;")
        self.titleLabel = QLabel(MyReservationsView)
        self.titleLabel.setObjectName(u"titleLabel")
        self.titleLabel.setGeometry(QRect(20, 20, 820, 40))
        self.titleLabel.setStyleSheet(u"font: 900 18pt \"Segoe UI\"; color: white;")
        self.reservationsTable = QTableWidget(MyReservationsView)
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
        self.cancelButton = QPushButton(MyReservationsView)
        self.cancelButton.setObjectName(u"cancelButton")
        self.cancelButton.setGeometry(QRect(20, 480, 120, 50))
        self.cancelButton.setStyleSheet(u"\n"
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
        self.rescheduleButton = QPushButton(MyReservationsView)
        self.rescheduleButton.setObjectName(u"rescheduleButton")
        self.rescheduleButton.setGeometry(QRect(160, 480, 120, 50))
        self.rescheduleButton.setStyleSheet(u"\n"
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
        self.backButton = QPushButton(MyReservationsView)
        self.backButton.setObjectName(u"backButton")
        self.backButton.setGeometry(QRect(300, 480, 120, 50))
        self.backButton.setStyleSheet(u"\n"
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

        self.retranslateUi(MyReservationsView)

        QMetaObject.connectSlotsByName(MyReservationsView)
    # setupUi

    def retranslateUi(self, MyReservationsView):
        self.titleLabel.setText(QCoreApplication.translate("MyReservationsView", u"All Reservations", None))
        ___qtablewidgetitem = self.reservationsTable.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MyReservationsView", u"Hall", None));
        ___qtablewidgetitem1 = self.reservationsTable.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MyReservationsView", u"Date", None));
        ___qtablewidgetitem2 = self.reservationsTable.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MyReservationsView", u"Duration", None));
        ___qtablewidgetitem3 = self.reservationsTable.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MyReservationsView", u"Status", None));
        self.cancelButton.setText(QCoreApplication.translate("MyReservationsView", u"Cancel", None))
        self.rescheduleButton.setText(QCoreApplication.translate("MyReservationsView", u"Reschedule", None))
        self.backButton.setText(QCoreApplication.translate("MyReservationsView", u"Back", None))
        pass
    # retranslateUi

