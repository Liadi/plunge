__author__ = 'Omotola'
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from math import floor
from random import randint
import sys
import PoserOne
from customInterfaceWidget import Tile

class InterfaceSub(PoserOne.Interface):
    data = ""

    def __init__(self):
        f = open("condi_ss.stylesheet", 'r')
        InterfaceSub.data = f.read()
        f.close()

        super(InterfaceSub, self).__init__()
        self.main()

    def main(self):

        self.boardObject.lay.addWidget(MainBoard())
        self.drop = DropBoard()
        self.control = ControlBoard()
        self.timer = TimerBoard()
        self.sideObj.lay.addWidget(self.drop)
        self.sideObj.lay.addWidget(self.timer)
        self.sideObj.lay.addWidget(self.control)

class MainBoard(QFrame):
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

    def getMatrix(self):
        return self.row, self.col
    def dragEnterEvent(self, e):
        e.accept()

    def mouseMoveEvent(self, e):
        if self.connected and e.buttons() == Qt.LeftButton:
            pass

    def dropEvent(self, e):
        i = int(e.mimeData().text())
        obj = DropBoard.tileArray[i]
        if obj.getConnected() != None:
            obj.getConnected().setStyleSheet('QPushButton{background-color: black;'
                                      'border-radius:2px}')


        self.setStyleSheet('QPushButton{background-color: blue;'
                                      'border-radius:2px}')
        obj.setConnected(tile=self)
        txt = obj.text()

        obj.line.setP2(QPoint(self.pos()))
        obj.line.setP1(QPoint(obj.pos()))

        # #painter.begin(mainAppObject)
        # pen = QPen(Qt.red, 2, Qt.SolidLine)
        # print("wait")
        #
        # ln = QLineF(0.0, 0.0, 200.0, 500.0)
        # painter = QPainter(self)
        # painter.setPen(pen)
        # painter.drawLine(ln)
        # #painter.end()
        # #ln = Line()

        path = QPainterPath();
        path.moveTo(20, 80);
        path.lineTo(20, 30);
        path.cubicTo(80, 0, 50, 50, 80, 80);

        painter = QPainter(self);
        painter.drawPath(path);

class Line(QWidget):
    def __init__(self):
        super(Line, self).__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 280, 270)
        self.show()
    def paintEvent(self, e):
        print("whatag")
        qp = QPainter()
        qp.begin(self)
        self.drawLine(qp)
        qp.end()
    def drawLine(self, qp):
        pen = QPen(Qt.red, 2, Qt.SolidLine)
        qp.setPen(pen)
        print("what")
        qp.drawLine(20, 40, 250, 40)

class Droper(QPushButton):
    def __init__(self, index):
        super(Droper, self).__init__()
        self.setStyleSheet(InterfaceSub.data)
        self.connected = None
        self.index = index
        self.line = QLine()
    def setConnected(self, tile):
        self.connected = tile
    def getConnected(self):
        return self.connected
    def mouseMoveEvent(self, e):
        if TimerBoard.pressed and (e.buttons() == Qt.LeftButton):
            mimeData = QMimeData()
            #self.text()
            mimeData.setText(str(self.index))

            self.drag = QDrag(self)
            self.drag.setMimeData(mimeData)
            self.drag.start()

class DropBoard(QFrame):
    tileArray = []
    def __init__(self):
        super(DropBoard, self).__init__()
        self.setLineWidth(2)
        self.setFrameStyle(QFrame.Panel | QFrame.Raised)
        self.grid = QGridLayout(self)
        self.grid.setContentsMargins(0,0,0,0)
        self.grid.setHorizontalSpacing(0)
        self.grid.setVerticalSpacing(0)
        self.grid.setSpacing(0)
        for i in range(0, 25, 1):
            row = floor(i/5)
            col = i%5
            btn = Droper(index = i)
            btn.setMaximumHeight(65)
            btn.setMaximumWidth(75)

            DropBoard.tileArray.append(btn)
            self.grid.addWidget(btn, row, col)


    def setDimension(self, height, width):
        self.setFixedHeight(height)
        self.setFixedWidth(width)

class TimerBoard(QFrame):
    pressed = False
    def __init__(self):
        super(TimerBoard, self).__init__()
        self.setLineWidth(2)
        self.setFrameStyle(QFrame.Panel | QFrame.Raised)
        self.lcd = QLCDNumber(self)
        self.lcd.setDigitCount(5)


        self.restartBtn = QPushButton("START")
        self.restartBtn.setObjectName("prBtn")
        self.restartBtn.setStyleSheet(InterfaceSub.data)

        self.lcd.setFixedHeight(self.height() * 0.1)

        self.restartBtn.clicked.connect(self.start)

        self.btnLay = QHBoxLayout()
        self.btnLay.addWidget(self.restartBtn)
        self.lay = QVBoxLayout()
        self.lay.addWidget(self.lcd)
        self.lay.addLayout(self.btnLay)
        self.setLayout(self.lay)
        self.h = 0
        self.m = 2
        self.s = 0

        self.hour = 0
        self.minute = 0
        self.second = 0
        self.main()


    def start(self):
        if TimerBoard.pressed:
            TimerBoard.restartBtn
        for i in range(1, mainAppObject.drop.children().__len__(), 1):
            d = randint(0,1)
            row = randint(0,4) * 2 + d
            col = randint(0,4) * 2 + d
            txt = str(row)+","+ str(col)
            mainAppObject.drop.children()[i].setText(txt)

        TimerBoard.pressed = True

    def restart(self):
        TimerBoard.press = False
        TimerBoard.pressed = False
        self.start()


    def main(self):
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.modify)

    def modify(self):
        if self.s == 0:
            self.s = 59
            self.m -= 1
        else:
            self.s -= 1
        if self.s == 0 and self.m == 0:
            self.timer.stop()



class ControlBoard(QFrame):
    def __init__(self):
        super(ControlBoard, self).__init__()
        self.setLineWidth(2)
        self.setFrameStyle(QFrame.Panel | QFrame.Raised)

app = QApplication(sys.argv)
mainAppObject = InterfaceSub()

sys.exit(app.exec_())
