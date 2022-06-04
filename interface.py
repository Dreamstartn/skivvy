from Skivvyui import Ui_MainWindow
from PyQt5 import QtGui,QtCore,QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtGui import QMovie
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys

class Gui_Start(QMainWindow):
    def _init__(self):
        super(). init ()
        self.skivvy_gui=Ui_MainWindow()
        self.skivvy_gui.setupUi(self)

      
        self.skivvy_gui.pushButton.clicked.connect(self.startFunc)
        self.skivvy_gui.pushButton_2.clicked.connect(self.close) 
    
    def startFunc(self):    
        self.skivvy_gui.move_1 =QtGui.QMovie("loading_1.gif")
        self.skivvy_gui.load.setMovie(self.skivvy_gui.move_1)
        self.skivvy_gui.move_1.start()
                        
        self.skivvy_gui.move_2 =QtGui.QMovie("s2.gif")
        self.skivvy_gui.label.setMovie(self.skivvy_gui.move_2)
        self.skivvy_gui.move_2.start()
        
        self.skivvy_gui.move_3 =QtGui.QMovie("Earth.gif")
        self.skivvy_gui.label_4.setMovie(self.skivvy_gui.move_3)
        self.skivvy_gui.move_3.start()
        
        self.skivvy_gui.move_4 =QtGui.QMovie("Siri.gif")
        self.skivvy_gui.listen.setMovie(self.skivvy_gui.move_4)
        self.skivvy_gui.move_4.start()
        
       
    
if __name__ == "__main__":     

 Gui_App=QApplication(sys.argv)
 Gui_Skivvy= Gui_Start()
 Gui_Skivvy.show()
 exit(Gui_App.exec_())       