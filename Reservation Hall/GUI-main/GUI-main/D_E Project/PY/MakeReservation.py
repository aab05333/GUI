# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MakeReservation.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QLabel,
    QListWidget, QListWidgetItem, QPushButton, QSizePolicy,
    QSpinBox, QWidget)

class Ui_ReservationView(object):
    def setupUi(self, ReservationView):
        if not ReservationView.objectName():
            ReservationView.setObjectName(u"ReservationView")
        ReservationView.resize(860, 561)
        ReservationView.setStyleSheet(u"background-color: #23272A;")
        self.titleLabel = QLabel(ReservationView)
        self.titleLabel.setObjectName(u"titleLabel")
        self.titleLabel.setGeometry(QRect(20, 20, 820, 40))
        self.titleLabel.setStyleSheet(u"font: 900 18pt \"Segoe UI\"; color: white;")
        self.hallLabel = QLabel(ReservationView)
        self.hallLabel.setObjectName(u"hallLabel")
        self.hallLabel.setGeometry(QRect(20, 80, 200, 25))
        self.hallLabel.setStyleSheet(u"font: 700 12pt \"Segoe UI\"; color: white;")
        self.hallComboBox = QComboBox(ReservationView)
        self.hallComboBox.setObjectName(u"hallComboBox")
        self.hallComboBox.setGeometry(QRect(20, 110, 300, 35))
        self.hallComboBox.setStyleSheet(u"\n"
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
        self.dateLabel = QLabel(ReservationView)
        self.dateLabel.setObjectName(u"dateLabel")
        self.dateLabel.setGeometry(QRect(20, 200, 200, 25))
        self.dateLabel.setStyleSheet(u"font: 700 12pt \"Segoe UI\"; color: white;")
        self.dateEdit = QDateEdit(ReservationView)
        self.dateEdit.setObjectName(u"dateEdit")
        self.dateEdit.setGeometry(QRect(20, 230, 300, 35))
        self.dateEdit.setStyleSheet(u"\n"
"     QDateEdit {\n"
"       background-color: #1E1F22;\n"
"       color: white;\n"
"       border-radius: 8px;\n"
"       padding-left: 10px;\n"
"     }\n"
"     QDateEdit:hover {\n"
"       border: 1px solid #5865F2;\n"
"     }\n"
"    ")
        self.dateEdit.setCalendarPopup(True)
        self.durationLabel = QLabel(ReservationView)
        self.durationLabel.setObjectName(u"durationLabel")
        self.durationLabel.setGeometry(QRect(20, 280, 200, 25))
        self.durationLabel.setStyleSheet(u"font: 700 12pt \"Segoe UI\"; color: white;")
        self.durationSpinBox = QSpinBox(ReservationView)
        self.durationSpinBox.setObjectName(u"durationSpinBox")
        self.durationSpinBox.setGeometry(QRect(20, 310, 120, 35))
        self.durationSpinBox.setStyleSheet(u"\n"
"     QSpinBox {\n"
"       background-color: #1E1F22;\n"
"       color: white;\n"
"       border-radius: 8px;\n"
"       padding-left: 10px;\n"
"     }\n"
"     QSpinBox:hover {\n"
"       border: 1px solid #5865F2;\n"
"     }\n"
"    ")
        self.durationSpinBox.setMinimum(1)
        self.durationSpinBox.setMaximum(12)
        self.slotsLabel = QLabel(ReservationView)
        self.slotsLabel.setObjectName(u"slotsLabel")
        self.slotsLabel.setGeometry(QRect(350, 80, 450, 25))
        self.slotsLabel.setStyleSheet(u"font: 700 12pt \"Segoe UI\"; color: white;")
        self.slotsListWidget = QListWidget(ReservationView)
        self.slotsListWidget.setObjectName(u"slotsListWidget")
        self.slotsListWidget.setGeometry(QRect(350, 110, 450, 250))
        self.slotsListWidget.setStyleSheet(u"\n"
"     QListWidget {\n"
"       background-color: #1E1F22;\n"
"       color: white;\n"
"       border-radius: 10px;\n"
"     }\n"
"    ")
        self.reserveButton = QPushButton(ReservationView)
        self.reserveButton.setObjectName(u"reserveButton")
        self.reserveButton.setGeometry(QRect(20, 360, 300, 60))
        self.reserveButton.setStyleSheet(u"\n"
"     QPushButton {\n"
"       font: 700 16pt \"Segoe UI\";\n"
"       color: white;\n"
"       background-color: #5865F2;\n"
"       border-radius: 15px;\n"
"     }\n"
"     QPushButton:hover {\n"
"       background-color: #4752C4;\n"
"     }\n"
"    ")
        self.label = QLabel(ReservationView)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 160, 291, 16))
        self.label.setStyleSheet(u"font: 700 12pt \"Segoe UI\";\n"
"color: white;\n"
"color: rgb(0, 202, 0);")
        self.BackButton = QPushButton(ReservationView)
        self.BackButton.setObjectName(u"BackButton")
        self.BackButton.setGeometry(QRect(20, 430, 300, 60))
        self.BackButton.setStyleSheet(u"\n"
"     QPushButton {\n"
"       font: 700 16pt \"Segoe UI\";\n"
"       color: white;\n"
"       background-color: rgb(255, 0, 0);\n"
"       border-radius: 15px;\n"
"     }\n"
"     QPushButton:hover {\n"
"       background-color: rgb(170, 0, 0);\n"
"     }\n"
"    ")

        self.retranslateUi(ReservationView)

        QMetaObject.connectSlotsByName(ReservationView)
    # setupUi

    def retranslateUi(self, ReservationView):
        self.titleLabel.setText(QCoreApplication.translate("ReservationView", u"Make a New Reservation", None))
        self.hallLabel.setText(QCoreApplication.translate("ReservationView", u"Select Hall", None))
        self.dateLabel.setText(QCoreApplication.translate("ReservationView", u"Select Date", None))
        self.durationLabel.setText(QCoreApplication.translate("ReservationView", u"Duration (hours)", None))
        self.slotsLabel.setText(QCoreApplication.translate("ReservationView", u"Available Time Slots", None))
        self.reserveButton.setText(QCoreApplication.translate("ReservationView", u"Reserve And Pay", None))
        self.label.setText(QCoreApplication.translate("ReservationView", u"Price: $0.00", None))
        self.BackButton.setText(QCoreApplication.translate("ReservationView", u"Back", None))
        pass
    # retranslateUi

