'''
Created on 2019/11/19

@Title: Coding the ProgramIndex support to the test tool edition update.
@Author: ZL Chen
'''

import os
import sys
from PyQt5.QtWidgets import QDialog, QApplication
from program_index import Ui_Form


class AppWindow(QDialog):

	def __init__(self):
		super().__init__()
		self.ui = Ui_Form()
		self.ui.setupUi(self)

		# # 綁上與點擊事件對應的function，所有東西都在ui底下！！
		self.pyuic5()
		self.show()

	def pyuic5(self):
		try:
			os.system('pyuic5 program_index.ui -o program_index.py')
			print('pyuic5 program_index.ui -o program_index.py')
			pass
		except Exception as e:
			raise e

	def ftp(self):
		pass

	def test_suits(self):
		pass

	def test_cases(self):
		pass

	def download(self):
		pass

	def open(self):
		pass

	def search(self):
		pass

	def exit(self):
		pass

app = QApplication(sys.argv)
w = AppWindow()
w.show()
sys.exit(app.exec_())
