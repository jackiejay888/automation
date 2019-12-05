'''
Created on 2019/11/19

@Title: Coding the ProgramIndex support to the test tool edition update.
@Author: ZL Chen
'''

import sys
from PyQt5.QtWidgets import QDialog, QApplication
from program_index import Ui_Form


class AppWindow(QDialog):
	def __init__(self):
		super().__init__()
		self.ui = Ui_Form()
		self.ui.setupUi(self)

		# # 綁上與點擊事件對應的function，所有東西都在ui底下！！
		# self.ui.pushButton_4.clicked.connect()
		self.show()


app = QApplication(sys.argv)
w = AppWindow()
w.show()
sys.exit(app.exec_())
