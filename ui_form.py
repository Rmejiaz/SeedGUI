# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
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
from PySide6.QtWidgets import (QApplication, QMainWindow, QMenu, QMenuBar,
    QSizePolicy, QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1033, 555)
        self.actionNuevo_Experimento = QAction(MainWindow)
        self.actionNuevo_Experimento.setObjectName(u"actionNuevo_Experimento")
        self.actionAbrir_Experimento = QAction(MainWindow)
        self.actionAbrir_Experimento.setObjectName(u"actionAbrir_Experimento")
        self.actionManual_de_Usuario = QAction(MainWindow)
        self.actionManual_de_Usuario.setObjectName(u"actionManual_de_Usuario")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1033, 30))
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
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionNuevo_Experimento.setText(QCoreApplication.translate("MainWindow", u"Nuevo Experimento", None))
        self.actionAbrir_Experimento.setText(QCoreApplication.translate("MainWindow", u"Abrir Experimento", None))
        self.actionManual_de_Usuario.setText(QCoreApplication.translate("MainWindow", u"Manual de Usuario", None))
        self.menuArchivo.setTitle(QCoreApplication.translate("MainWindow", u"Archivo", None))
        self.menuAyuda.setTitle(QCoreApplication.translate("MainWindow", u"Ayuda", None))
    # retranslateUi

