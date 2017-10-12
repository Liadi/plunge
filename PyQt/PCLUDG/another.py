__author__ = 'Omotola'

import sys
from PyQt4.QtGui import *
from  PyQt4.QtCore import *

class Example(QWidget):

    def __init__(self):
        super(Example, self).__init__()
        self.setGeometry(300, 300, 280, 270)
        self.setWindowTitle('Pen styles')
        self.initUI()

    def initUI(self):
        btn = QPushButton(self)
        data = ""
        f = open("condi_ss.stylesheet", 'r')
        data = f.read()
        f.close()
        self.show()
        btn.setStyleSheet(data)
        self.show()



def main():

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()