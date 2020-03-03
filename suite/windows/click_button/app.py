#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from click_button import Ui_Form_click_button
'''
Created on 2020/03/03

@Title: Coding the ProgramIndex support to the test tool edition update.
@Author: ZL Chen
'''

import os
import sys
import time
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtWidgets import QDesktopWidget
from PyQt5.QtWidgets import QListWidget
from PyQt5.QtWidgets import QMessageBox

os.system('pyuic5 click_button.ui > click_button.py')


class AppWindow(QDialog):

	def __init__(self):
		super().__init__()

		self.ui = Ui_Form_click_button()

		self.ui.setupUi(self)

		# Signal the click_button button
		self.ui.click_button.clicked.connect(self.timer)

		# Signal the log_reset button
		self.ui.log_reset.clicked.connect(self.reset)

		self.windows_center()  # Setup the windows to center

		self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)

		self.show()

	def reset(self):
		timer = 0
		os.system('taskkill /f /im notepad.exe')
		os.system('del /f /q timer.txt')
		write_timer = open('timer.txt', 'w')
		try:
			write_timer.write(str(timer))
		finally:
			write_timer.close()
		read_timer = open('timer.txt')
		try:
			self.ui.click_button.setText(read_timer.read())
			pass
		finally:
			read_timer.close()
		MessageBox = QMessageBox()
		MessageBox.information(self, 'Clear the log',
							   'Clear the log is completed.')

	def timer(self):
		read_timer = open('timer.txt')
		timer = int(read_timer.read())
		timer += 1
		write_timer = open('timer.txt', 'w')
		try:
			write_timer.write(str(timer))
		finally:
			write_timer.close()
		read_timer = open('timer.txt')
		try:
			self.ui.click_button.setText(read_timer.read())
			pass
		finally:
			read_timer.close()

	def windows_center(self):
		screen = QDesktopWidget().screenGeometry()
		size = self.geometry()
		self.resize(screen.width(), screen.height())
		self.ui.click_button.setGeometry(
			QtCore.QRect(0, 0, screen.width(), screen.height()))
		self.ui.log_reset.setGeometry(
			QtCore.QRect(screen.width()/2-25, 0, 50, 50))


if __name__ == '__main__':
	app = QApplication(sys.argv)
	appwindow = AppWindow()
	appwindow.show()
	sys.exit(app.exec_())
