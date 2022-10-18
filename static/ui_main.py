# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.3.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QMenu,
    QMenuBar, QProgressBar, QPushButton, QSizePolicy,
    QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1082, 599)
        self.actionNuevo_Experimento = QAction(MainWindow)
        self.actionNuevo_Experimento.setObjectName(u"actionNuevo_Experimento")
        self.actionAbrir_Experimento = QAction(MainWindow)
        self.actionAbrir_Experimento.setObjectName(u"actionAbrir_Experimento")
        self.actionManual_de_Usuario = QAction(MainWindow)
        self.actionManual_de_Usuario.setObjectName(u"actionManual_de_Usuario")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.videoLabel = QLabel(self.centralwidget)
        self.videoLabel.setObjectName(u"videoLabel")
        self.videoLabel.setGeometry(QRect(80, 40, 381, 371))
        self.progressBar = QProgressBar(self.centralwidget)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(80, 450, 911, 21))
        self.progressBar.setValue(24)
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(570, 30, 131, 41))
        font = QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(570, 80, 121, 41))
        self.label_2.setFont(font)
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(570, 130, 111, 41))
        self.label_3.setFont(font)
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(570, 180, 171, 41))
        self.label_4.setFont(font)
        self.labelNombre = QLabel(self.centralwidget)
        self.labelNombre.setObjectName(u"labelNombre")
        self.labelNombre.setGeometry(QRect(760, 30, 281, 41))
        self.labelNombre.setFont(font)
        self.labelTiempoRestante = QLabel(self.centralwidget)
        self.labelTiempoRestante.setObjectName(u"labelTiempoRestante")
        self.labelTiempoRestante.setGeometry(QRect(760, 180, 271, 41))
        self.labelTiempoRestante.setFont(font)
        self.labelFin = QLabel(self.centralwidget)
        self.labelFin.setObjectName(u"labelFin")
        self.labelFin.setGeometry(QRect(760, 130, 261, 41))
        self.labelFin.setFont(font)
        self.labelInicio = QLabel(self.centralwidget)
        self.labelInicio.setObjectName(u"labelInicio")
        self.labelInicio.setGeometry(QRect(760, 80, 281, 41))
        self.labelInicio.setFont(font)
        self.iniciarButton = QPushButton(self.centralwidget)
        self.iniciarButton.setObjectName(u"iniciarButton")
        self.iniciarButton.setGeometry(QRect(570, 250, 84, 34))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1082, 30))
        self.menuArchivo = QMenu(self.menubar)
        self.menuArchivo.setObjectName(u"menuArchivo")
        self.menuAyuda = QMenu(self.menubar)
        self.menuAyuda.setObjectName(u"menuAyuda")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuArchivo.menuAction())
        self.menubar.addAction(self.menuAyuda.menuAction())
        self.menuArchivo.addAction(self.actionNuevo_Experimento)
        self.menuArchivo.addAction(self.actionAbrir_Experimento)
        self.menuAyuda.addAction(self.actionManual_de_Usuario)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"SeedGUI", None))
        self.actionNuevo_Experimento.setText(QCoreApplication.translate("MainWindow", u"Nuevo Experimento", None))
        self.actionAbrir_Experimento.setText(QCoreApplication.translate("MainWindow", u"Abrir Experimento", None))
        self.actionManual_de_Usuario.setText(QCoreApplication.translate("MainWindow", u"Manual de Usuario", None))
        self.videoLabel.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Experimento:", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Inicio:", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Fin:", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Tiempo Restante:", None))
        self.labelNombre.setText("")
        self.labelTiempoRestante.setText("")
        self.labelFin.setText("")
        self.labelInicio.setText("")
        self.iniciarButton.setText(QCoreApplication.translate("MainWindow", u"Iniciar", None))
        self.menuArchivo.setTitle(QCoreApplication.translate("MainWindow", u"Archivo", None))
        self.menuAyuda.setTitle(QCoreApplication.translate("MainWindow", u"Ayuda", None))
    # retranslateUi

