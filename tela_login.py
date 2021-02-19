# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tela_login.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(485, 479)
        MainWindow.setStyleSheet("\n"
"background-color: rgb(85, 170, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(190, 260, 161, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(46, 255, 242);\n"
"border-radius: 15px;\n"
"border-style:outset;\n"
"border-width: 2px;\n"
"border-color:black;")
        self.pushButton.setObjectName("pushButton")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(130, 77, 271, 41))
        self.lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 15px;\n"
"border-style:outset;\n"
"border-width: 2px;")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(130, 170, 271, 41))
        self.lineEdit_3.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 15px;\n"
"border-style:outset;\n"
"border-width: 2px;")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(310, 380, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 127);\n"
"border-radius: 15px;\n"
"border-style:outset;\n"
"border-width: 2px;\n"
"border-color:black;")
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(30, 390, 58, 16))
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(40, 390, 191, 21))
        font = QtGui.QFont()
        font.setFamily("KacstLetter")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("\n"
"color: rgb(0, 0, 0);")
        self.label_4.setObjectName("label_4")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(90, 80, 31, 41))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("usuario1.svg"))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(90, 170, 41, 41))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("9263241821582518283-32.png"))
        self.label_2.setObjectName("label_2")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(130, 230, 0, 0))
        self.label_5.setMaximumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color rgb(255, 255, 127);")
        self.label_5.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.label_2.raise_()
        self.label.raise_()
        self.pushButton.raise_()
        self.lineEdit.raise_()
        self.lineEdit_3.raise_()
        self.pushButton_2.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.label_5.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 485, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "LOGIN"))
        self.pushButton_2.setText(_translate("MainWindow", "Cadastrar-se"))
        self.label_4.setText(_translate("MainWindow", "Não é cadastrado?"))
