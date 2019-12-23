'''
Created on 2019/11/19

@Title: Coding the ProgramIndex support to the test tool edition update.
@Author: ZL Chen
'''

import os
import sys
import sqlite3
from PyQt5.QtWidgets import QDialog, QApplication, QVBoxLayout, QMessageBox
from app_program_index import Ui_Form
from ftplib import FTP

class AppWindow(QDialog):

	def __init__(self):
		super().__init__()
		self.ui = Ui_Form()
		self.ui.setupUi(self)		

		#--------------------------------#
		self.ui.pushButton_3.clicked.connect(self.search)

		#--------------------------------#
		self.ui.pushButton_2.clicked.connect(self.download_to)

		#--------------------------------#
		self.show()

	def download_to(self):
		# self.ui.lineEdit.setText(_translate(self, '11111'))
		pass

	def search(self):
		ip = self.ui.lineEdit_2.text()
		ftp = FTP(ip)
		# ip = '172.17.9.225'
		# ftp.login('dqa','dqa8101d')
		ftp.login('admin','admin')
		ftp.retrlines('LIST')

		self.case_folder()


	def case_folder(self):
		if self.ui.comboBox_2.currentText() != '':
			self.ui.comboBox.setEditable(True)
		else:
			self.messagebox_warning('case_folder')

	def messagebox_warning(self, value):
		msg = QMessageBox()
		msg.setIcon(QMessageBox.Information)
		msg.setText("This is a message box")
		msg.setInformativeText("This is additional information")
		msg.setWindowTitle(value)
		msg.setDetailedText("The details are as follows:")


if __name__ == '__main__':
	app = QApplication(sys.argv)
	w = AppWindow()
	w.show()
	sys.exit(app.exec_())