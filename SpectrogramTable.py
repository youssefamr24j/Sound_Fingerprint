# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SpectrogramTable.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Table(object):
    def __init__(self,data):
        self.data=data
    def setupUi(self, Table):
        Table.setObjectName("Table")
        Table.resize(744, 511)
        Table.setStyleSheet("background-color:rgb(255, 255, 127)")
        self.centralwidget = QtWidgets.QWidget(Table)
        self.centralwidget.setStyleSheet("background-color:")
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy)
        self.tableWidget.setMaximumSize(QtCore.QSize(16777215, 535))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.tableWidget.setFont(font)
        self.tableWidget.setStyleSheet("color:red;")
        self.tableWidget.setAutoScroll(True)
        self.tableWidget.setGridStyle(QtCore.Qt.SolidLine)
        self.tableWidget.setRowCount(10)
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setObjectName("tableWidget")
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(350)
        self.tableWidget.verticalHeader().setVisible(True)
        self.tableWidget.verticalHeader().setDefaultSectionSize(40)
        self.gridLayout.addWidget(self.tableWidget, 0, 0, 1, 1)
        Table.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Table)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 744, 25))
        self.menubar.setObjectName("menubar")
        Table.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Table)
        self.statusbar.setObjectName("statusbar")
        Table.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(Table)
        self.toolBar.setObjectName("toolBar")
        Table.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)

        self.tableWidget.setEnabled(False)
        # self.tableWidget.setItem(1,1,QtWidgets.QTableWidgetItem("10"))

        self.retranslateUi(Table)
        QtCore.QMetaObject.connectSlotsByName(Table)

    def retranslateUi(self, Table):
        _translate = QtCore.QCoreApplication.translate
        Table.setWindowTitle(_translate("Table", "Table"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Table", "Song name"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Table", "Similarity percentage"))
        self.toolBar.setWindowTitle(_translate("Table", "toolBar"))
        self.ViewData()



    def ViewData(self):
        level=0
        for i in self.data:
            self.tableWidget.setItem(level,0,QtWidgets.QTableWidgetItem(i[0]))
            self.tableWidget.setItem(level,1,QtWidgets.QTableWidgetItem(str(i[1])+'%'))
            level=level+1
            


