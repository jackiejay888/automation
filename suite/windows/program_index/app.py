'''
Created on 2019/11/19

@Title: Coding the ProgramIndex support to the test tool edition update.
@Author: ZL Chen
'''

import os
import sys
import configparser
from PyQt5.QtWidgets import QDialog, QApplication, QFileDialog, QDesktopWidget, QListWidget
from app_program_index import Ui_Form_dqa
from ftplib import FTP

config = configparser.ConfigParser()
config.read('app_program_index.config')


class AppWindow(QDialog):

	def __init__(self):
		super().__init__()
		self.ui = Ui_Form_dqa()
		self.ui.setupUi(self)
		# Initial the servier ip address
		self.ui.lineEdit_ip.setText(config.get('set', 'server_ip'))

		# Signal the search button
		self.ui.pushButton_search.clicked.connect(self.search)

		# Initial the program index's root directory
		self.ui.lineEdit_open.setText(os.getcwd())

		# Initial parser the ftp server data
		self.suite_folder()

		# Initial parser the ftp server data
		self.case_folder()

		# Highlight the select value
		self.ui.comboBox_suite.activated.connect(self.case_folder_add)

		# Initial the listwidget view
		self.ui.listwidget_view.itemClicked.connect(self.view)

		# Signal the download button
		self.ui.pushButton_download.clicked.connect(self.download)

		# Signal the open button
		self.ui.pushButton_open.clicked.connect(self.open)
		# Slot the close button
		self.ui.pushButton_close.clicked.connect(self.close)
		# Setup the windows to center
		self.center()
		self.show()

	def search(self):
		try:
			ip = self.ui.lineEdit_ip.text()
			ftp = FTP(ip)
			ftp.login(config.get('set', 'username'),
					  config.get('set', 'password'))
			ftp.cwd('/' + str(self.ui.comboBox_suite.currentText()) +
					'/' + str(self.ui.comboBox_case.currentText()))
			print(ftp.retrlines('LIST'))
			self.ui.listwidget_view.clear()
			# item = self.ui.QtWidgets.QListWidgetItem()
			# self.ui.listwidget_view.addItem(item)
			# item = self.ui.listwidget_view.item(0)
			# item.setText('N/A')
		except Exception as e:
			raise e

	def download(self):
		source = '/' + str(self.ui.comboBox_suite.currentText())
		destination = self.ui.lineEdit_open.text()
		ip = self.ui.lineEdit_ip.text()
		ftp = FTP(ip)
		ftp.login(config.get('set', 'username'), config.get('set', 'password'))
		ftp.cwd('/' + str(self.ui.comboBox_suite.currentText()))
		print(ftp.cwd('/' + str(self.ui.comboBox_suite.currentText())))

	def view(self):
		pass

	def suite_folder(self):
		ip = self.ui.lineEdit_ip.text()
		ftp = FTP(ip)
		ftp.login(config.get('set', 'username'), config.get('set', 'password'))
		ftp.cwd('/')
		number = len(ftp.nlst())
		for addItem in range(int(number)):
			self.ui.comboBox_suite.addItem('')
		for comboBox_suite_n in range(int(number)):
			# print(comboBox_suite_n)
			# print(ftp.nlst()[comboBox_suite_n])
			self.ui.comboBox_suite.setItemText(
				comboBox_suite_n, ftp.nlst()[comboBox_suite_n])

	def case_folder(self):
		ip = self.ui.lineEdit_ip.text()
		ftp = FTP(ip)
		ftp.login(config.get('set', 'username'), config.get('set', 'password'))
		ftp.cwd('/' + str(self.ui.comboBox_suite.currentText()))
		number = len(ftp.nlst())
		for addItem in range(int(number)):
			self.ui.comboBox_case.addItem('')
		for comboBox_case_n in range(int(number)):
			# print(comboBox_case_n)
			# print(ftp.nlst()[comboBox_case_n])
			self.ui.comboBox_case.setItemText(
				comboBox_case_n, ftp.nlst()[comboBox_case_n])

	def case_folder_add(self):
		self.ui.comboBox_case.clear()
		# print(str(self.ui.comboBox_suite.currentText()))
		self.case_folder()

	def open(self):
		dialog = QFileDialog()
		dialog.setFileMode(QFileDialog.Directory)
		if dialog.exec_():
			for dirname in dialog.selectedFiles():
				self.ui.lineEdit_open.setText(str(dirname))

	def center(self):
		screen = QDesktopWidget().screenGeometry()
		size = self.geometry()
		self.move((screen.width() - size.width()) / 2,
				  (screen.height() - size.height()) / 2)


if __name__ == '__main__':
	app = QApplication(sys.argv)
	appwindow = AppWindow()
	appwindow.show()
	sys.exit(app.exec_())
