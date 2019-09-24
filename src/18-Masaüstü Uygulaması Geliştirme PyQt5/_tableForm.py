# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '_tableForm.ui'
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
        self.tableProducts = QtWidgets.QTableWidget(self.centralwidget)
        self.tableProducts.setGeometry(QtCore.QRect(10, 10, 311, 261))
        self.tableProducts.setObjectName("tableProducts")
        self.tableProducts.setColumnCount(0)
        self.tableProducts.setRowCount(0)
        self.formLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(340, 10, 231, 171))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.txtName = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.txtName.setObjectName("txtName")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.txtName)
        self.txtPrice = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.txtPrice.setObjectName("txtPrice")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.txtPrice)
        self.label = QtWidgets.QLabel(self.formLayoutWidget)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.btnSave = QtWidgets.QPushButton(self.formLayoutWidget)
        self.btnSave.setObjectName("btnSave")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.btnSave)
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
        self.label.setText(_translate("MainWindow", "Name"))
        self.label_2.setText(_translate("MainWindow", "Price"))
        self.btnSave.setText(_translate("MainWindow", "Save"))
