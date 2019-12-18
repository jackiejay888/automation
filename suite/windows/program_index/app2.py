'''
Created on 2019/12/18

@Title: Coding the ProgramIndex support to the test tool edition update.
@Author: ZL Chen
'''

import os
import sys
from PyQt5.QtWidgets import QDialog, QApplication, QMainWindow
from program_index2 import Ui_MainWindow


class AppWindow(object):

	def pyuic5(self):
		os.system('pyuic5 program_index2.ui > program_index2.py')
		print('pyuic5 program_index2.ui > program_index2.py')
		pass


if __name__ == '__main__':
	AppWindow = AppWindow()
	AppWindow.pyuic5()
	app = QApplication(sys.argv)
	MainWindow = QMainWindow()
	ui = Ui_MainWindow()
	ui.setupUi(MainWindow)
	MainWindow.show()
	sys.exit(app.exec_())
