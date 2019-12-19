'''
Created on 2019/12/19

@Title: Coding the ProgramIndex support to the test tool edition update.
@Author: ZL Chen
'''

import sys
from PyQt5.QtWidgets import QDialog, QApplication
from zl_program_index import Ui_Form  # MyFirstUI 是你的.py檔案名字


class AppWindow(QDialog):

	def __init__(self):
		super().__init__()
		self.ui = Ui_Form()
		self.ui.setupUi(self)

		#--------------------------------#
		self.ui.pushButton.clicked.connect(self.pushButton_Click)
		self.show()

	def pushButton_Click(self):
		self.ui.label.setText("Hello World")


if __name__ == '__main__':
	app = QApplication(sys.argv)
	w = AppWindow()
	w.show()
	sys.exit(app.exec_())
