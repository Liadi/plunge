__author__ = 'Omotola'
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from enum import Enum
from math import floor
import logic

class NameBar(QLabel):
    def __init__(self, parent, height, width, x = 0, y = 0):
        super(NameBar, self).__init__()
        self.setParent(parent)
        self.graphics()

        self.setPosition(x, y)
        self.setDimension(height, width)

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

    def graphics(self):
        pass

class SideBar(QFrame):
    def __init__(self, parent, height, width, x = 0, y = 0):
        super(SideBar, self).__init__()
        self.setParent(parent)
        self.graphics()
        self.setPosition(x, y)
        self.setDimension(height, width)

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

    def graphics(self):
        pass

class Status(Enum):
    void = 0
    source = 1
    target = 2

class State(Enum):
    live = 1
    dead = 2

class Side(Enum):
    A = 1
    B = 2

class Tile(QPushButton):

    def __init__(self, i, parent):
        super(Tile, self).__init__()
        if(i ==  -1 and parent == None):
            return
        else:
            self.controlinit(i,parent)

    def controlinit(self, i, parent):
        self.i = i
        self.retained = False#in place of Enum to show play must be enforced on this Tile
        self.setParent(parent)
        self.setAcceptDrops(True)

        self.state = State.dead
        self.status = Status.void
        j = i % 10
        self.column = (j * 2) % 10 + floor(j/5)
        self.row = floor(i/5)

    def getIcon(self):
       return self.icon()

    def _setIcon(self, pixMap):
        self.setIcon(QIcon(pixMap))

    def getMatrix(self):
        return self.row, self.column


    def getStatus(self):
        return self.status

    def setStatus(self, status):
        self.status = status

    def getState(self):
        return self.state

    def setState(self, state):
        self.state = state

    def getDescription(self):
        return self.getMatrix(), self.getState(), self.getStatus()

    def mouseMoveEvent(self, e):
        if (e.buttons() != Qt.LeftButton) or (self.getState() != State.live):
            return
        boardObj = Board()
        if boardObj.enforceTile >= 0 and boardObj.enforceTile <= 49:
            if boardObj.enforceTile != self.i:
                return
            else:
                pass    #enforce chop on a particular tile

        icon = self.icon()

        mimeData = QMimeData()
        mimeData.setText(str(self.i))

        self.drag = QDrag(self)
        self.drag.setMimeData(mimeData)
        self.drag.setPixmap(icon.pixmap(QSize(50, 50)))

        #dropAction = self.drag.startQt.MoveAction
        self.drag.start()

    def dragEnterEvent(self, e):
        e.accept()

    def dropEvent(self, e):
        i = int(e.mimeData().text())
        source = Board.tileArray[i]
        target = self

        place = logic.Decision()
        returned = place.main(source=source, target=target)
        if returned[0]:
            if returned[1] >= 0 and returned[1] <= 49:
                boardObj = Board()
                boardObj.enforceTile = returned[1]
            else:
                try:
                    Interface.side = 2 / Interface.side.value
                    place.control(Side(Interface.side))
                except AttributeError:
                    Interface.side = 2 / Interface.side
                    place.control(Side(Interface.side))

class SpecificBtn(QToolButton):
    def __init__(self, image, height, width, parent):
        super(SpecificBtn, self).__init__()
        self.setParent(parent)
        self.setMaximumHeight(height)
        self.setMaximumWidth(width)
        self.setIcon(QIcon(image))
        self.setUi()

    def setUi(self):
        pass

class Piece(QPushButton):
    def __init__(self, colour):
        super(Piece, self).__init__()

        self.graphics()

    def graphics(self):
        pass

class King(Piece):
    def __init__(self, parent):
        super(King,self).__init__()
        self.setParent(parent)

        self.graphics()

    def graphics(self):
        pass

class Board(QFrame):
    tileArray = []
    enforceTile = -1
    def __init__(self, parent = None, height = 0, width = 0, x = 0, y = 0):
        super(Board, self).__init__()

        self.setLineWidth(2)
        self.setFrameStyle(QFrame.Panel | QFrame.Raised)
        self.setParent(parent)
        self.graphics()
        self.setPosition(x, y)
        self.setDimension(height, width)

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

    def graphics(self):

        height, width = self.height(), self.width()
        grid = QGridLayout(self)
        grid.setHorizontalSpacing(0)
        grid.setVerticalSpacing(0)

        for i in range(0, 10, 1):
            for j in range(0, 10, 1):
                if (i + j) % 2 == 0:

                    btn = Tile(i = self.tileArray.__len__(),parent = self)
                    self.tileArray.append(btn)
                    btn.setMaximumHeight(65)
                    btn.setMaximumWidth(75)
                    if (i == j):
                        btn.setStyleSheet('QPushButton{background-color: red;'
                                      'border-radius:2px}')
                    else:
                        btn.setStyleSheet('QPushButton{background-color: black;'
                                      'border-radius:2px}')
                    if 0 <= btn.row and btn.row <= 3:
                        btn.setStatus(Status.target)
                        tile = QPixmap("C:/Users/Omotola/Downloads/others/Play-icon1.png")
                        btn._setIcon(tile)

                    elif 6 <= btn.row and btn.row <= 9:
                        btn.setStatus(Status.source)
                        tile = QPixmap("C:/Users/Omotola/Downloads/others/Start-icon.png")
                        btn._setIcon(tile)

                    btn.setIconSize(QSize(50,50))
                    grid.setContentsMargins(0,0,0,0)
                    grid.setSpacing(0)
                    grid.addWidget(btn, i, j)

                else:
                    continue

class Track(QFrame):
    def __init__(self, parent, height, width, x = 0, y = 0):
        super(Track, self).__init__()
        self.setParent(parent)
        self.graphics()
        self.setPosition(x, y)
        self.setDimension(height, width)
        self.lay = QHBoxLayout(self)
        self.resetButton = SpecificBtn(image = QPixmap("C:/Users/Omotola/Pictures/snipping/XPUTER.jpg"), height = self.height() * 0.8, width = self.height() * 2, parent = self)
        self.resetButton.setIconSize(QSize(50,50))
        self.backTrackButton = SpecificBtn(image = QPixmap("C:/Users/Omotola/Pictures/snipping/images(2).png"), height = self.height() * 0.8, width = self.height() * 2, parent = self)
        self.backTrackButton.setIconSize(QSize(50,50))
        self.lay.addWidget(self.resetButton)
        self.lay.addWidget(self.backTrackButton)
        self.setLayout(self.lay)

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

    def graphics(self):
        pass

class Control(QFrame):
    def __init__(self, parent, height, width, x = 0, y = 0):
        super(Control, self).__init__()
        self.setParent(parent)

        self.graphics()
        self.setPosition(x, y)
        self.setDimension(height, width)

        self.lay = QHBoxLayout(self)
        self.stopButton = SpecificBtn(image = QPixmap("C:/Users/Omotola/Pictures/snipping/XPUTER.jpg"), height = self.height() * 0.8, width = self.height() * 0.8, parent = self)
        self.stopButton.setIconSize(QSize(50,50))
        self.pauseButton = SpecificBtn(image = QPixmap("C:/Users/Omotola/Pictures/snipping/images(2).png"), height = self.height() * 0.8, width = self.height() * 0.8, parent = self)
        self.pauseButton.setIconSize(QSize(50,50))
        self.lay.addWidget(self.stopButton)
        self.lay.addWidget(self.pauseButton)


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

    def graphics(self):
        pass
        #self.show()

class ScoreBoard(QFrame):
    def __init__(self, parent, height, width, x = 0, y = 0):
        super(ScoreBoard, self).__init__()
        self.setParent(parent)
        self.graphics()
        self.setPosition(x, y)
        self.setDimension(height, width)

        self.vertical = QVBoxLayout(self)
        self.grid = QGridLayout(self)
        self.horizontal = QHBoxLayout(self)
        self.playerOneLabel = QLabel(self)
        self.playerTwoLabel = QLabel(self)
        self.playerOneImage = QLabel(self)
        self.playerTwoImage =QLabel(self)
        self.playerOneLCD = QLCDNumber(2, self)
        self.playerTwoLCD = QLCDNumber(2, self)
        self.playerOneTurn = QLabel(self)
        self.playerTwoTurn = QLabel(self)

        self.playerOneTurn.setMaximumHeight((self.width() / 2) - 100)
        self.playerTwoTurn.setMaximumHeight((self.width() / 2) - 100)
        self.playerOneLabel.setMaximumHeight(self.width() / 6)
        self.playerTwoLabel.setMaximumHeight(self.width() / 6)

        self.horizontal.addWidget(self.playerOneTurn)
        self.horizontal.addWidget(self.playerTwoTurn)
        self.grid.addWidget(self.playerOneLabel, 0, 0)
        self.grid.addWidget(self.playerTwoLabel, 0, 1)
        self.grid.addWidget(self.playerOneImage, 1, 0)
        self.grid.addWidget(self.playerTwoImage, 1, 1)
        self.grid.addWidget(self.playerOneLCD, 2, 0)
        self.grid.addWidget(self.playerTwoLCD, 2, 1)

        self.vertical.addLayout(self.grid)
        self.vertical.addLayout(self.horizontal)

        self.setLayout(self.vertical)
        for child in self.children():
            try:
                child.setLineWidth(2)
                child.setFrameStyle(QFrame.Panel | QFrame.Raised)
            except:
                continue
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




    def graphics(self):
        pass

class Interface (QMainWindow):
    side = Side.A
    def __init__(self):
        super(Interface, self).__init__()
        self.setGeometry(QDesktopWidget().screenGeometry())
        self.connect(self,SIGNAL("resize()"),self.updateSize)
        height = self.height() - self.height() * 0.035
        width = self.width() - self.width() * 0
        self.sideBarObject = SideBar(parent = self, height = height * 1.0, width = width * 0.197)
        self.nameBarObject = NameBar(parent = self, height = height * 0.09, width = width * 0.8)
        self.boardObject = Board(parent = self, height = height * 0.79, width = width * 0.5)
        self.scoreBoardObject = ScoreBoard(parent = self, height = height * 0.79, width = width * 0.3)
        self.trackObject = Track(parent = self, height = height * 0.12, width = width * 0.5)
        self.controlObject = Control(parent = self, height = height * 0.12, width = width * 0.3)

        self.updateSize()

        self.ui()

    def resizeEvent(self, QResizeEvent):
        self.emit(SIGNAL("resize()"))

    def updateSize(self):
        height = self.height() - self.height() * 0.005
        width = self.width() - self.width() * 0
        self.sideBarObject.setDimension(height = height * 1.0, width = width * 0.197)
        self.nameBarObject.setDimension(height = height * 0.09, width = width * 0.8)
        self.boardObject.setDimension(height = height * 0.79, width = width * 0.5)
        self.scoreBoardObject.setDimension(height = height * 0.79, width = width * 0.3)
        self.trackObject.setDimension(height = height * 0.12, width = width * 0.5)
        self.controlObject.setDimension(height = height * 0.12, width = width * 0.3)
        x,y,z = 0, 0, 0
        array = []
        for child in self.children():
            try:
                #child.setLineWidth(0)
                child.setFrameStyle(QFrame.Panel | QFrame.Raised)
                array.append(child)
            except:
                continue
        array[0].setPosition(0,0)
        a,b = array[0].getDimension()
        array[1].setPosition(a,0)
        i,j = array[1].getPosition()
        a,b = array[1].getDimension()
        array[2].setPosition(i, j + b)
        i,j = array[2].getPosition()
        a,b = array[2].getDimension()
        array[3].setPosition(i + a, j)
        array[4].setPosition(i, j + b)
        i,j = array[4].getPosition()
        a,b = array[4].getDimension()
        array[5].setPosition(i + a, j)

    def ui(self):
        self.showMaximized()
        self.show()
