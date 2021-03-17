# -*- coding: utf-8 -*-
'''
Created on 2021/02/19

@author: ZL Chen
@title: Unittest calculator for android 8.1 and 9 by appium server.
'''

from appium import webdriver
from nose.tools import *
from HTMLTestRunner import *
from time import sleep
import os


class take_screen_shot():
	def __init__(self, func):
		self.func = func
		self.name = func.__name__ + ' (__main__.CalTestCase).png'

	def __call__(self, *args):
		try:
			self.func(self, *args)
		finally:
			driver.get_screenshot_as_file(self.name)

class CalTestCase(unittest.TestCase):
	@classmethod
	def setUpClass(self):
		desired_caps = {}
		desired_caps['platformName'] = 'Android'
		desired_caps['platformVersion'] = '9'
		# desired_caps['platformVersion'] = '8.1.0'
		desired_caps['deviceName'] = 'sda660_q200'
		# desired_caps['deviceName'] = 'usc130_160'
		desired_caps['automationName'] = 'UiAutomator2'
		desired_caps['appPackage'] = 'com.android.calculator2'
		desired_caps['appActivity'] = 'com.android.calculator2.Calculator'
		global driver
		driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

	@classmethod
	def tearDownClass(self):
		driver.quit()

	@take_screen_shot
	def test_case_01_open(self):
		text = driver.find_element_by_id('com.android.calculator2:id/result').text
		assert_equal(text, '')

	@take_screen_shot
	def test_case_02_plus(self):
		sleep(1)
		driver.find_element_by_id('com.android.calculator2:id/digit_1').click()
		sleep(1)
		driver.find_element_by_id('com.android.calculator2:id/op_add').click()
		sleep(1)
		driver.find_element_by_id('com.android.calculator2:id/digit_2').click()
		sleep(1)
		driver.find_element_by_id('com.android.calculator2:id/eq').click()
		sleep(1)
		text = driver.find_element_by_xpath('//*[@resource-id="com.android.calculator2:id/result"]').text
		sleep(1)
		assert_equal(text, '3')

	@take_screen_shot
	def test_case_03_sub(self):
		sleep(1)
		driver.find_element_by_id('com.android.calculator2:id/digit_5').click()
		sleep(1)
		driver.find_element_by_id('com.android.calculator2:id/op_sub').click()
		sleep(1)
		driver.find_element_by_id('com.android.calculator2:id/digit_3').click()
		sleep(1)
		driver.find_element_by_id('com.android.calculator2:id/eq').click()
		sleep(1)
		text = driver.find_element_by_xpath('//*[@resource-id="com.android.calculator2:id/result"]').text
		sleep(1)
		assert_equal(text, '2')

	@take_screen_shot
	def test_case_04_mul(self):
		sleep(1)
		driver.find_element_by_id('com.android.calculator2:id/digit_2').click()
		sleep(1)
		driver.find_element_by_id('com.android.calculator2:id/op_mul').click()
		sleep(1)
		driver.find_element_by_id('com.android.calculator2:id/digit_3').click()
		sleep(1)
		driver.find_element_by_id('com.android.calculator2:id/eq').click()
		sleep(1)
		text = driver.find_element_by_xpath('//*[@resource-id="com.android.calculator2:id/result"]').text
		sleep(1)
		assert_equal(text, '6')

	@take_screen_shot
	def test_case_05_div(self):
		sleep(1)
		driver.find_element_by_id('com.android.calculator2:id/digit_9').click()
		sleep(1)
		driver.find_element_by_id('com.android.calculator2:id/op_div').click()
		sleep(1)
		driver.find_element_by_id('com.android.calculator2:id/digit_3').click()
		sleep(1)
		driver.find_element_by_id('com.android.calculator2:id/eq').click()
		sleep(1)
		text = driver.find_element_by_xpath('//*[@resource-id="com.android.calculator2:id/result"]').text
		sleep(1)
		assert_equal(text, '3')


if __name__ == '__main__':
	os.system('adb shell killall atx-agent')
	# os.system('del *.png *.html')
	report_dir = r'CalculatorTest.html'
	re_open = open(report_dir, 'wb')
	suite = unittest.TestLoader().loadTestsFromTestCase(CalTestCase)
	runner = HTMLTestRunner(stream=re_open,
							title=u'Automated testing of android environment by ZL',
							description=u'The test report as below.')
	runner.run(suite)
