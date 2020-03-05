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
        Form_click_button.setWindowModality(QtCore.Qt.WindowModal)
        Form_click_button.resize(500, 500)
        Form_click_button.setAutoFillBackground(False)
        self.click_button = QtWidgets.QPushButton(Form_click_button)
        self.click_button.setGeometry(QtCore.QRect(50, 50, 400, 400))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(70)
        font.setBold(True)
        font.setWeight(75)
        self.click_button.setFont(font)
        self.click_button.setAutoFillBackground(False)
        self.click_button.setStyleSheet("")
        self.click_button.setText("Click")
        self.click_button.setCheckable(False)
        self.click_button.setChecked(False)
        self.click_button.setObjectName("click_button")
        self.log_reset = QtWidgets.QPushButton(Form_click_button)
        self.log_reset.setGeometry(QtCore.QRect(0, 0, 50, 50))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.log_reset.setFont(font)
        self.log_reset.setAutoFillBackground(False)
        self.log_reset.setStyleSheet("")
        self.log_reset.setObjectName("log_reset")
        self.lcd_show = QtWidgets.QLCDNumber(Form_click_button)
        self.lcd_show.setGeometry(QtCore.QRect(200, 0, 100, 50))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setBold(True)
        font.setWeight(75)
        self.lcd_show.setFont(font)
        self.lcd_show.setAutoFillBackground(False)
        self.lcd_show.setFrameShape(QtWidgets.QFrame.Box)
        self.lcd_show.setLineWidth(1)
        self.lcd_show.setMidLineWidth(1)
        self.lcd_show.setSmallDecimalPoint(False)
        self.lcd_show.setDigitCount(5)
        self.lcd_show.setSegmentStyle(QtWidgets.QLCDNumber.Filled)
        self.lcd_show.setProperty("intValue", 99999)
        self.lcd_show.setObjectName("lcd_show")
        self.enable = QtWidgets.QRadioButton(Form_click_button)
        self.enable.setEnabled(True)
        self.enable.setGeometry(QtCore.QRect(430, 10, 60, 15))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.enable.setFont(font)
        self.enable.setChecked(False)
        self.enable.setObjectName("enable")
        self.disable = QtWidgets.QRadioButton(Form_click_button)
        self.disable.setEnabled(True)
        self.disable.setGeometry(QtCore.QRect(430, 25, 60, 15))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.disable.setFont(font)
        self.disable.setCheckable(True)
        self.disable.setChecked(False)
        self.disable.setObjectName("disable")

        self.retranslateUi(Form_click_button)
        QtCore.QMetaObject.connectSlotsByName(Form_click_button)

    def retranslateUi(self, Form_click_button):
        _translate = QtCore.QCoreApplication.translate
        Form_click_button.setWindowTitle(_translate("Form_click_button", "ZL"))
        self.log_reset.setText(_translate("Form_click_button", "Clear"))
        self.enable.setText(_translate("Form_click_button", "Enable"))
        self.disable.setText(_translate("Form_click_button", "Disable"))
