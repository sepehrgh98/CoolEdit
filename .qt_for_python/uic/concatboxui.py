# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\sepeh\Desktop\Visualization\dist\main\visualization\GUI\pdw\concatboxui.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(122, 97)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.concatGroupBox = QtWidgets.QGroupBox(Form)
        self.concatGroupBox.setObjectName("concatGroupBox")
        self.concatBoxLayout = QtWidgets.QFormLayout(self.concatGroupBox)
        self.concatBoxLayout.setObjectName("concatBoxLayout")
        self.verticalLayout.addWidget(self.concatGroupBox)
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(8, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.applyBtn = QtWidgets.QPushButton(self.widget)
        self.applyBtn.setObjectName("applyBtn")
        self.horizontalLayout.addWidget(self.applyBtn)
        self.verticalLayout.addWidget(self.widget)
        self.verticalLayout.setStretch(0, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.concatGroupBox.setTitle(_translate("Form", "Concat Box"))
        self.applyBtn.setText(_translate("Form", "Apply"))
