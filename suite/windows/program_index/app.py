'''
Created on 2019/11/19

@Title: Coding the ProgramIndex support to the test tool edition update.
@Author: ZL Chen
'''

import os
import sys
import configparser
# from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QFileDialog
from PyQt5.QtWidgets import QDesktopWidget, QMessageBox, QListWidget
from app_program_index import Ui_Form_dqa
from ftplib import FTP

config = configparser.ConfigParser()
config.read('app_program_index.config')


class AppWindow(QDialog):

	def __init__(self):
		super().__init__()
		self.ui = Ui_Form_dqa()
		self.ui.setupUi(self)
		#---------------------------------------------------------------------#
		self.ui.lineEdit_ip.setText(config.get('set', 'server_ip'))
		self.ui.pushButton_search.clicked.connect(self.search)
		#---------------------------------------------------------------------#
		self.ui.lineEdit_open.setText(os.getcwd())

		#---------------------------------------------------------------------#	
		self.ui.comboBox_suite.setItemText(0, config.get('set', 'suite_name'))	
		self.ui.comboBox_suite.highlighted.connect(self.suite_folder)
		#---------------------------------------------------------------------#
		self.ui.pushButton_open.clicked.connect(self.open)
		#---------------------------------------------------------------------#
		# self.ui.listwidget_view.itemClicked.connect(self.view)
		#---------------------------------------------------------------------#
		self.ui.pushButton_close.clicked.connect(self.close)
		#---------------------------------------------------------------------#
		self.center()
		self.show()

	def center(self):
		screen = QDesktopWidget().screenGeometry()
		size = self.geometry()
		self.move((screen.width() - size.width()) / 2,
				  (screen.height() - size.height()) / 2)

	def suite_folder(self):
		self.ui.comboBox_case.setEditable(True)

	def case_folder(self):
		pass

	def open(self):
		dialog = QFileDialog()
		dialog.setFileMode(QFileDialog.Directory)
		if dialog.exec_():
			for dirname in dialog.selectedFiles():
				self.ui.lineEdit_open.setText(str(dirname))

	def view(self):
		msg = QMessageBox()
		msg.information('error')
		pass

	def search(self):
		ip = self.ui.lineEdit_ip.text()
		ftp = FTP(ip)
		ftp.login(config.get('set', 'username'), config.get('set', 'password'))
		ftp.cwd('/' + str(self.ui.comboBox_suite.currentText()))
		print(ftp.retrlines('LIST'))


if __name__ == '__main__':
	app = QApplication(sys.argv)
	appwindow = AppWindow()
	appwindow.show()
	sys.exit(app.exec_())
