# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SearchDeviceUI.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(677, 702)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.devicelist_groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.devicelist_groupBox.setGeometry(QtCore.QRect(20, 10, 641, 381))
        self.devicelist_groupBox.setObjectName("devicelist_groupBox")
        self.tableWidget = QtWidgets.QTableWidget(self.devicelist_groupBox)
        self.tableWidget.setEnabled(True)
        self.tableWidget.setGeometry(QtCore.QRect(30, 20, 601, 351))
        self.tableWidget.setGridStyle(QtCore.Qt.SolidLine)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(11)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(9)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(10, item)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(150)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(50)
        self.tableWidget.verticalHeader().setVisible(False)
        self.searchdevice_groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.searchdevice_groupBox.setGeometry(QtCore.QRect(20, 400, 311, 141))
        self.searchdevice_groupBox.setObjectName("searchdevice_groupBox")
        self.SearchDeviceButton = QtWidgets.QPushButton(self.searchdevice_groupBox)
        self.SearchDeviceButton.setEnabled(True)
        self.SearchDeviceButton.setGeometry(QtCore.QRect(30, 50, 261, 41))
        self.SearchDeviceButton.setObjectName("SearchDeviceButton")
        self.Searchtime_label = QtWidgets.QLabel(self.centralwidget)
        self.Searchtime_label.setGeometry(QtCore.QRect(360, 450, 121, 20))
        self.Searchtime_label.setObjectName("Searchtime_label")
        self.Searchtime_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.Searchtime_lineEdit.setGeometry(QtCore.QRect(490, 450, 131, 20))
        self.Searchtime_lineEdit.setObjectName("Searchtime_lineEdit")
        self.Init_groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.Init_groupBox.setGeometry(QtCore.QRect(20, 540, 311, 91))
        self.Init_groupBox.setObjectName("Init_groupBox")
        self.InitButton = QtWidgets.QPushButton(self.Init_groupBox)
        self.InitButton.setGeometry(QtCore.QRect(30, 30, 261, 41))
        self.InitButton.setObjectName("InitButton")
        self.SearchByIpButton = QtWidgets.QPushButton(self.centralwidget)
        self.SearchByIpButton.setGeometry(QtCore.QRect(360, 570, 261, 41))
        self.SearchByIpButton.setObjectName("SearchByIpButton")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(340, 400, 331, 231))
        self.groupBox.setObjectName("groupBox")
        self.StartIP_lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.StartIP_lineEdit.setGeometry(QtCore.QRect(150, 90, 131, 20))
        self.StartIP_lineEdit.setObjectName("StartIP_lineEdit")
        self.StartIP_label = QtWidgets.QLabel(self.groupBox)
        self.StartIP_label.setGeometry(QtCore.QRect(20, 90, 121, 20))
        self.StartIP_label.setObjectName("StartIP_label")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(30, 130, 111, 20))
        self.label_2.setObjectName("label_2")
        self.EndIP_lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.EndIP_lineEdit.setGeometry(QtCore.QRect(150, 130, 131, 20))
        self.EndIP_lineEdit.setObjectName("EndIP_lineEdit")
        self.groupBox.raise_()
        self.searchdevice_groupBox.raise_()
        self.devicelist_groupBox.raise_()
        self.Searchtime_label.raise_()
        self.Searchtime_lineEdit.raise_()
        self.Init_groupBox.raise_()
        self.SearchByIpButton.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 677, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.SearchDeviceButton.clicked.connect(MainWindow.search_Device_Btn)
        self.InitButton.clicked.connect(MainWindow.Init_Btn)
        self.SearchByIpButton.clicked.connect(MainWindow.search_Device_ByIp_Btn)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "设备搜索Search Devices"))
        self.devicelist_groupBox.setTitle(_translate("MainWindow", "设备列表(Device List)"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "序号(No.)"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "状态(Status)"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "IP版本(IP Version)"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "IP地址(IP Address)"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "端口(Port)"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", " 子网掩码(Subnet Mask)"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "网关(Gateway)"))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "物理地址(Mac Address)"))
        item = self.tableWidget.horizontalHeaderItem(8)
        item.setText(_translate("MainWindow", "设备类型(Device Type)"))
        item = self.tableWidget.horizontalHeaderItem(9)
        item.setText(_translate("MainWindow", "详细类型(Detail Type)"))
        item = self.tableWidget.horizontalHeaderItem(10)
        item.setText(_translate("MainWindow", "Http(Http)"))
        self.searchdevice_groupBox.setTitle(_translate("MainWindow", "搜索设备(Search Devices)"))
        self.SearchDeviceButton.setText(_translate("MainWindow", "组播和广播搜索(Multicast and Broadcast)"))
        self.Searchtime_label.setText(_translate("MainWindow", "搜索时间ms(Time:ms):"))
        self.Searchtime_lineEdit.setText(_translate("MainWindow", "3000"))
        self.Init_groupBox.setTitle(_translate("MainWindow", "操作设备(Operate Devices)"))
        self.InitButton.setText(_translate("MainWindow", "初始化(Initialization)"))
        self.SearchByIpButton.setText(_translate("MainWindow", "点对点搜索(Point to Point Search)"))
        self.groupBox.setTitle(_translate("MainWindow", "单播搜索(Unicast)"))
        self.StartIP_label.setText(_translate("MainWindow", "起始IP地址(Start IP)"))
        self.label_2.setText(_translate("MainWindow", "结束IP地址(End IP)"))
