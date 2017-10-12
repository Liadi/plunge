# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainMenu.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(548, 500)
        MainWindow.setMinimumSize(QtCore.QSize(500, 500))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.doubleButton = QtGui.QPushButton(self.centralwidget)
        self.doubleButton.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Chiller"))
        font.setPointSize(25)
        self.doubleButton.setFont(font)
        self.doubleButton.setObjectName(_fromUtf8("doubleButton"))
        self.verticalLayout.addWidget(self.doubleButton)
        self.gridButton = QtGui.QPushButton(self.centralwidget)
        self.gridButton.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Chiller"))
        font.setPointSize(25)
        self.gridButton.setFont(font)
        self.gridButton.setObjectName(_fromUtf8("gridButton"))
        self.verticalLayout.addWidget(self.gridButton)
        self.conditionButton = QtGui.QPushButton(self.centralwidget)
        self.conditionButton.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Chiller"))
        font.setPointSize(25)
        self.conditionButton.setFont(font)
        self.conditionButton.setObjectName(_fromUtf8("conditionButton"))
        self.verticalLayout.addWidget(self.pushButton_3)
        self.pushButton_4 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_4.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Chiller"))
        font.setPointSize(25)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.verticalLayout.addWidget(self.pushButton_4)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 548, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.pushButton.setText(_translate("MainWindow", "Double", None))
        self.gridButton.setText(_translate("MainWindow", "Grid", None))
        self.conditionButton.setText(_translate("MainWindow", "Condition", None))
        self.pushButton_4.setText(_translate("MainWindow", "Poser", None))
