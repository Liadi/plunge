__author__ = 'Omotola'
#from PyQt4.QtCore import *
from PyQt4.QtGui import *
from enum import Enum
#from math import floor
import sys
import customInterfaceWidget
import logic

class GameMode(Enum):
    Poser = 0
    Single = 1
    Double = 2

class InterfaceSub(customInterfaceWidget.Interface):
    def __init__(self):
        super(InterfaceSub, self).__init__()
        gameMode = GameMode.Single
        logic.Decision().control(self.side)
        self.main()

    def main(self):
        pass




app = QApplication(sys.argv)
mainAppObject = InterfaceSub()

sys.exit(app.exec_())
