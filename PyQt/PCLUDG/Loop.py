__author__ = 'Omotola'
from PyQt4.QtGui import *
import sys
import Poser

class InterfaceSub(Poser.Interface):
    def __init__(self):
        super(InterfaceSub, self).__init__()
        self.main()

    def main(self):
        pass




app = QApplication(sys.argv)
mainAppObject = InterfaceSub()

sys.exit(app.exec_())