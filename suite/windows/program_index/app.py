#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Created on 2019/11/19

@Title: Coding the ProgramIndex support to the test tool edition update.
@Author: ZL Chen
'''

import os
import sys
import configparser
from PyQt5.QtWidgets import QDialog, QApplication, QFileDialog, QDesktopWidget, QListWidget, QMessageBox
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

		self.ui.pushButton_search.clicked.connect(
			self.search)  # Signal the search button

		self.ui.listwidget_view.clear()  # Initial listwidget_view content

		# Initial the program index's root directory
		self.ui.lineEdit_open.setText(os.getcwd())

		self.suite_folder()  # Initial parser the ftp server data

		self.case_folder()  # Initial parser the ftp server data

		self.ui.comboBox_suite.activated.connect(
			self.case_folder_add)  # Highlight the select value

		self.ui.listwidget_view.itemClicked.connect(
			self.view)  # Initial the listwidget view

		self.ui.pushButton_open.clicked.connect(
			self.open)  # Signal the open button

		self.ui.pushButton_exit.clicked.connect(
			self.close)  # Signal the close button

		self.center()  # Setup the windows to center

		self.show()

	def search(self):
		ip = self.ui.lineEdit_ip.text()
		ftp = FTP(ip)
		ftp.login(config.get('set', 'username'),
				  config.get('set', 'password'))
		ftp.cwd('/' + str(self.ui.comboBox_suite.currentText()) +
				'/' + str(self.ui.comboBox_case.currentText()))
		number = len(ftp.nlst())
		self.ui.listwidget_view.clear()
		for listwidget_view in range(int(number)):
			self.ui.listwidget_view.addItem(ftp.nlst()[listwidget_view])

	def host_to_local(self, get_item):
		host = '/' + str(self.ui.comboBox_suite.currentText()) + \
			'/' + str(self.ui.comboBox_case.currentText())
		local = self.ui.lineEdit_open.text()
		ip = self.ui.lineEdit_ip.text()
		ftp = FTP(ip)
		ftp.login(config.get('set', 'username'), config.get('set', 'password'))
		ftp.cwd(host)
		if get_item != '':
			print(host + get_item)
			MessageBox = QMessageBox()
			MessageBox.information(self, 'Download the ' + get_item,
								   'Downloading the \"' + get_item + '\"yy from Host to local.')
		else:
			pass

	def view(self, item):
		get_item = item.text()
		self.host_to_local(get_item)

	def suite_folder(self):
		ip = self.ui.lineEdit_ip.text()
		ftp = FTP(ip)
		ftp.login(config.get('set', 'username'), config.get('set', 'password'))
		ftp.cwd('/')
		number = len(ftp.nlst())
		for addItem in range(int(number)):
			self.ui.comboBox_suite.addItem('')
		for comboBox_suite_n in range(int(number)):
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
			self.ui.comboBox_case.setItemText(
				comboBox_case_n, ftp.nlst()[comboBox_case_n])

	def case_folder_add(self):
		self.ui.comboBox_case.clear()
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
