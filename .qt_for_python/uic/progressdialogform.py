# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'f:\Visualization\visualization\GUI\progressdialogform.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(491, 163)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.formLayout = QtWidgets.QFormLayout(self.groupBox)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.readingProgressBar = QtWidgets.QProgressBar(self.groupBox)
        self.readingProgressBar.setProperty("value", 0)
        self.readingProgressBar.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.readingProgressBar.setObjectName("readingProgressBar")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.readingProgressBar)
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.parsingProgressBar = QtWidgets.QProgressBar(self.groupBox)
        self.parsingProgressBar.setProperty("value", 0)
        self.parsingProgressBar.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.parsingProgressBar.setObjectName("parsingProgressBar")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.parsingProgressBar)
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.visualizingProgressBar = QtWidgets.QProgressBar(self.groupBox)
        self.visualizingProgressBar.setProperty("value", 0)
        self.visualizingProgressBar.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.visualizingProgressBar.setObjectName("visualizingProgressBar")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.visualizingProgressBar)
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.capsulationProgressBar = QtWidgets.QProgressBar(self.groupBox)
        self.capsulationProgressBar.setProperty("value", 0)
        self.capsulationProgressBar.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.capsulationProgressBar.setTextVisible(True)
        self.capsulationProgressBar.setObjectName("capsulationProgressBar")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.capsulationProgressBar)
        self.verticalLayout.addWidget(self.groupBox)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Reading:"))
        self.readingProgressBar.setFormat(_translate("Dialog", "%p%"))
        self.label_2.setText(_translate("Dialog", "Parsing:"))
        self.label_3.setText(_translate("Dialog", "Visualizing:"))
        self.label_4.setText(_translate("Dialog", "Capsulation:"))
