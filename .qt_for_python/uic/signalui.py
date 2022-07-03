# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\sepeh\Desktop\Visualization\visualization\GUI\signal\signalui.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.plotControllerWidget = QtWidgets.QWidget(self.centralwidget)
        self.plotControllerWidget.setObjectName("plotControllerWidget")
        self.plotControllerWidgetLayout = QtWidgets.QHBoxLayout(self.plotControllerWidget)
        self.plotControllerWidgetLayout.setObjectName("plotControllerWidgetLayout")
        self.verticalLayout.addWidget(self.plotControllerWidget)
        self.plotWidget = QtWidgets.QWidget(self.centralwidget)
        self.plotWidget.setObjectName("plotWidget")
        self.plotLayout = QtWidgets.QVBoxLayout(self.plotWidget)
        self.plotLayout.setObjectName("plotLayout")
        self.verticalLayout.addWidget(self.plotWidget)
        self.controlWidget = QtWidgets.QWidget(self.centralwidget)
        self.controlWidget.setObjectName("controlWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.controlWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.toolsWidget = QtWidgets.QWidget(self.controlWidget)
        self.toolsWidget.setObjectName("toolsWidget")
        self.formLayout = QtWidgets.QFormLayout(self.toolsWidget)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.toolsWidget)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.sampleFreqLineEdit = QtWidgets.QLineEdit(self.toolsWidget)
        self.sampleFreqLineEdit.setObjectName("sampleFreqLineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.sampleFreqLineEdit)
        self.openFileBtn = QtWidgets.QPushButton(self.toolsWidget)
        self.openFileBtn.setObjectName("openFileBtn")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.SpanningRole, self.openFileBtn)
        self.IFLineEdit = QtWidgets.QLineEdit(self.toolsWidget)
        self.IFLineEdit.setObjectName("IFLineEdit")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.IFLineEdit)
        self.label_2 = QtWidgets.QLabel(self.toolsWidget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.horizontalLayout.addWidget(self.toolsWidget)
        self.tableContainerWidget = QtWidgets.QWidget(self.controlWidget)
        self.tableContainerWidget.setObjectName("tableContainerWidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.tableContainerWidget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.tableWidget = QtWidgets.QTableWidget(self.tableContainerWidget)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
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
        self.horizontalLayout_2.addWidget(self.tableWidget)
        self.horizontalLayout.addWidget(self.tableContainerWidget)
        self.horizontalLayout.setStretch(1, 1)
        self.verticalLayout.addWidget(self.controlWidget)
        self.verticalLayout.setStretch(1, 2)
        self.verticalLayout.setStretch(2, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
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
        self.label.setText(_translate("MainWindow", "Sample Frequency (Hz)"))
        self.openFileBtn.setText(_translate("MainWindow", "open file"))
        self.label_2.setText(_translate("MainWindow", "IF Frequency(Hz)"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Strat Time(mics)"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "End Time(mics)"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Type"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "IFFreq "))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "PW"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Start Freq(MHz)"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "End Freq(MHz)"))
