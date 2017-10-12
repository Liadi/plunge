__author__ = 'Omotola'
from PyQt4.QtGui import *
from PyQt4.QtCore import *
import sys
import ui_mainMenu

class MainMenu(QMainWindow, ui_mainMenu.Ui_MainWindow):
    def __init__(self, parent = None):
        super(MainMenu, self).__init__(parent)
        #self.setGeometry(300, 150, 650, 450)
        self.setupUi(self)
        self.graphics()

    def graphics(self):
        # self.
        pass

        self.show()


app = QApplication(sys.argv)
mainAppObject = MainMenu()
sys.exit(app.exec_())
