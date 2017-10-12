__author__ = 'Omotola'
import sys
from PyQt4.QtGui import *
from  PyQt4.QtCore import *

class Button(QPushButton):
    def __init__(self, par):
        super(Button, self).__init__()
        self.setParent(par)
        self.label = QLabel("lbl", self)
        self.label.resize(300,90)

class Example(QWidget):
    def __init__(self):
        super(Example, self).__init__()
        #self.setGeometry(300, 300, 280, 270)
        self.setWindowTitle('Pen styles')
        #self.move(0, 0)
        self.resize(750,750)
        self.btn = QPushButton("Animated Button", self)
        self.btn.setGeometry(450, 450, 100, 30)
        self.connect(self.btn, SIGNAL("clicked()"), self.lblAnim)
        butt = Button(self)
        self.lbl = butt.label

        # self.lbl = QLabel("lbl", self)
        # self.lbl.resize(300,90)
        pix = QPixmap("C:/Users/Omotola/Downloads/others/Play-icon1.png")
        pix = pix.scaled(self.lbl.size(), Qt.KeepAspectRatio)
        # pix.scaled(20, 20)
        # print("BOOLEAN",pix.save("pixCreated.png"));
        # finalPix = QPixmap()
        # finalPix.fromImage(pix)
        self.lbl.setPixmap(pix)
        self.show()
        #self.btn.resize(150,50)

    def btnAnim(self):
        anim = QPropertyAnimation(self.btn,"geometry",self)
        anim.setDuration(1000)
        anim.setStartValue(QRect(0, 0, 100, 30))
        anim.setEndValue(QRect(450, 450, 200, 60))
        anim.start()

    def lblAnim(self):
        # self.btn.setGeometry(450, 450, 100, 30)
        lastLabel = QLabel(self)
        anim = QPropertyAnimation(self.lbl,"geometry",self)
        anim.setDuration(1000)
        anim.setStartValue(QRect(0, 0, 300, 90))
        anim.setEndValue(QRect(475, 475, 300, 90))
        anim.start()

        #lbl = QLabel("lbl", self.btn)


        # img = QImage("C:/Users/Omotola/Downloads/others/Start-icon.png")
        # img.scaled(15, 15)
        # img.rect().moveTo(150,0)
        # rect = QRect(QPoint(100, 200), QSize(11, 16))
        # # rect.setSize(QSize(150, 150))
        # # rect.moveTo(150, 150)
        #
        # lbl.setPixmap(QPixmap(img))
        # lbl.setGeometry(15,0, 25, 25)
        #self.show()


def main():

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()