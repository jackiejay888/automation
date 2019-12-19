'''
Created on 2019/11/19

@Title: Coding the ProgramIndex support to the test tool edition update.
@Author: ZL Chen
'''

import os
import sys
from PyQt5.QtWidgets import QDialog, QApplication
from app_program_index import Ui_Form


class AppWindow(QDialog):

	def __init__(self):
		super().__init__()
		self.ui = Ui_Form()
		self.ui.setupUi(self)

		#--------------------------------#
		self.pyuic5()
		self.show()

	def pyuic5(self):
		try:
			os.system('pyuic5 app_program_index.ui -o app_program_index.py')
			pass
		except Exception as e:
			raise e


app = QApplication(sys.argv)
w = AppWindow()
w.show()
sys.exit(app.exec_())
