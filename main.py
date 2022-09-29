from PySide6 import QtWidgets
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile, QIODevice, QThread, QTimer, QSize
import sys
import os
from createSession import CreateSession
import cv2
from PySide6.QtGui import QImage, QPixmap
from datetime import datetime







class MainWindow(QMainWindow):
    def  __init__ ( self ):
        
        super().__init__()
        self.main = QUiLoader().load(os.path.join('static', 'main.ui'))     
        self.main.showNormal()
        self.main.actionNuevo_Experimento.triggered.connect(lambda evt: self.create_session())
        
        

        #Camera and video setup
        self.video_size = QSize(640, 480)
        self.setup_camera()
        
        # Session info

        self.sessionInfo = {'Nombre': None, 'Parametros': None, 'Cantidad': None, 'Duracion': None, 'Frecuencia':None, 'Inicio':None, 'Fin':None}


    
    def create_session(self):
        self.session = CreateSession(self.main,self.sessionInfo)


    

    def begin_session(self):

        self.sessionInfo['Inicio'] = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        self.sessionInfo['Duracion'] = self.code_time(self.sessionInfo['Duracion'])
        self.sessionInfo['Frecuencia'] = self.code_time(self.sessionInfo['Frecuencia'])
        


        self.main.labelInicio.text(self.sessionInfo['Inicio'])
        

    def code_time(self, time):

        unit = time[1]
        time = time[0]

        if unit =='Segundos':
            return time
        
        if unit == 'Minutos':
            return time*60
        
        if unit == 'Horas':
            return time*3600
        
        if unit == 'Dias':
            return time*3600*24
        
        if unit == 'Semanas':
            return time*3600*24*7




    def setup_camera(self):
        """Initialize camera.
        """
        self.capture = cv2.VideoCapture(0)
        self.capture.set(cv2.CAP_PROP_FRAME_WIDTH, self.video_size.width())
        self.capture.set(cv2.CAP_PROP_FRAME_HEIGHT, self.video_size.height())

        self.timer = QTimer()
        self.timer.timeout.connect(self.display_video_stream)
        self.timer.start(30)

    def display_video_stream(self):
        """Read frame from camera and repaint QLabel widget.
        """
        _, frame = self.capture.read()
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame = cv2.flip(frame, 1)
        image = QImage(frame, frame.shape[1], frame.shape[0], 
                       frame.strides[0], QImage.Format_RGB888)
        self.main.videoLabel.setPixmap(QPixmap.fromImage(image))




if __name__ == "__main__":
    
    app  =  QApplication ([]) 
    window  =  MainWindow() 
    app.exec ()