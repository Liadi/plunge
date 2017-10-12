__author__ = 'Omotola'
from customInterfaceWidget import Status
from customInterfaceWidget import State
from customInterfaceWidget import Side
from customInterfaceWidget import Tile
from random import randint

from PyQt4.QtGui import *
from PyQt4.QtCore import *
import sys

class Board(QFrame):
    tiles = []
    def __init__(self, parent = None, height = 0, width = 0, x = 0, y = 0):
        super(Board, self).__init__()

        self.setLineWidth(2)
        self.setFrameStyle(QFrame.Panel | QFrame.Raised)
        self.setParent(parent)
        self.setPosition(x, y)
        self.setDimension(height, width)
        self.graphics()
        self.lbl = QLabel("no",self)
    # def animator(self, sourceTile, targetTile):
    #     movingLabel = QLabel(self)
    #     movingLabel.resize(60, 65)
    #     movingLabel.setPixmap(sourceTile.lbl.pixmap())
    #     movingLabel.move(QLabel(sourceTile.lbl).pos())
    #
    #     animate = QPropertyAnimation(movingLabel,"geometry",self)
    #     animate.setDuration(40000)
    #     animate.setStartValue(QRect(0, 0, 300, 90))
    #     animate.setEndValue(QRect(475, 475, 300, 90))
    #     # animate.setStartValue(QRect(sourceTile.pos(), sourceTile.lbl.size()))
    #     # animate.setEndValue(QRect(targetTile.pos(), targetTile.lbl.size()))
    #     animate.start()


    def graphics(self):
        height, width = self.height(), self.width()
        grid = QGridLayout(self)
        grid.setHorizontalSpacing(0)
        grid.setVerticalSpacing(0)
        targetStartRow = randint(0, 5)
        targetStartCol = randint(0, 6)
        boolTileAllNull = True
        for i in range(0, 10, 1):
            for j in range(0, 10, 1):
                if (i + j) % 2 == 0:
                    lbl = QLabel(self)
                    btn = Tile(i,j, lbl)
                    btn.setMaximumHeight(65)
                    btn.setMaximumWidth(75)
                    if (i == j):
                        btn.setStyleSheet('QPushButton{background-color: red;'
                                      'border-radius:2px}')
                    else:
                        btn.setStyleSheet('QPushButton{background-color: black;'
                                      'border-radius:2px}')


                    if ((i >= targetStartRow and i <= targetStartRow + 4) and (j >= targetStartCol and j <= targetStartCol+3)):
                        x = randint(0,2)
                        if x != 0:
                            boolTileAllNull = False
                        elif Board.tiles.__len__() == 8 and boolTileAllNull:
                            x = randint(1, 2)
                        cellStatus = x
                        btn.setStatus(cellStatus)
                        Board.tiles.append(btn)


                    btn.setIconSize(QSize(50,50))
                    # Board.tiles.append(btn)
                    grid.setContentsMargins(0,0,0,0)
                    grid.setSpacing(0)
                    grid.addWidget(btn, i, j)

                else:
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
        self.setLayout(self.lay)
        self.graphics()


    def graphics(self):
        self.timeFrame = QFrame()
        self.timeFrame.setFixedHeight(self.parent().height() * 0.1)
        self.setFixedWidth(self.parent().width() * 1)
        self.timeFrame.setLineWidth(2)
        self.timeFrame.setFrameStyle(QFrame.Panel | QFrame.Raised)
        self.timeLCD = QLCDNumber()
        self.timeFrameLayout = QVBoxLayout()
        self.timeFrameLayout.addWidget(self.timeLCD)
        self.timeFrame.setLayout(self.timeFrameLayout)



        self.questionFrame = QFrame()
        self.questionFrameArray = []
        self.questionFrame.setLineWidth(2)
        self.questionFrame.setFrameStyle(QFrame.Panel | QFrame.Raised)
        self.questionFrameLayout = QVBoxLayout()
        self.questionFrame.setLayout(self.questionFrameLayout)

        self.questionSideFrame = QFrame()
        self.questionFrameArray.append(self.questionSideFrame)
        self.questionSideFrameLayout = QHBoxLayout()
        self.questionSideFrame.setLayout(self.questionSideFrameLayout)
        self.questionSideLabel = QLabel("Move made by the correct side")
        self.questionSideRadioTrue = QRadioButton("True")
        self.questionSideRadioFalse = QRadioButton("False")
        self.questionSideRadioGroup = QButtonGroup()
        self.questionSideRadioGroup.addButton(self.questionSideRadioTrue, 1)
        self.questionSideRadioGroup.addButton(self.questionSideRadioFalse, 2)
        self.questionSideRadioGroup.buttonClicked.connect(self.radioSideSignal)
        self.connect(self.questionSideRadioGroup, SIGNAL("emittingButtonClicked(QFrame, QButtonGroup)"), self.questionControl)
        self.questionSideFrameLayout.addWidget(self.questionSideLabel)
        self.questionSideFrameLayout.addWidget(self.questionSideRadioTrue)
        self.questionSideFrameLayout.addWidget(self.questionSideRadioFalse)
        self.questionSideRadioFalse.setChecked(True)
        self.questionFrameLayout.addWidget(self.questionSideFrame)


        self.questionForwardFrame = QFrame()
        self.questionFrameArray.append(self.questionForwardFrame)
        self.questionForwardFrameLayout = QHBoxLayout()
        self.questionForwardFrame.setLayout(self.questionForwardFrameLayout)
        self.questionForwardLabel = QLabel("A forward move")
        self.questionForwardRadioTrue = QRadioButton("True")
        self.questionForwardRadioFalse = QRadioButton("False")
        self.questionForwardRadioGroup = QButtonGroup()
        self.questionForwardRadioGroup.addButton(self.questionForwardRadioTrue, 1)
        self.questionForwardRadioGroup.addButton(self.questionForwardRadioFalse, 2)
        self.questionForwardRadioGroup.buttonClicked.connect(self.radioForwardSignal)
        self.connect(self.questionForwardRadioGroup, SIGNAL("emittingButtonClicked(QFrame, QButtonGroup)"), self.questionControl)
        self.questionForwardFrameLayout.addWidget(self.questionForwardLabel)
        self.questionForwardFrameLayout.addWidget(self.questionForwardRadioTrue)
        self.questionForwardFrameLayout.addWidget(self.questionForwardRadioFalse)
        self.questionForwardRadioFalse.setChecked(True)

        self.questionValidForwardFrame = QFrame()
        self.questionFrameArray.append(self.questionValidForwardFrame)
        self.questionValidForwardFrameLayout = QHBoxLayout()
        self.questionValidForwardFrame.setLayout(self.questionValidForwardFrameLayout)
        self.questionValidForwardLabel = QLabel("A valid forward move")
        self.questionValidForwardRadioTrue = QRadioButton("True")
        self.questionValidForwardRadioFalse = QRadioButton("False")
        self.questionValidForwardRadioGroup = QButtonGroup()
        self.questionValidForwardRadioGroup.addButton(self.questionValidForwardRadioTrue, 1)
        self.questionValidForwardRadioGroup.addButton(self.questionValidForwardRadioFalse, 2)
        self.questionValidForwardRadioGroup.buttonClicked.connect(self.radioValidForwardSignal)
        self.connect(self.questionValidForwardRadioGroup, SIGNAL("emittingButtonClicked(QFrame, QButtonGroup)"), self.questionControl)
        self.questionValidForwardFrameLayout.addWidget(self.questionValidForwardLabel)
        self.questionValidForwardFrameLayout.addWidget(self.questionValidForwardRadioTrue)
        self.questionValidForwardFrameLayout.addWidget(self.questionValidForwardRadioFalse)
        self.questionValidForwardRadioFalse.setChecked(True)

        self.questionJumpFrame = QFrame()
        self.questionFrameArray.append(self.questionJumpFrame)
        self.questionJumpFrameLayout = QHBoxLayout()
        self.questionJumpFrame.setLayout(self.questionJumpFrameLayout)
        self.questionJumpLabel = QLabel("Move was a jump")
        self.questionJumpRadioTrue = QRadioButton("True")
        self.questionJumpRadioFalse = QRadioButton("False")
        self.questionJumpRadioGroup = QButtonGroup()
        self.questionJumpRadioGroup.addButton(self.questionJumpRadioTrue, 1)
        self.questionJumpRadioGroup.addButton(self.questionJumpRadioFalse, 2)
        self.questionJumpRadioGroup.buttonClicked.connect(self.radioJumpSignal)
        self.connect(self.questionJumpRadioGroup, SIGNAL("emittingButtonClicked(QFrame, QButtonGroup)"), self.questionControl)
        self.questionJumpFrameLayout.addWidget(self.questionJumpLabel)
        self.questionJumpFrameLayout.addWidget(self.questionJumpRadioTrue)
        self.questionJumpFrameLayout.addWidget(self.questionJumpRadioFalse)
        self.questionJumpRadioFalse.setChecked(True)

        self.questionValidJumpFrame = QFrame()
        self.questionFrameArray.append(self.questionValidJumpFrame)
        self.questionValidJumpFrameLayout = QHBoxLayout()
        self.questionValidJumpFrame.setLayout(self.questionValidJumpFrameLayout)
        self.questionValidJumpLabel = QLabel("Jump was valid")
        self.questionValidJumpRadioTrue = QRadioButton("True")
        self.questionValidJumpRadioFalse = QRadioButton("False")
        self.questionValidJumpRadioGroup = QButtonGroup()
        self.questionValidJumpRadioGroup.addButton(self.questionValidJumpRadioTrue, 1)
        self.questionValidJumpRadioGroup.addButton(self.questionValidJumpRadioFalse, 2)
        self.questionValidJumpRadioGroup.buttonClicked.connect(self.radioValidJumpSignal)
        self.connect(self.questionValidJumpRadioGroup, SIGNAL("emittingButtonClicked(QFrame, QButtonGroup)"), self.questionControl)
        self.questionValidJumpFrameLayout.addWidget(self.questionValidJumpLabel)
        self.questionValidJumpFrameLayout.addWidget(self.questionValidJumpRadioTrue)
        self.questionValidJumpFrameLayout.addWidget(self.questionValidJumpRadioFalse)
        self.questionValidJumpRadioFalse.setChecked(True)

        self.questionOtherValidJumpFrame = QFrame()
        self.questionFrameArray.append(self.questionOtherValidJumpFrame)
        self.questionOtherValidJumpFrameLayout = QHBoxLayout()
        self.questionOtherValidJumpFrame.setLayout(self.questionOtherValidJumpFrameLayout)
        self.questionOtherValidJumpLabel = QLabel("Is there any other tile with a valid jump")
        self.questionOtherValidJumpRadioTrue = QRadioButton("True")
        self.questionOtherValidJumpRadioFalse = QRadioButton("False")
        self.questionOtherValidJumpRadioGroup = QButtonGroup()
        self.questionOtherValidJumpRadioGroup.addButton(self.questionOtherValidJumpRadioTrue, 1)
        self.questionOtherValidJumpRadioGroup.addButton(self.questionOtherValidJumpRadioFalse, 2)
        self.questionOtherValidJumpRadioGroup.buttonClicked.connect(self.radioOtherValidJumpSignal)
        self.connect(self.questionOtherValidJumpRadioGroup, SIGNAL("emittingButtonClicked(QFrame, QButtonGroup)"), self.questionControl)
        self.questionOtherValidJumpFrameLayout.addWidget(self.questionOtherValidJumpLabel)
        self.questionOtherValidJumpFrameLayout.addWidget(self.questionOtherValidJumpRadioTrue)
        self.questionOtherValidJumpFrameLayout.addWidget(self.questionOtherValidJumpRadioFalse)
        self.questionOtherValidJumpRadioFalse.setChecked(True)




        self.answerFrame = QFrame()
        self.answerFrame.setLineWidth(2)
        self.answerFrame.setFrameStyle(QFrame.Panel | QFrame.Raised)
        self.answerFrameLayout = QVBoxLayout()
        self.answerFrame.setLayout(self.answerFrameLayout)

        self.answerSideFrame = QFrame()
        self.answerSideFrameLayout = QHBoxLayout()
        self.answerSideFrame.setLayout(self.answerSideFrameLayout)
        self.answerSideLabel = QLabel("Move made by the correct side")
        self.answerSideRadioTrue = QRadioButton("True")
        self.answerSideRadioFalse = QRadioButton("False")
        self.answerSideFrameLayout.addWidget(self.answerSideLabel)
        self.answerSideFrameLayout.addWidget(self.answerSideRadioTrue)
        self.answerSideFrameLayout.addWidget(self.answerSideRadioFalse)
        self.answerSideRadioFalse.setCheckable(False)
        self.answerSideRadioTrue.setCheckable(False)
        self.answerFrameLayout.addWidget(self.answerSideFrame)


        self.answerFowardFrame = QFrame()
        self.answerForwardFrameLayout = QHBoxLayout()
        self.answerFowardFrame.setLayout(self.answerForwardFrameLayout)
        self.answerForwardLabel = QLabel("A forward move")
        self.answerForwardRadioTrue = QRadioButton("True")
        self.answerForwardRadioFalse = QRadioButton("False")
        self.answerForwardFrameLayout.addWidget(self.answerForwardLabel)
        self.answerForwardFrameLayout.addWidget(self.answerForwardRadioTrue)
        self.answerForwardFrameLayout.addWidget(self.answerForwardRadioFalse)
        self.answerForwardRadioFalse.setCheckable(False)
        self.answerForwardRadioTrue.setCheckable(False)

        self.answerValidForwardFrame = QFrame()
        self.answerValidForwardFrameLayout = QHBoxLayout()
        self.answerValidForwardFrame.setLayout(self.answerValidForwardFrameLayout)
        self.answerValidForwardLabel = QLabel("A valid forward move")
        self.answerValidForwardRadioTrue = QRadioButton("True")
        self.answerValidForwardRadioFalse = QRadioButton("False")
        self.answerValidForwardFrameLayout.addWidget(self.answerValidForwardLabel)
        self.answerValidForwardFrameLayout.addWidget(self.answerValidForwardRadioTrue)
        self.answerValidForwardFrameLayout.addWidget(self.answerValidForwardRadioFalse)
        self.answerValidForwardRadioFalse.setCheckable(False)
        self.answerValidForwardRadioTrue.setCheckable(False)

        self.answerJumpFrame = QFrame()
        self.answerJumpFrameLayout = QHBoxLayout()
        self.answerJumpFrame.setLayout(self.answerJumpFrameLayout)
        self.answerJumpLabel = QLabel("Move was a jump")
        self.answerJumpRadioTrue = QRadioButton("True")
        self.answerJumpRadioFalse = QRadioButton("False")
        self.answerJumpFrameLayout.addWidget(self.answerJumpLabel)
        self.answerJumpFrameLayout.addWidget(self.answerJumpRadioTrue)
        self.answerJumpFrameLayout.addWidget(self.answerJumpRadioFalse)
        self.answerJumpRadioFalse.setCheckable(False)
        self.answerJumpRadioTrue.setCheckable(False)

        self.answerValidJumpFrame = QFrame()
        self.answerValidJumpFrameLayout = QHBoxLayout()
        self.answerValidJumpFrame.setLayout(self.answerValidJumpFrameLayout)
        self.answerValidJumpLabel = QLabel("Jump was valid")
        self.answerValidJumpRadioTrue = QRadioButton("True")
        self.answerValidJumpRadioFalse = QRadioButton("False")
        self.answerValidJumpFrameLayout.addWidget(self.answerValidJumpLabel)
        self.answerValidJumpFrameLayout.addWidget(self.answerValidJumpRadioTrue)
        self.answerValidJumpFrameLayout.addWidget(self.answerValidJumpRadioFalse)
        self.answerValidJumpRadioFalse.setCheckable(False)
        self.answerValidJumpRadioTrue.setCheckable(False)

        self.answerOtherValidJumpFrame = QFrame()
        self.answerOtherValidJumpFrameLayout = QHBoxLayout()
        self.answerOtherValidJumpFrame.setLayout(self.answerOtherValidJumpFrameLayout)
        self.answerOtherValidJumpLabel = QLabel("Is there any other tile with a valid jump")
        self.answerOtherValidJumpRadioTrue = QRadioButton("True")
        self.answerOtherValidJumpRadioFalse = QRadioButton("False")
        self.answerOtherValidJumpFrameLayout.addWidget(self.answerOtherValidJumpLabel)
        self.answerOtherValidJumpFrameLayout.addWidget(self.answerOtherValidJumpRadioTrue)
        self.answerOtherValidJumpFrameLayout.addWidget(self.answerOtherValidJumpRadioFalse)

        self.answerOtherValidJumpRadioTrue.setCheckable(False)
        self.answerOtherValidJumpRadioFalse.setCheckable(False)


        self.sidePickerFrame = QFrame()
        self.sidePickerFrame.setLineWidth(2)
        self.sidePickerFrame.setFrameStyle(QFrame.Panel | QFrame.Raised)
        self.sidePickerFrameLayout = QVBoxLayout()
        self.sidePickerFrame.setLayout(self.sidePickerFrameLayout)
        self.aboveSideLabel = QLabel()
        self.belowSideLabel = QLabel()

        self.aboveSideLabel.resize(50,50)
        self.belowSideLabel.resize(50,50)

        self.sidePickerFrameLayout.addWidget(self.aboveSideLabel)
        self.sidePickerFrameLayout.addWidget(self.belowSideLabel)
        pix = QPixmap("C:/Users/Omotola/Downloads/others/Play-icon1.png")
        pix = pix.scaled(self.aboveSideLabel.size(), Qt.KeepAspectRatio)
        self.aboveSideLabel.setPixmap(pix)
        pix = QPixmap("C:/Users/Omotola/Downloads/others/Start-icon.png")
        pix = pix.scaled(self.belowSideLabel.size(), Qt.KeepAspectRatio)
        self.belowSideLabel.setPixmap(pix)


        self.menuFrame = QFrame()
        self.menuFrame.setLineWidth(2)
        self.menuFrame.setFrameStyle(QFrame.Panel | QFrame.Raised)
        self.menuFrameLayout = QVBoxLayout()
        self.menuFrame.setLayout(self.menuFrameLayout)
        # self.menuUpperFrame = QFrame(self.menuFrame)
        # self.menuLowerFrame = QFrame(self.menuFrame)
        self.menuLowerFrameLayout = QHBoxLayout()
        self.menuUpperFrameLayout = QHBoxLayout()
        self.menuFrameLayout.addLayout(self.menuUpperFrameLayout)
        self.menuFrameLayout.addLayout(self.menuLowerFrameLayout)
        self.regenerateBtn = QToolButton()
        self.menuUpperFrameLayout.addWidget(self.regenerateBtn)
        self.advanceBtn = QToolButton()
        self.connect(self.advanceBtn, SIGNAL("clicked()"), self.anim)
        self.menuUpperFrameLayout.addWidget(self.advanceBtn)
        self.menuBtn = QToolButton()
        self.menuLowerFrameLayout.addWidget(self.menuBtn)


        self.lay.addWidget(self.timeFrame)
        self.lay.addWidget(self.questionFrame)
        # self.lay.addWidget(self.answerFrame)

        self.lastLayout = QHBoxLayout()
        self.lastLayout.addWidget(self.sidePickerFrame)
        self.lastLayout.addWidget(self.menuFrame)


        self.lay.addLayout(self.lastLayout)

    def radioSideSignal(self):
        print("already Side")
        self.questionSideRadioGroup.emit(SIGNAL("emittingButtonClicked(QFrame, QButtonGroup)"), self.questionSideFrame, self.questionSideRadioGroup)

    def radioForwardSignal(self):
        print("already forward")
        self.questionForwardRadioGroup.emit(SIGNAL("emittingButtonClicked(QFrame, QButtonGroup)"), self.questionForwardFrame, self.questionForwardRadioGroup)

    def radioValidForwardSignal(self):
        print("already Valid forward")
        self.questionValidForwardRadioGroup.emit(SIGNAL("emittingButtonClicked(QFrame, QButtonGroup)"), self.questionValidForwardFrame, self.questionValidForwardRadioGroup)

    def radioJumpSignal(self):
        print("already")
        self.questionJumpRadioGroup.emit(SIGNAL("emittingButtonClicked(QFrame, QButtonGroup)"), self.questionJumpFrame, self.questionJumpRadioGroup)

    def radioValidJumpSignal(self):
        print("already")
        self.questionValidJumpRadioGroup.emit(SIGNAL("emittingButtonClicked(QFrame, QButtonGroup)"), self.questionValidJumpFrame, self.questionValidJumpRadioGroup)

    def radioOtherValidJumpSignal(self):
        print("already")
        self.questionOtherValidJumpRadioGroup.emit(SIGNAL("emittingButtonClicked(QFrame, QButtonGroup)"), self.questionOtherValidJumpFrame, self.questionOtherValidJumpRadioGroup)

    def questionControl(self, e, btnGrp):
        print("children ",self.questionFrame.children().__len__())
        childIndex = self.questionFrame.children().index(e)
        print("childIndex", childIndex)
        id = btnGrp.checkedId()
        if id == 1:
            self.questionFrameLayout.addWidget(self.questionFrameArray[childIndex])
            self.questionFrameArray[childIndex].setParent(self.questionFrame)
        elif self.questionFrame.children().__len__() > childIndex:
            for i in range(childIndex, self.questionFrame.children().__len__() - 1):
                print("i is ", i)
                self.questionFrameArray[i].children()[3].setChecked(True)
                self.questionFrameArray[i].setParent(None)



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

    def anim(self):
        print("got in anim")
        status = randint(1, 2)
        sourceTile = None
        targetTile = None
        i = 0
        j = 0
        k = 0
        targetStatus = 0
        while i < Board.tiles.__len__():
            print("BoardTileStatus: ", Board.tiles[i].getStatus(),"| i: ", i, "| targetStatus: ", targetStatus, "| SourceStatus: ", status, "| targetTile: ", targetTile, "| sourceTile: ", sourceTile)
            if sourceTile != None and targetTile != None:
                if sourceTile == targetTile:
                    if Board.tiles.index(sourceTile) <= 4:
                        sourceTile = Board.tiles[Board.tiles.index(sourceTile) + 2]
                    else:
                        targetTile = Board.tiles[Board.tiles.index(sourceTile) - 2]
                break
            elif status == Board.tiles[i].getStatus() and sourceTile == None:
                print("b")
                if Board.tiles[i].getStatus() != 0:
                    sourceTile = Board.tiles[i]
                i += 1
                continue
            elif Board.tiles[i].getStatus() == targetStatus and targetTile == None:
                print("c")
                targetTile = Board.tiles[i]
                i += 1
                continue

            if Board.tiles.__len__() - i ==  1:
                if sourceTile == None and j < 3:
                    status = (status % 2) + 1
                    i = 0
                    j += 1

                elif targetTile == None and k < 3:
                    if targetStatus == 0:
                        targetStatus += 1
                    else:
                        targetStatus = (targetStatus % 2) + 1
                    i = 0
                    k += 1

                else:
                    raise EnvironmentError
                    break

            else:
                i += 1
                continue

        print("target: ", targetTile.getMatrix(), ", source: ", sourceTile.getMatrix())

        lbl = mainAppObject.boardObject.lbl
        lbl.setPixmap(QPixmap(sourceTile.lbl.pixmap()))

        animate = QPropertyAnimation(lbl,"geometry",self)
        animate.setDuration(2000)
        # animate.setStartValue(QRect(0, 0, 300, 90))
        # animate.setEndValue(QRect(475, 475, 300, 90))
        animate.setStartValue(QRect(sourceTile.pos(), sourceTile.lbl.size()))
        animate.setEndValue(QRect(targetTile.pos(), targetTile.lbl.size()))
        animate.start()
        sourceTile.lbl.setPixmap(QPixmap(""))
        targetTile.lbl.setPixmap(QPixmap(sourceTile.lbl.pixmap()))



class Tile(QPushButton):

    def __init__(self, row, col, lbl):
        super(Tile, self).__init__()
        self.setAcceptDrops(True)
        self.row = row
        self.col = col
        self.lbl = lbl
        self.lbl.resize(60, 65)
        self.lbl.setParent(self)

    def getIcon(self):
       return self.icon()

    def _setIcon(self, pixMap):
        #self.lbl.move(self.row * self.width(), self.col * self.height())
        pix = pixMap.scaled(self.lbl.size(), Qt.KeepAspectRatio)
        self.lbl.setPixmap(pix)



        #self.setIcon(QIcon(pixMap))

    def getMatrix(self):
        return self.row, self.col


    def getStatus(self):
        return self.status

    def setStatus(self, status):
        self.status = status
        if self.getStatus() == 1:
            tile = QPixmap("C:/Users/Omotola/Downloads/others/Start-icon.png")

            self._setIcon(tile)
        elif self.getStatus() == 2:
            tile = QPixmap("C:/Users/Omotola/Downloads/others/Play-icon1.png")
            self._setIcon(tile)

    def getState(self):
        return self.state

    def setState(self, state):
        self.state = state


class Interface (QMainWindow):
    def __init__(self):
        super(Interface, self).__init__()
        self.setGeometry(QDesktopWidget().screenGeometry())
        height = self.height() - self.height() * 0.035
        width = self.width() - self.width() * 0
        self.boardObject = Board(parent=self, height=height * 0.8, width=width * 0.5, x=width * 0.05, y=height * 0.08)
        self.sideObj = SideBoard(parent=self, height=height * 0.81, width=width * 0.49, x=width * 0.55, y=height * 0)
        self.connect(self,SIGNAL("resize()"),self.updateSize)
        self.updateSize()
        self.ui()

    def resizeEvent(self, QResizeEvent):
        self.emit(SIGNAL("resize()"))
    def updateSize(self):
        height = self.height() - self.height() * 0.035
        width = self.width()
        self.boardObject.setDimension(height=height * 0.9, width=width * 0.55)
        self.boardObject.setPosition(length=width * 0.05, depth=height * 0.08)
        self.sideObj.setDimension(height=height * 0.98, width=width * 0.4)
        self.sideObj.setPosition(length=width * 0.6, depth=height * 0)

    def ui(self):
        self.showMaximized()
        self.show()

app = QApplication(sys.argv)
mainAppObject = Interface()
sys.exit(app.exec_())