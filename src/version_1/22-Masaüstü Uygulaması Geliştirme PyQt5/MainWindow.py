# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(494, 343)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(60, 60, 51, 31))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(60, 90, 51, 31))
        self.label_2.setObjectName("label_2")
        self.txt_sayi1 = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_sayi1.setGeometry(QtCore.QRect(110, 60, 200, 32))
        self.txt_sayi1.setObjectName("txt_sayi1")
        self.txt_sayi2 = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_sayi2.setGeometry(QtCore.QRect(110, 100, 200, 32))
        self.txt_sayi2.setObjectName("txt_sayi2")
        self.btn_toplama = QtWidgets.QPushButton(self.centralwidget)
        self.btn_toplama.setGeometry(QtCore.QRect(110, 150, 71, 31))
        self.btn_toplama.setObjectName("btn_toplama")
        self.btn_cikarma = QtWidgets.QPushButton(self.centralwidget)
        self.btn_cikarma.setGeometry(QtCore.QRect(190, 150, 71, 31))
        self.btn_cikarma.setObjectName("btn_cikarma")
        self.btn_bolme = QtWidgets.QPushButton(self.centralwidget)
        self.btn_bolme.setGeometry(QtCore.QRect(270, 150, 71, 31))
        self.btn_bolme.setObjectName("btn_bolme")
        self.btn_carpma = QtWidgets.QPushButton(self.centralwidget)
        self.btn_carpma.setGeometry(QtCore.QRect(350, 180, 71, 31))
        self.btn_carpma.setObjectName("btn_carpma")
        self.lbl_sonuc = QtWidgets.QLabel(self.centralwidget)
        self.lbl_sonuc.setGeometry(QtCore.QRect(110, 200, 121, 21))
        self.lbl_sonuc.setObjectName("lbl_sonuc")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 494, 18))
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
        self.label.setText(_translate("MainWindow", "Sayı 1:"))
        self.label_2.setText(_translate("MainWindow", "Sayı 2:"))
        self.btn_toplama.setText(_translate("MainWindow", "Toplama"))
        self.btn_cikarma.setText(_translate("MainWindow", "Çıkarma"))
        self.btn_bolme.setText(_translate("MainWindow", "Bölme"))
        self.btn_carpma.setText(_translate("MainWindow", "Çarpma"))
        self.lbl_sonuc.setText(_translate("MainWindow", "Sonuç:"))
