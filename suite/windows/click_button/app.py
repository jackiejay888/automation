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
		read_timer = open('timer.txt', 'r')
		self.ui.lcd_show.setProperty("intValue", int(read_timer.read()))

		global shutdown_on_off
		global waiting_time
		shutdown_on_off = open('shutdown.txt', 'r').read()
		if int(shutdown_on_off) == 0:
			self.ui.disable.setChecked(True)
		else:
			self.ui.enable.setChecked(True)

		if self.ui.enable.isChecked() == True:
			waiting_time = open('waiting_time.txt', 'r').read()
		else:
			pass

		# Signal the Enable RadioButton
		self.ui.enable.toggled.connect(lambda: self.enable_disable(self.ui.enable))
		# Signal the Disable RadioButton
		self.ui.disable.toggled.connect(lambda: self.enable_disable(self.ui.disable))

		# Signal the click_button button
		self.ui.click_button.clicked.connect(self.timer)

		# Signal the log_reset button
		self.ui.log_reset.clicked.connect(self.reset)

		# Windows initial setting
		self.windows_setting()

		self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)

		self.show()

	# Shutdown enable or disable
	def enable_disable(self, enable_disable):
		global shutdown_on_off
		global waiting_time
		if enable_disable.text() == 'Shutdown Enable':
			if enable_disable.isChecked() == True:
				shutdown_on_off = 1
				try:
					write_shutdown = open('shutdown.txt', 'w')
					write_shutdown.write(str(shutdown_on_off))
				finally:
					write_shutdown.close()
				if int(open('timer.txt', 'r').read()) > 0:
					waiting_time = open('waiting_time.txt', 'r').read()
					print(waiting_time)
					print(type(waiting_time))
				else:
					self.shutdown_waiting_time()
			else:
				pass
		if enable_disable.text() == 'Shutdown Disable':
			if enable_disable.isChecked() == True:
				shutdown_on_off = 0
				try:
					write_shutdown = open('shutdown.txt', 'w')
					write_shutdown.write(str(shutdown_on_off))
				finally:
					write_shutdown.close()
			else:
				pass

	def shutdown_waiting_time(self):
		global waiting_time
		waiting_time = QtWidgets.QInputDialog()
		waiting_time, ok = waiting_time.getText(self, 'Waiting Time', 'Waiting Time:')
		try:
			waiting_time_log = open('waiting_time.txt', 'w')
			waiting_time_log.write(waiting_time)
		finally:
			waiting_time_log.close()
		if ok is True:
			if waiting_time == '':
				QMessageBox.information(self, 'Input the Waiting Time','Input the Waiting Time\n 60 or 120 seconds.')
				self.shutdown_waiting_time()
			else:
				pass
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
		global shutdown_on_off
		shutdown_on_off = 0
		timer = 0
		self.ui.click_button.setStyleSheet('')
		self.ui.log_reset.setStyleSheet('')
		self.ui.disable.setChecked(True)
		os.system('taskkill /f /im notepad.exe')
		os.system('del /f /q timer.txt')
		write_timer = open('timer.txt', 'w')
		try:
			write_timer.write(str(timer))
		finally:
			write_timer.close()
		read_timer = open('timer.txt', 'r')
		try:
			self.ui.lcd_show.setProperty("intValue", int(read_timer.read()))
		finally:
			read_timer.close()
		self.initial_match_timer()
		MessageBox = QMessageBox()
		MessageBox.information(self, 'Clear', 'Clear the log is completed.')

	def timer(self):
		read_timer = open('timer.txt', 'r')
		timer = int(read_timer.read())
		timer += 1
		write_timer = open('timer.txt', 'w')
		try:
			write_timer.write(str(timer))
		finally:
			write_timer.close()
		read_timer = open('timer.txt', 'r')
		MessageBox = QMessageBox()
		try:
			self.ui.lcd_show.setProperty("intValue", int(read_timer.read()))
			if open('match.txt', 'r').read() == open('timer.txt', 'r').read():
				self.ui.click_button.setStyleSheet('background-color: rgb(0, 255, 0);')
				self.ui.log_reset.setStyleSheet('background-color: rgb(0, 255, 0);')
				if int(shutdown_on_off) == 0:
					pass
				else:
					if waiting_time == '':
						self.shutdown_waiting_time()
					else:
						os.system('shutdown /s /t ' + open('waiting_time.txt', 'r').read())
						MessageBox.information(self, 'Shut Down', 'Shut down after ' + str(waiting_time) + ' seconds.')
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
