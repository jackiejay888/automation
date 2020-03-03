# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'click_button.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form_click_button(object):
    def setupUi(self, Form_click_button):
        Form_click_button.setObjectName("Form_click_button")
        Form_click_button.resize(500, 500)
        self.click_button = QtWidgets.QPushButton(Form_click_button)
        self.click_button.setGeometry(QtCore.QRect(50, 50, 400, 400))
        self.click_button.setText("ZL")
        self.click_button.setObjectName("click_button")
        self.log_reset = QtWidgets.QPushButton(Form_click_button)
        self.log_reset.setGeometry(QtCore.QRect(0, 0, 50, 50))
        self.log_reset.setObjectName("log_reset")

        self.retranslateUi(Form_click_button)
        QtCore.QMetaObject.connectSlotsByName(Form_click_button)

    def retranslateUi(self, Form_click_button):
        _translate = QtCore.QCoreApplication.translate
        Form_click_button.setWindowTitle(_translate("Form_click_button", "ZL"))
        self.log_reset.setText(_translate("Form_click_button", "Reset"))
