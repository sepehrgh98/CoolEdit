# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'f:\Visualization\visualization\GUI\pdw\pdwexporttools.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(797, 84)
        self.horizontalLayout = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.widget_2 = QtWidgets.QWidget(Form)
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.concatChannelsBtn = QtWidgets.QPushButton(self.widget_2)
        self.concatChannelsBtn.setMinimumSize(QtCore.QSize(40, 40))
        self.concatChannelsBtn.setMaximumSize(QtCore.QSize(40, 40))
        self.concatChannelsBtn.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("f:\\Visualization\\visualization\\GUI\\pdw\\../../Resources/icons/concate.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.concatChannelsBtn.setIcon(icon)
        self.concatChannelsBtn.setIconSize(QtCore.QSize(30, 30))
        self.concatChannelsBtn.setCheckable(False)
        self.concatChannelsBtn.setObjectName("concatChannelsBtn")
        self.horizontalLayout_2.addWidget(self.concatChannelsBtn)
        self.horizontalLayout.addWidget(self.widget_2)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
