# -*- coding: utf-8 -*-
'''
Created on 2019/09/10

@author: ZL Chen
@title: AutoIT for Calculator UI..
'''

import win32com.client
import os

autoit = win32com.client.Dispatch("AutoItX3.Control")
list_calculator = ['{+}', '{-}', '{*}', '{/}']


class autoit_control(object):

	def run(self):
		os.system('taskkill /f /im Calculator.exe')
		initial = 0
		number = '123456789'
		autoit.Run('calc.exe')
		autoit.Sleep(1000)
		autoit.WinActivate(u'小算盤 ‎- 小算盤', '')
		for loop in range(4):
			initial = initial + 1
			autoit.Send(number)
			autoit.Sleep(500)
			if initial == 4:
				break
			autoit.Send(list_calculator[initial])
		print('pass')
		pass


if __name__ == '__main__':
	autoit_control = autoit_control()
	autoit_control.run()
