# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '_listForm.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.listItems = QtWidgets.QListWidget(self.centralwidget)
        self.listItems.setGeometry(QtCore.QRect(30, 30, 291, 261))
        self.listItems.setObjectName("listItems")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(370, 30, 101, 261))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.btnAdd = QtWidgets.QPushButton(self.widget)
        self.btnAdd.setObjectName("btnAdd")
        self.verticalLayout.addWidget(self.btnAdd)
        self.btnEdit = QtWidgets.QPushButton(self.widget)
        self.btnEdit.setObjectName("btnEdit")
        self.verticalLayout.addWidget(self.btnEdit)
        self.btnRemove = QtWidgets.QPushButton(self.widget)
        self.btnRemove.setObjectName("btnRemove")
        self.verticalLayout.addWidget(self.btnRemove)
        self.btnUp = QtWidgets.QPushButton(self.widget)
        self.btnUp.setObjectName("btnUp")
        self.verticalLayout.addWidget(self.btnUp)
        self.btnDown = QtWidgets.QPushButton(self.widget)
        self.btnDown.setObjectName("btnDown")
        self.verticalLayout.addWidget(self.btnDown)
        self.btnSort = QtWidgets.QPushButton(self.widget)
        self.btnSort.setObjectName("btnSort")
        self.verticalLayout.addWidget(self.btnSort)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.btnExit = QtWidgets.QPushButton(self.widget)
        self.btnExit.setObjectName("btnExit")
        self.verticalLayout.addWidget(self.btnExit)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 18))
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
        self.btnAdd.setText(_translate("MainWindow", "Add"))
        self.btnEdit.setText(_translate("MainWindow", "Edit"))
        self.btnRemove.setText(_translate("MainWindow", "Remove"))
        self.btnUp.setText(_translate("MainWindow", "Up"))
        self.btnDown.setText(_translate("MainWindow", "Down"))
        self.btnSort.setText(_translate("MainWindow", "Sort"))
        self.btnExit.setText(_translate("MainWindow", "Exit"))
