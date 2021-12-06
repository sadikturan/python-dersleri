# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '_comboboxForm.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(403, 311)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.cbSehirler = QtWidgets.QComboBox(self.centralwidget)
        self.cbSehirler.setGeometry(QtCore.QRect(50, 20, 151, 41))
        self.cbSehirler.setObjectName("cbSehirler")
        self.lblResult = QtWidgets.QLabel(self.centralwidget)
        self.lblResult.setGeometry(QtCore.QRect(220, 20, 141, 41))
        self.lblResult.setObjectName("lblResult")
        self.btnGetItem = QtWidgets.QPushButton(self.centralwidget)
        self.btnGetItem.setGeometry(QtCore.QRect(50, 90, 151, 41))
        self.btnGetItem.setObjectName("btnGetItem")
        self.btnLoadItems = QtWidgets.QPushButton(self.centralwidget)
        self.btnLoadItems.setGeometry(QtCore.QRect(220, 90, 151, 41))
        self.btnLoadItems.setObjectName("btnLoadItems")
        self.btnClear = QtWidgets.QPushButton(self.centralwidget)
        self.btnClear.setGeometry(QtCore.QRect(50, 140, 151, 41))
        self.btnClear.setObjectName("btnClear")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 403, 18))
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
        self.lblResult.setText(_translate("MainWindow", "TextLabel"))
        self.btnGetItem.setText(_translate("MainWindow", "Get Item"))
        self.btnLoadItems.setText(_translate("MainWindow", "Load Items"))
        self.btnClear.setText(_translate("MainWindow", "Clear Items"))
