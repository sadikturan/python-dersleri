# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '_checkbox.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(498, 368)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btnHobilerSecilenleriAl = QtWidgets.QPushButton(self.centralwidget)
        self.btnHobilerSecilenleriAl.setGeometry(QtCore.QRect(80, 190, 111, 41))
        self.btnHobilerSecilenleriAl.setObjectName("btnHobilerSecilenleriAl")
        self.lblResultHobiler = QtWidgets.QLabel(self.centralwidget)
        self.lblResultHobiler.setGeometry(QtCore.QRect(80, 240, 111, 101))
        self.lblResultHobiler.setText("")
        self.lblResultHobiler.setObjectName("lblResultHobiler")
        self.groupHobiler = QtWidgets.QGroupBox(self.centralwidget)
        self.groupHobiler.setGeometry(QtCore.QRect(60, 10, 181, 181))
        self.groupHobiler.setObjectName("groupHobiler")
        self.widget = QtWidgets.QWidget(self.groupHobiler)
        self.widget.setGeometry(QtCore.QRect(30, 30, 111, 111))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.cbSinema = QtWidgets.QCheckBox(self.widget)
        self.cbSinema.setObjectName("cbSinema")
        self.verticalLayout.addWidget(self.cbSinema)
        self.cbKitapOkumak = QtWidgets.QCheckBox(self.widget)
        self.cbKitapOkumak.setObjectName("cbKitapOkumak")
        self.verticalLayout.addWidget(self.cbKitapOkumak)
        self.cbSpor = QtWidgets.QCheckBox(self.widget)
        self.cbSpor.setObjectName("cbSpor")
        self.verticalLayout.addWidget(self.cbSpor)
        self.groupDersler = QtWidgets.QGroupBox(self.centralwidget)
        self.groupDersler.setGeometry(QtCore.QRect(270, 10, 181, 181))
        self.groupDersler.setObjectName("groupDersler")
        self.layoutWidget = QtWidgets.QWidget(self.groupDersler)
        self.layoutWidget.setGeometry(QtCore.QRect(30, 30, 111, 111))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.cbWebTasarim = QtWidgets.QCheckBox(self.layoutWidget)
        self.cbWebTasarim.setObjectName("cbWebTasarim")
        self.verticalLayout_2.addWidget(self.cbWebTasarim)
        self.cbProgramlama = QtWidgets.QCheckBox(self.layoutWidget)
        self.cbProgramlama.setObjectName("cbProgramlama")
        self.verticalLayout_2.addWidget(self.cbProgramlama)
        self.cbMatematik = QtWidgets.QCheckBox(self.layoutWidget)
        self.cbMatematik.setObjectName("cbMatematik")
        self.verticalLayout_2.addWidget(self.cbMatematik)
        self.btnDerslerSecilenleriAl = QtWidgets.QPushButton(self.centralwidget)
        self.btnDerslerSecilenleriAl.setGeometry(QtCore.QRect(270, 190, 111, 41))
        self.btnDerslerSecilenleriAl.setObjectName("btnDerslerSecilenleriAl")
        self.lblResultDersler = QtWidgets.QLabel(self.centralwidget)
        self.lblResultDersler.setGeometry(QtCore.QRect(270, 240, 111, 101))
        self.lblResultDersler.setText("")
        self.lblResultDersler.setObjectName("lblResultDersler")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 498, 18))
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
        self.btnHobilerSecilenleriAl.setText(_translate("MainWindow", "Seçilenleri Al"))
        self.groupHobiler.setTitle(_translate("MainWindow", "GroupBox"))
        self.cbSinema.setText(_translate("MainWindow", "Sinema"))
        self.cbKitapOkumak.setText(_translate("MainWindow", "Kitap Okumak"))
        self.cbSpor.setText(_translate("MainWindow", "Spor"))
        self.groupDersler.setTitle(_translate("MainWindow", "GroupBox"))
        self.cbWebTasarim.setText(_translate("MainWindow", "Web Tasarım"))
        self.cbProgramlama.setText(_translate("MainWindow", "Programlama"))
        self.cbMatematik.setText(_translate("MainWindow", "Matematik"))
        self.btnDerslerSecilenleriAl.setText(_translate("MainWindow", "Seçilenleri Al"))
