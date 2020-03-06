#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Created on 2020/03/03

@Title: Coding the ProgramIndex support to the test tool edition update.
@Author: ZL Chen
'''

import os
import sys
import time
from PyQt5 import QtCore, \
					QtGui, \
					QtWidgets
from PyQt5.QtWidgets import QDialog, \
							QApplication, \
							QFileDialog, \
							QDesktopWidget, \
							QListWidget, \
							QMessageBox
from click_button import Ui_Form_click_button


class AppWindow(QDialog):

	def __init__(self):
		super().__init__()

		self.ui = Ui_Form_click_button()

		self.ui.setupUi(self)

		# Initial the match.txt timer
		self.initial_match_timer()

		# Show the lcd_show value
		read_timer = open('timer.txt')
		self.ui.lcd_show.setProperty("intValue", int(read_timer.read()))

		# Signal the Enable RadioButton
		self.ui.enable.toggled.connect(lambda: self.enable_disable(self.ui.enable))

		# Signal the Disable RadioButton
		global shutdown
		shutdown = 0
		self.ui.disable.setChecked(True)
		self.ui.disable.toggled.connect(lambda: self.enable_disable(self.ui.disable))

		# Signal the click_button button
		self.ui.click_button.clicked.connect(self.timer)

		# Signal the log_reset button
		self.ui.log_reset.clicked.connect(self.reset)

		# Windows initial setting
		self.windows_setting()

		self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)

		self.show()

	def enable_disable(self, enable_disable):
		global shutdown
		if enable_disable.text() == 'Shutdown Enable':
			if enable_disable.isChecked() == True:
				shutdown = 1
			else:
				pass
		if enable_disable.text() == 'Shutdown Disable':
			if enable_disable.isChecked() == True:
				shutdown = 0
			else:
				pass

	def initial_match_timer(self):
		read_timer = open('timer.txt', 'r')
		try:
			read_timer_add = int(str(read_timer.read())) + 1
			read_timer_value = int(read_timer_add)
		finally:
			read_timer.close()

		write_timer = open('match.txt', 'w')
		try:
			write_timer.write(str(read_timer_value))
		finally:
			write_timer.close()

	def reset(self):
		timer = 0
		self.ui.click_button.setStyleSheet('')
		self.ui.log_reset.setStyleSheet('')
		os.system('taskkill /f /im notepad.exe')
		os.system('del /f /q timer.txt')
		write_timer = open('timer.txt', 'w')
		try:
			write_timer.write(str(timer))
		finally:
			write_timer.close()
		read_timer = open('timer.txt')
		try:
			self.ui.lcd_show.setProperty("intValue", int(read_timer.read()))
		finally:
			read_timer.close()
		self.initial_match_timer()
		MessageBox = QMessageBox()
		MessageBox.information(self, 'Clear', 'Clear the log is completed.')

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
		MessageBox = QMessageBox()
		try:
			self.ui.lcd_show.setProperty("intValue", int(read_timer.read()))
			if open('match.txt', 'r').read() == open('timer.txt', 'r').read():
				self.ui.click_button.setStyleSheet('background-color: rgb(0, 255, 0);')
				self.ui.log_reset.setStyleSheet('background-color: rgb(0, 255, 0);')
				if shutdown == 0:
					pass
				else:
					os.system('shutdown /s /t 180')
					MessageBox.information(self, 'Shut Down', 'Shut down after ten seconds.')
			else:
				self.ui.click_button.setStyleSheet('background-color: rgb(255, 0, 0);')
				self.ui.log_reset.setStyleSheet('background-color: rgb(255, 0, 0);')
				MessageBox.information(self, 'Error', 'The expect timer and actual timer are inconsistent.\nExpect timer : ' + open(
					'match.txt', 'r').read() + '\nActual timer : ' + open('timer.txt', 'r').read())
		finally:
			read_timer.close()

	def windows_setting(self):
		screen = QDesktopWidget().screenGeometry()
		width = screen.width() / 4
		self.move(screen.width() - width, 0)
		self.resize(width, screen.height())
		self.ui.click_button.setGeometry(
			QtCore.QRect(0, 0, width, screen.height()))
		lcd_show_size_x = 280
		lcd_show_size_y = 160
		self.ui.lcd_show.setGeometry(QtCore.QRect(width / 2 - lcd_show_size_x / 2, \
									(screen.height() / 2 - lcd_show_size_y / 2) - lcd_show_size_y, lcd_show_size_x, lcd_show_size_y))
		log_reset_size_x = 280
		log_reset_size_y = 60
		self.ui.log_reset.setGeometry(QtCore.QRect(width / 2 - log_reset_size_x / 2, \
									log_reset_size_y / 2, log_reset_size_x, log_reset_size_y))
		enable_size_x = 120
		enable_size_y = 20
		self.ui.enable.setGeometry(QtCore.QRect(width / 2 - enable_size_x / 2 - 70, \
									enable_size_y / 2, enable_size_x, enable_size_y))
		disable_size_x = 120
		disable_size_y = 20
		self.ui.disable.setGeometry(QtCore.QRect(width / 2 - disable_size_x / 2 + 70, \
									disable_size_y / 2, disable_size_x, disable_size_y))


if __name__ == '__main__':
	app = QApplication(sys.argv)
	appwindow = AppWindow()
	appwindow.show()
	sys.exit(app.exec_())
