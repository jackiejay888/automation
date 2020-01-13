# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'app_program_index.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(624, 338)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(530, 140, 75, 25))
        self.pushButton.setObjectName("pushButton")
        self.label_1 = QtWidgets.QLabel(Form)
        self.label_1.setGeometry(QtCore.QRect(20, 20, 70, 20))
        self.label_1.setObjectName("label_1")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(20, 110, 70, 20))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(20, 50, 70, 20))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(20, 80, 70, 20))
        self.label_4.setObjectName("label_4")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(530, 110, 75, 25))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(100, 140, 75, 25))
        self.pushButton_3.setObjectName("pushButton_3")
        self.checkBox = QtWidgets.QCheckBox(Form)
        self.checkBox.setEnabled(True)
        self.checkBox.setGeometry(QtCore.QRect(20, 140, 70, 20))
        self.checkBox.setObjectName("checkBox")
        self.comboBox = QtWidgets.QComboBox(Form)
        self.comboBox.setEnabled(True)
        self.comboBox.setGeometry(QtCore.QRect(100, 80, 420, 20))
        self.comboBox.setObjectName("comboBox")
        self.comboBox_2 = QtWidgets.QComboBox(Form)
        self.comboBox_2.setEnabled(True)
        self.comboBox_2.setGeometry(QtCore.QRect(100, 50, 420, 20))
        self.comboBox_2.setEditable(True)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.setItemText(0, "")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(100, 110, 420, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(100, 20, 420, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.listView = QtWidgets.QListView(Form)
        self.listView.setGeometry(QtCore.QRect(20, 175, 584, 151))
        self.listView.setObjectName("listView")
        self.pushButton_4 = QtWidgets.QPushButton(Form)
        self.pushButton_4.setGeometry(QtCore.QRect(530, 20, 75, 25))
        self.pushButton_4.setObjectName("pushButton_4")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Advantech_DQA"))
        self.pushButton.setText(_translate("Form", "Download"))
        self.label_1.setText(_translate("Form", "FTP Server IP"))
        self.label_2.setText(_translate("Form", "Download"))
        self.label_3.setText(_translate("Form", "Suite Folder"))
        self.label_4.setText(_translate("Form", "Case Folder"))
        self.pushButton_2.setText(_translate("Form", "Open"))
        self.pushButton_3.setText(_translate("Form", "Search"))
        self.checkBox.setText(_translate("Form", "Latest"))
        self.comboBox_2.setItemText(1, _translate("Form", "Android"))
        self.comboBox_2.setItemText(2, _translate("Form", "Function"))
        self.comboBox_2.setItemText(3, _translate("Form", "Other"))
        self.comboBox_2.setItemText(4, _translate("Form", "Performance"))
        self.comboBox_2.setItemText(5, _translate("Form", "Reliability"))
        self.lineEdit_2.setText(_translate("Form", "127.0.0.1"))
        self.pushButton_4.setText(_translate("Form", "Exit"))
