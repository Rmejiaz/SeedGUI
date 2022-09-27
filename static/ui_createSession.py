# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'createSession.ui'
##
## Created by: Qt User Interface Compiler version 6.3.2
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
from PySide6.QtWidgets import (QApplication, QComboBox, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QStatusBar,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(566, 433)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 80, 141, 81))
        font = QFont()
        font.setPointSize(18)
        self.label.setFont(font)
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(30, 30, 111, 81))
        self.label_4.setFont(font)
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(30, 130, 121, 81))
        self.label_5.setFont(font)
        self.pushButtonCrear = QPushButton(self.centralwidget)
        self.pushButtonCrear.setObjectName(u"pushButtonCrear")
        self.pushButtonCrear.setGeometry(QRect(240, 340, 91, 41))
        self.pushButtonCrear.setFont(font)
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(30, 180, 121, 81))
        self.label_6.setFont(font)
        self.comboBoxTipoDuracion = QComboBox(self.centralwidget)
        self.comboBoxTipoDuracion.addItem("")
        self.comboBoxTipoDuracion.addItem("")
        self.comboBoxTipoDuracion.addItem("")
        self.comboBoxTipoDuracion.addItem("")
        self.comboBoxTipoDuracion.setObjectName(u"comboBoxTipoDuracion")
        self.comboBoxTipoDuracion.setGeometry(QRect(430, 210, 81, 31))
        font1 = QFont()
        font1.setPointSize(8)
        self.comboBoxTipoDuracion.setFont(font1)
        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(30, 230, 131, 81))
        self.label_7.setFont(font)
        self.comboBoxTipoFrecuencia = QComboBox(self.centralwidget)
        self.comboBoxTipoFrecuencia.addItem("")
        self.comboBoxTipoFrecuencia.addItem("")
        self.comboBoxTipoFrecuencia.addItem("")
        self.comboBoxTipoFrecuencia.addItem("")
        self.comboBoxTipoFrecuencia.setObjectName(u"comboBoxTipoFrecuencia")
        self.comboBoxTipoFrecuencia.setGeometry(QRect(430, 260, 81, 31))
        self.comboBoxTipoFrecuencia.setFont(font1)
        self.lineEditNombre = QLineEdit(self.centralwidget)
        self.lineEditNombre.setObjectName(u"lineEditNombre")
        self.lineEditNombre.setGeometry(QRect(180, 60, 331, 32))
        self.lineEditCantidad = QLineEdit(self.centralwidget)
        self.lineEditCantidad.setObjectName(u"lineEditCantidad")
        self.lineEditCantidad.setGeometry(QRect(180, 160, 331, 32))
        self.lineEditDuracion = QLineEdit(self.centralwidget)
        self.lineEditDuracion.setObjectName(u"lineEditDuracion")
        self.lineEditDuracion.setGeometry(QRect(180, 210, 241, 32))
        self.lineEditFrecuencia = QLineEdit(self.centralwidget)
        self.lineEditFrecuencia.setObjectName(u"lineEditFrecuencia")
        self.lineEditFrecuencia.setGeometry(QRect(180, 260, 241, 32))
        self.lineEditParams = QLineEdit(self.centralwidget)
        self.lineEditParams.setObjectName(u"lineEditParams")
        self.lineEditParams.setGeometry(QRect(180, 110, 331, 32))
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Crear Experimento", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Par\u00e1metros:", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Nombre:", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Cantidad:", None))
        self.pushButtonCrear.setText(QCoreApplication.translate("MainWindow", u"Iniciar", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Duraci\u00f3n:", None))
        self.comboBoxTipoDuracion.setItemText(0, QCoreApplication.translate("MainWindow", u"Minutos", None))
        self.comboBoxTipoDuracion.setItemText(1, QCoreApplication.translate("MainWindow", u"Horas", None))
        self.comboBoxTipoDuracion.setItemText(2, QCoreApplication.translate("MainWindow", u"Dias", None))
        self.comboBoxTipoDuracion.setItemText(3, QCoreApplication.translate("MainWindow", u"Semanas", None))

        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Frecuencia:", None))
        self.comboBoxTipoFrecuencia.setItemText(0, QCoreApplication.translate("MainWindow", u"Minutos", None))
        self.comboBoxTipoFrecuencia.setItemText(1, QCoreApplication.translate("MainWindow", u"Horas", None))
        self.comboBoxTipoFrecuencia.setItemText(2, QCoreApplication.translate("MainWindow", u"Dias", None))
        self.comboBoxTipoFrecuencia.setItemText(3, QCoreApplication.translate("MainWindow", u"Semanas", None))

    # retranslateUi

