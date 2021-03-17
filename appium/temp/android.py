# -*- coding: utf-8 -*-
'''
Created on 2021/02/18

@author: ZL Chen
@title: Unittest by appium server.
'''

from appium import webdriver
from nose.tools import *
from HTMLTestRunner import *
import unittest, os

class take_scren_shot(unittest.TestCase):

	def test_Case_01_MemFree(self):
		print('test_Case_01_MemFree')
		with os.popen('adb shell \"cat /proc/meminfo | grep MemFree\"') as f:
			meminformation = f.read()
			print(meminformation)

	def test_Case_02_UICheck(self):
		print('test_Case_02_UICheck')

	def test_Case_03_KeyEvent(self):
		print('test_Case_03_Other')
		for i in range(3):
			os.system('adb shell input keyevent 26')
			os.system('adb shell input keyevent 26')

if __name__ == '__main__':
	unittest.main()