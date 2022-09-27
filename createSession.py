from PySide6 import QtWidgets
from PySide6.QtCore import QFile, QObject, SIGNAL, QDir, QTimer
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile, QIODevice
import sys
import os


class CreateSession(QWidget):
    def __init__(self, main, sessionInfo):
        self.main = main
        self.sessionInfo = sessionInfo
        super().__init__()

        self.createSessionMain = QUiLoader().load(os.path.join('static', 'createSession.ui'))     
        self.createSessionMain.show()

        QObject().connect(self.createSessionMain.pushButtonCrear, SIGNAL ('clicked()'), self.session_created)

        


    def session_created(self):

        self.sessionInfo['Nombre'] = self.createSessionMain.lineEditNombre.text()
        self.sessionInfo['Parametros'] = self.createSessionMain.lineEditParametros.text()
        self.sessionInfo['Cantidad'] = self.createSessionMain.lineEditCantidad.text()
        self.sessionInfo['Duracion'] = self.createSessionMain.lineEditDuracion.text()
        self.sessionInfo['Frecuencia'] = self.createSessionMain.lineEditFrecuencia.text()


        self.createSessionMain.close()

if __name__ == '__main__':

    session = CreateSession()

    sys.exit()


    