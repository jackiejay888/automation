'''
Created on 2019/11/19

@Title: Coding the ProgramIndex support to the test tool edition update.
@Author: ZL Chen
'''

import os
import sys
import configparser
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QFileDialog
from PyQt5.QtCore import QDir
from app_program_index import Ui_Form_dqa
from ftplib import FTP

config = configparser.ConfigParser()
config.read('app_program_index.config')

class AppWindow(QDialog):

	def __init__(self):
		super().__init__()
		self.ui = Ui_Form_dqa()
		self.ui.setupUi(self)
		self.ui.pushButton_search.clicked.connect(self.search)
		self.ui.pushButton_close.clicked.connect(self.close)
		self.ui.lineEdit_ip.setText(config.get('set', 'server_ip'))
		self.ui.lineEdit_open.setText(os.getcwd())
		self.ui.pushButton_open.clicked.connect(self.open)
		self.ui.comboBox_suite.setItemText(0, config.get('set', 'suite_name'))
		self.show()

	def search(self):
		ip = self.ui.lineEdit_ip.text()
		ftp = FTP(ip)
		ftp.login(config.get('set', 'username'), config.get('set', 'password'))
		ftp.cwd(str(self.ui.comboBox_suite.currentText()))
		print(ftp.retrlines('LIST'))
		self.case_folder()

	def open(self):
		dialog = QFileDialog()
		dialog.setFileMode(QFileDialog.Directory)
		if dialog.exec_():
			for dirname in dialog.selectedFiles():
				self.ui.lineEdit_open.setText(str(dirname))

	def case_folder(self):
		if self.ui.comboBox_suite.currentText() != '':
			self.ui.comboBox_case.setEditable(True)
		else:
			self.ui.comboBox_case.setEditable(False)


if __name__ == '__main__':
	app = QApplication(sys.argv)
	appwindow = AppWindow()
	appwindow.show()
	sys.exit(app.exec_())
