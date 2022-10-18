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
        self.createSessionMain.advertenciaLabel.setVisible(False)
        


    def session_created(self):

        if(self.createSessionMain.lineEditNombre.text() == "" or self.createSessionMain.lineEditParams.text() == "" or self.createSessionMain.lineEditDuracion.text() == "" or self.createSessionMain.lineEditFrecuencia.text() == ""):
            self.createSessionMain.advertenciaLabel.setVisible(True)
        
        else:
            self.createSessionMain.advertenciaLabel.setVisible(True)




            self.sessionInfo['Nombre'] = self.createSessionMain.lineEditNombre.text()
            self.sessionInfo['Parametros'] = self.createSessionMain.lineEditParams.text()
            self.sessionInfo['Cantidad'] = self.createSessionMain.lineEditCantidad.text()
            self.sessionInfo['Duracion'] = (self.createSessionMain.lineEditDuracion.text(), self.createSessionMain.comboBoxUnidadDuracion.currentText())
            self.sessionInfo['Frecuencia'] = (self.createSessionMain.lineEditFrecuencia.text(), self.createSessionMain.comboBoxUnidadFrecuencia.currentText())


            self.main.labelNombre.setText(self.sessionInfo['Nombre'])



            self.createSessionMain.close()




if __name__ == '__main__':

    session = CreateSession()

    sys.exit()


    