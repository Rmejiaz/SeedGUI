from PySide6 import QtWidgets
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtUiTools import QUiLoader
import sys
import os

loader = QUiLoader()
app = QtWidgets.QApplication(sys.argv)
window = loader.load("form.ui",None)
window.show()
app.exec_()