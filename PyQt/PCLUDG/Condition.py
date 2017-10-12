__author__ = 'Omotola'
from PyQt4.QtGui import *
from PyQt4.QtCore import *
import sys
import PoserOne
from enum import Enum
from random import randint


class Level(Enum):
    Easy = 1
    Medium = 2
    Hard = 3

class InterfaceSub(PoserOne.Interface):
    score = 0
    level = Level.Easy
    def __init__(self):
        super(InterfaceSub, self).__init__()
        self.main()

    def main(self):
        self.boardObject.lay.addWidget(MainBoard())
        self.sdb = SideBoard(parent= self.sideObj)
        self.sideObj.lay.addWidget(self.sdb)




class MainBoard(QFrame):
    tiles = []
    def __init__(self):
        super(MainBoard, self).__init__()

        self.setLineWidth(2)
        self.graphics()
    def graphics(self):

        height, width = self.height(), self.width()
        grid = QGridLayout(self)
        grid.setHorizontalSpacing(0)
        grid.setVerticalSpacing(0)

        for i in range(0, 10, 1):
            for j in range(0, 10, 1):
                if (i + j) % 2 == 0:

                    btn = PositionTile(i,j)
                    btn.setMaximumHeight(65)
                    btn.setMaximumWidth(75)
                    btn.setStyleSheet('QPushButton{background-color: black;'
                                      'border-radius:2px}')

                    btn.setIconSize(QSize(50,50))
                    MainBoard.tiles.append(btn)
                    grid.setContentsMargins(0,0,0,0)
                    grid.setSpacing(0)
                    grid.addWidget(btn, i, j)

                else:
                    continue


class PositionTile(QPushButton):

    def __init__(self, row, col):
        super(PositionTile, self).__init__()
        self.setAcceptDrops(True)
        self.row = row
        self.col = col

class BoolBtn(QPushButton):

    def __init__(self,name):
        self.name = name
        #print(self.objectName())
        super(BoolBtn, self).__init__()
        self.connect(self,SIGNAL("clicked()"),self.btnClicked)
        self.connect(self, SIGNAL("boolDecider(QPushButton)"),self.decidingSignal)

    def btnClicked(self):
        self.emit(SIGNAL("boolDecider(QPushButton)"), self)

    def decidingSignal(self, place):
        if SideBoard.played:
            print("\t\t",SideBoard.outcome,"\t\t",place.name)
            if SideBoard.outcome == place.name:
                print("correct")
            else:
                print("wrong")

            SideBoard.outcome = False
            SideBoard.setUp(mainAppObject.sdb)


class SideBoard(QFrame):
    f = open('condition', 'r')
    line = (f.readlines()).copy()
    onlyTile, tileOne, tileTwo = None, None, None
    f.close()
    played = False
    outcome = False
    def __init__(self, parent = None):
        super(SideBoard, self).__init__()
        self.setParent(parent)

        self.lay = QVBoxLayout()
        self.timerLCD = QLCDNumber()
        self.booleanFrame = QFrame()
        self.controlFrame = QFrame()

        self.txtBrowserFrame = QFrame()
        self.txtBrowser = QTextBrowser()
        self.txtlay = QVBoxLayout()
        self.txtlay.addWidget(self.txtBrowser)
        self.txtBrowserFrame.setLayout(self.txtlay)

        self.txtBrowserFrame.setLineWidth(2)
        self.txtBrowserFrame.setFrameStyle(QFrame.Panel | QFrame.Raised)


        self.booleanFrame.setLineWidth(2)
        self.booleanFrame.setFrameStyle(QFrame.Panel | QFrame.Raised)

        booleanFrameLay = QHBoxLayout()

        self.trueBtn =  BoolBtn(True)

        self.falseBtn = BoolBtn(False)

        booleanFrameLay.addWidget(self.trueBtn)
        booleanFrameLay.addWidget(self.falseBtn)

        self.booleanFrame.setLayout(booleanFrameLay)


        controlFrameLay = QGridLayout()

        self.playBtn = QPushButton("play")
        self.playBtn.clicked.connect(self.play)

        self.menuBtn = QPushButton("menu")
        self.menuBtn.clicked.connect(self.menu)

        controlFrameLay.addWidget(self.playBtn)
        controlFrameLay.addWidget(self.menuBtn)
        self.controlFrame.setLayout(controlFrameLay)



        self.controlFrame.setLineWidth(2)
        self.controlFrame.setFrameStyle(QFrame.Panel | QFrame.Raised)

        self.booleanFrame.setFixedHeight(self.parent().height() * 0.25)
        self.txtBrowserFrame.setFixedHeight(self.parent().height() * 0.25)

        self.lay.addWidget(self.timerLCD)
        self.lay.addWidget(self.txtBrowserFrame)
        self.lay.addWidget(self.booleanFrame)
        self.lay.addWidget(self.controlFrame)
        self.setLayout(self.lay)
        self.txtBrowser.setText(SideBoard.line[0])
        self.txtBrowser.append(SideBoard.line[1])
        #self.setUp()

    def play(self):
        if not(SideBoard.played):
            SideBoard.played = True
            self.setUp()


    def menu(self):
        pass

    def setUp(self):

        for i in MainBoard.tiles:
            i.setStyleSheet('QPushButton{background-color: black;'
                                      'border-radius:2px}')
        if InterfaceSub.level == Level.Easy:
            fileDeterminate = randint(0,0)
            if fileDeterminate == 0:
                #generate one Tile
                fileGenerate = randint(2,6)
                SideBoard.onlyTile = MainBoard.tiles[randint(0,49)]
                whole = (SideBoard.line[fileGenerate].strip()).split("@")
                txt, bool, perm = whole[0], whole[1], whole[2]
                self.txtBrowser.setText(txt)
                print("\n\nrow:",SideBoard.onlyTile.row ,"\tcol:",SideBoard.onlyTile.col, "\t\t", bool)
                print("bool is",bool)

                if bool == "0":
                    if SideBoard.onlyTile.row > SideBoard.onlyTile.col:
                        print("got in 0")
                        SideBoard.outcome = True

                elif bool == "1":
                    if SideBoard.onlyTile.row < SideBoard.onlyTile.col:
                        print("got in 1")
                        SideBoard.outcome = True

                elif bool == "2":
                    if SideBoard.onlyTile.row >= SideBoard.onlyTile.col:
                        print("got in 2")
                        SideBoard.outcome = True

                elif bool == "3":
                    if SideBoard.onlyTile.row <= SideBoard.onlyTile.col:
                        print("got in 3")
                        SideBoard.outcome = True

                elif bool == "4":
                    if SideBoard.onlyTile.row == SideBoard.onlyTile.col:
                        print("got in 4")
                        SideBoard.outcome = True

                # if bool.__len__() == 3:
                #     if bool[1] == "0":#greater than or equal to
                #         if SideBoard.onlyTile.row >= SideBoard.onlyTile.col:
                #             print("greater than or equal to")
                #             SideBoard.outcome = True
                #     elif SideBoard.onlyTile.row <= SideBoard.onlyTile.col:#less than or equal to
                #         print("less than or equal to")
                #         SideBoard.outcome = True
                #
                # elif bool.__len__() == 2:
                #     if bool[0] == "1":
                #         if SideBoard.onlyTile.row > SideBoard.onlyTile.col:
                #             print("greater than")
                #             SideBoard.outcome = True
                #     elif bool[1] == "0":
                #         if SideBoard.onlyTile.row == SideBoard.onlyTile.col:
                #             print("equal to")
                #             SideBoard.outcome = True
                #     elif SideBoard.onlyTile.row < SideBoard.onlyTile.col:
                #         print("less than")
                #         SideBoard.outcome = True





                self.txtBrowser.setStyleSheet("QTextBrowser{color: #00f;}")
                SideBoard.onlyTile.setText("only")
                SideBoard.onlyTile.setStyleSheet('QPushButton{background-color: red;'
                                      'border-radius:2px}')
                print("after setUp SideBoard.outcome =",SideBoard.outcome)
            # else:
            #     #generate two Tiles S and T
            #     fileGenerate = randint(7,26)
            #     SideBoard.tileOne = MainBoard.tiles[randint(0,49)]
            #     SideBoard.tileTwo = MainBoard.tiles[randint(0,49)]
            #     whole = (SideBoard.line[fileGenerate].strip()).split("@")
            #     txt, bool, perm = whole[0], whole[1], whole[2]
            #     self.txtBrowser.setText(txt)
            #     while SideBoard.tileOne == SideBoard.tileTwo:
            #         SideBoard.tileTwo = MainBoard.tiles[randint(0,49)]
            #         continue
            #     SideBoard.tileOne.setText("S")
            #     SideBoard.tileTwo.setText("T")
            #     SideBoard.tileOne.setStyleSheet('QPushButton{background-color: red;'
            #                           'border-radius:2px}')
            #     SideBoard.tileTwo.setStyleSheet('QPushButton{background-color: red;'
            #                           'border-radius:2px}')


app = QApplication(sys.argv)
mainAppObject = InterfaceSub()

sys.exit(app.exec_())