# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ManageHall.ui'
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

class Ui_HallView(object):
    def setupUi(self, HallView):
        if not HallView.objectName():
            HallView.setObjectName(u"HallView")
        HallView.resize(860, 560)
        HallView.setStyleSheet(u"background-color: #23272A;")
        self.titleLabel = QLabel(HallView)
        self.titleLabel.setObjectName(u"titleLabel")
        self.titleLabel.setGeometry(QRect(20, 20, 820, 40))
        self.titleLabel.setStyleSheet(u"font: 900 18pt \"Segoe UI\"; color: white;")
        self.hallTable = QTableWidget(HallView)
        if (self.hallTable.columnCount() < 4):
            self.hallTable.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.hallTable.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.hallTable.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.hallTable.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.hallTable.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.hallTable.setObjectName(u"hallTable")
        self.hallTable.setGeometry(QRect(20, 70, 820, 400))
        self.hallTable.setStyleSheet(u"\n"
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
        self.hallTable.setRowCount(0)
        self.hallTable.setColumnCount(4)
        self.addHallButton = QPushButton(HallView)
        self.addHallButton.setObjectName(u"addHallButton")
        self.addHallButton.setGeometry(QRect(20, 480, 120, 50))
        self.addHallButton.setStyleSheet(u"\n"
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
        self.editHallButton = QPushButton(HallView)
        self.editHallButton.setObjectName(u"editHallButton")
        self.editHallButton.setGeometry(QRect(160, 480, 120, 50))
        self.editHallButton.setStyleSheet(u"\n"
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
        self.deleteHallButton = QPushButton(HallView)
        self.deleteHallButton.setObjectName(u"deleteHallButton")
        self.deleteHallButton.setGeometry(QRect(300, 480, 120, 50))
        self.deleteHallButton.setStyleSheet(u"\n"
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
        self.backButton = QPushButton(HallView)
        self.backButton.setObjectName(u"backButton")
        self.backButton.setGeometry(QRect(440, 480, 120, 50))
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

        self.retranslateUi(HallView)

        QMetaObject.connectSlotsByName(HallView)
    # setupUi

    def retranslateUi(self, HallView):
        self.titleLabel.setText(QCoreApplication.translate("HallView", u"Manage Halls", None))
        ___qtablewidgetitem = self.hallTable.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("HallView", u"Hall Name", None));
        ___qtablewidgetitem1 = self.hallTable.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("HallView", u"Location", None));
        ___qtablewidgetitem2 = self.hallTable.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("HallView", u"Capacity", None));
        ___qtablewidgetitem3 = self.hallTable.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("HallView", u"Price", None));
        self.addHallButton.setText(QCoreApplication.translate("HallView", u"Add Hall", None))
        self.editHallButton.setText(QCoreApplication.translate("HallView", u"Edit Hall", None))
        self.deleteHallButton.setText(QCoreApplication.translate("HallView", u"Delete Hall", None))
        self.backButton.setText(QCoreApplication.translate("HallView", u"Back", None))
        pass
    # retranslateUi

