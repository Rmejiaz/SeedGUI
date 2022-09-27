from PySide6 import QtWidgets
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile, QIODevice
import sys
import os
from createSession import CreateSession



class MainWindow(QMainWindow):
    def  __init__ ( self ):
        
        super().__init__()
        self.main = QUiLoader().load(os.path.join('static', 'main.ui'))     
        self.main.showNormal()
        self.main.actionNuevo_Experimento.triggered.connect(lambda evt: self.create_session())
        

        self.sessionInfo = {'Nombre': None, 'Parametros': None, 'Cantidad': None, 'Duracion': None, 'Frecuencia':None}


    
    def create_session(self):
        self.session = CreateSession(self.main,self.sessionInfo)


        # self.main.labelNombre.setText(self.session.sessionName)


if __name__ == "__main__":
    
    app  =  QApplication ([]) 
    window  =  MainWindow() 
    app.exec ()