__author__ = 'Omotola'
__author__ = 'Omotola'
from customInterfaceWidget import Status
from customInterfaceWidget import State
from customInterfaceWidget import Side
from customInterfaceWidget import Tile

from PyQt4.QtGui import *
from PyQt4.QtCore import *
import sys

class Board(QFrame):
    tileArray = []
    def __init__(self, parent = None, height = 0, width = 0, x = 0, y = 0):
        super(Board, self).__init__()

        self.setLineWidth(2)
        self.setFrameStyle(QFrame.Panel | QFrame.Raised)
        self.setParent(parent)
        #self.graphics()
        self.setPosition(x, y)
        self.setDimension(height, width)
        self.lay = QVBoxLayout(self)

    def setPosition(self,length, depth):
        self.length = length
        self.depth = depth
        self.move(length,depth)

    def getPosition(self):
        return self.length, self.depth

    def setDimension(self, height, width):
        self.setFixedHeight(height)
        self.setFixedWidth(width)

    def getDimension(self):
        return self.width(),self.height()

class PositionFrame(QFrame):
    def __init__(self, parent, width, height, x, y, m, n):
        super(PositionFrame, self).__init__()
        self.setLineWidth(2)
        self.setFrameStyle(QFrame.Panel | QFrame.Raised)
        self.setParent(parent)
        self.setPosition(x, y)
        self.setDimension(height, width)
        grid = QGridLayout(self)
        grid.setHorizontalSpacing(3)
        grid.setVerticalSpacing(3)
        grid.setContentsMargins(0,0,0,0)
        for i in range(0, m, 1):
            for j in range(0, n, 1):
                btn = Tile()
                if m < n:
                    btn.setMaximumHeight(65)
                    btn.setMaximumWidth(75)
                else:
                    btn.setMaximumHeight(75)
                    btn.setMaximumWidth(65)
                btn.setStyleSheet('QPushButton{border-radius:3px}')
                grid.addWidget(btn, i,j)



    def setPosition(self,length, depth):
        self.length = length
        self.depth = depth
        self.move(length,depth)

    def getPosition(self):
        return self.length, self.depth

    def setDimension(self, height, width):
        self.setFixedHeight(height)
        self.setFixedWidth(width)

    def getDimension(self):
        return self.width(),self.height()

class SideBoard(QFrame):
    def __init__(self, parent, width, height, x, y):
        super(SideBoard, self).__init__()
        self.setLineWidth(2)
        self.setFrameStyle(QFrame.Panel | QFrame.Raised)
        self.setParent(parent)
        self.setPosition(x, y)
        self.setDimension(height, width)
        self.lay = QVBoxLayout(self)

    def setPosition(self,length, depth):
        self.length = length
        self.depth = depth
        self.move(length,depth)

    def getPosition(self):
        return self.length, self.depth

    def setDimension(self, height, width):
        self.setFixedHeight(height)
        self.setFixedWidth(width)

    def getDimension(self):
        return self.width(),self.height()

class Tile(QPushButton):

    def __init__(self):
        super(Tile, self).__init__()
        self.setAcceptDrops(True)

    def dragEnterEvent(self, e):
        e.accept()

    def dropEvent(self, e):
        i = e.mimeData().text()
        print(i)

class Interface (QMainWindow):
    def __init__(self):
        super(Interface, self).__init__()
        self.setGeometry(QDesktopWidget().screenGeometry())
        height = self.height() - self.height() * 0.035
        width = self.width() - self.width() * 0
        self.boardObject = Board(parent=self, height=height * 0.8, width=width * 0.5, x=width * 0.05, y=height * 0.08)
        self.colFrameObj = PositionFrame(parent=self, height=height * 0.01, width=width * 0.5, x=width * 0.05, y=height * 0.0, m=1, n=10)
        self.rowFrameObj = PositionFrame(parent=self, height=height * 0.8, width=width * 0.01, x=width * 0, y=height * 0.08, m=10, n=1)
        for i in range(1, self.colFrameObj.children().__len__(), 1):
            self.colFrameObj.children()[i].setStyleSheet('QPushButton{background-color:pink}')
            self.rowFrameObj.children()[i].setStyleSheet('QPushButton{background-color:yellow}')

        #self.playMove = Tile(i= -1, parent=self)

        self.playMove = QPushButton(self)
        self.playMove.setGeometry(0,0,width * 0.05, height * 0.08)
        tile = QPixmap("C:/Users/Omotola/Downloads/PyQT4 saved tutorial pages/Play-icon1.png")
        self.playMove.setIcon(QIcon(tile))
        self.playMove.setIconSize(QSize(50,50))
        self.playMove.setStyleSheet('QPushButton{background-color:white}')
        self.sideObj = SideBoard(parent=self, height=height * 0.81, width=width * 0.49, x=width * 0.55, y=height * 0)

        self.connect(self,SIGNAL("resize()"),self.updateSize)
        self.updateSize()
        self.ui()




    def resizeEvent(self, QResizeEvent):
        self.emit(SIGNAL("resize()"))
    def updateSize(self):
        height = self.height() - self.height() * 0.035
        width = self.width()
        self.playMove.setGeometry(0,0,width * 0.05, height * 0.08)
        self.boardObject.setDimension(height=height * 0.9, width=width * 0.55)
        self.boardObject.setPosition(length=width * 0.05, depth=height * 0.08)
        self.colFrameObj.setDimension(height=height * 0.08, width=width * 0.55)
        self.colFrameObj.setPosition(length=width * 0.05, depth=height * 0)
        self.rowFrameObj.setDimension(height=height * 0.9, width=width * 0.05)
        self.rowFrameObj.setPosition(length=width * 0, depth=height * 0.08)
        self.sideObj.setDimension(height=height * 0.98, width=width * 0.4)
        self.sideObj.setPosition(length=width * 0.6, depth=height * 0)
        #self.colFrameObj.grid.addWidget()

    def ui(self):
        self.showMaximized()
        self.show()
