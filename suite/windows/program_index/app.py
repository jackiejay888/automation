'''
Created on 2019/11/19

@Title: Coding the ProgramIndex support to the test tool edition update.
@Author: ZL Chen
'''

import os
import sys
from PyQt5.QtWidgets import QDialog
from PyQt5.QtWidgets import QApplication
from app_program_index import Ui_Form
from ftplib import FTP


class AppWindow(QDialog):

	def __init__(self):
		super().__init__()
		self.ui = Ui_Form()
		self.ui.setupUi(self)
		#--------------------------------#
		self.ui.pushButton_3.clicked.connect(self.search)
		self.ui.pushButton_4.clicked.connect(self.close)
		self.show()

	def search(self):
		ip = self.ui.lineEdit_2.text()
		ftp = FTP(ip)
		ftp.login('admin', 'admin')
		ftp.retrlines('LIST')
		self.case_folder()

	def case_folder(self):
		if self.ui.comboBox_2.currentText() != '':
			self.ui.comboBox.setEditable(True)
		else:
			self.ui.comboBox.setEditable(False)


if __name__ == '__main__':
	app = QApplication(sys.argv)
	appwindow = AppWindow()
	appwindow.show()
	sys.exit(app.exec_())
