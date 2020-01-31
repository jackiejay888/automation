# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'app_program_index.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form_dqa(object):
    def setupUi(self, Form_dqa):
        Form_dqa.setObjectName("Form_dqa")
        Form_dqa.resize(623, 554)
        self.pushButton_download = QtWidgets.QPushButton(Form_dqa)
        self.pushButton_download.setGeometry(QtCore.QRect(530, 140, 75, 25))
        self.pushButton_download.setObjectName("pushButton_download")
        self.label_ip = QtWidgets.QLabel(Form_dqa)
        self.label_ip.setGeometry(QtCore.QRect(20, 20, 70, 20))
        self.label_ip.setObjectName("label_ip")
        self.label_download = QtWidgets.QLabel(Form_dqa)
        self.label_download.setGeometry(QtCore.QRect(20, 110, 70, 20))
        self.label_download.setObjectName("label_download")
        self.label_suite = QtWidgets.QLabel(Form_dqa)
        self.label_suite.setGeometry(QtCore.QRect(20, 50, 70, 20))
        self.label_suite.setObjectName("label_suite")
        self.label_case = QtWidgets.QLabel(Form_dqa)
        self.label_case.setGeometry(QtCore.QRect(20, 80, 70, 20))
        self.label_case.setObjectName("label_case")
        self.pushButton_open = QtWidgets.QPushButton(Form_dqa)
        self.pushButton_open.setGeometry(QtCore.QRect(530, 110, 75, 25))
        self.pushButton_open.setObjectName("pushButton_open")
        self.pushButton_search = QtWidgets.QPushButton(Form_dqa)
        self.pushButton_search.setGeometry(QtCore.QRect(445, 140, 75, 25))
        self.pushButton_search.setObjectName("pushButton_search")
        self.checkBox_latest = QtWidgets.QCheckBox(Form_dqa)
        self.checkBox_latest.setEnabled(True)
        self.checkBox_latest.setGeometry(QtCore.QRect(20, 140, 91, 20))
        self.checkBox_latest.setChecked(True)
        self.checkBox_latest.setObjectName("checkBox_latest")
        self.comboBox_case = QtWidgets.QComboBox(Form_dqa)
        self.comboBox_case.setEnabled(True)
        self.comboBox_case.setGeometry(QtCore.QRect(100, 80, 420, 20))
        self.comboBox_case.setEditable(True)
        self.comboBox_case.setObjectName("comboBox_case")
        self.comboBox_suite = QtWidgets.QComboBox(Form_dqa)
        self.comboBox_suite.setEnabled(True)
        self.comboBox_suite.setGeometry(QtCore.QRect(100, 50, 420, 20))
        self.comboBox_suite.setEditable(True)
        self.comboBox_suite.setObjectName("comboBox_suite")
        self.lineEdit_ip = QtWidgets.QLineEdit(Form_dqa)
        self.lineEdit_ip.setGeometry(QtCore.QRect(100, 20, 420, 20))
        self.lineEdit_ip.setText("")
        self.lineEdit_ip.setObjectName("lineEdit_ip")
        self.lineEdit_open = QtWidgets.QLineEdit(Form_dqa)
        self.lineEdit_open.setGeometry(QtCore.QRect(100, 110, 420, 20))
        self.lineEdit_open.setText("")
        self.lineEdit_open.setObjectName("lineEdit_open")
        self.listwidget_view = QtWidgets.QListWidget(Form_dqa)
        self.listwidget_view.setGeometry(QtCore.QRect(20, 175, 584, 361))
        self.listwidget_view.setObjectName("listwidget_view")
        self.pushButton_exit = QtWidgets.QPushButton(Form_dqa)
        self.pushButton_exit.setGeometry(QtCore.QRect(530, 20, 75, 25))
        self.pushButton_exit.setObjectName("pushButton_exit")

        self.retranslateUi(Form_dqa)
        QtCore.QMetaObject.connectSlotsByName(Form_dqa)

    def retranslateUi(self, Form_dqa):
        _translate = QtCore.QCoreApplication.translate
        Form_dqa.setWindowTitle(_translate("Form_dqa", "Advantech_DQA"))
        self.pushButton_download.setText(_translate("Form_dqa", "Download"))
        self.label_ip.setText(_translate("Form_dqa", "Server IP"))
        self.label_download.setText(_translate("Form_dqa", "Download"))
        self.label_suite.setText(_translate("Form_dqa", "Suite Folder"))
        self.label_case.setText(_translate("Form_dqa", "Case Folder"))
        self.pushButton_open.setText(_translate("Form_dqa", "Open"))
        self.pushButton_search.setText(_translate("Form_dqa", "Search"))
        self.checkBox_latest.setText(_translate("Form_dqa", "Latest Version"))
        self.pushButton_exit.setText(_translate("Form_dqa", "Exit"))
