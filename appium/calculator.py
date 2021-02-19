#!/usr/bin/env python3
# coding=utf-8
from appium import webdriver
from nose.tools import *
import unittest
# import HtmlTestRunner
from HTMLTestRunner import *

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
		desired_caps['platformVersion'] = '10'
		desired_caps['deviceName'] = 'sda660_aim75'
		desired_caps['appPackage'] = 'com.google.android.calculator'
		desired_caps['appActivity'] = 'com.android.calculator2.Calculator'
		global driver
		driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
	@classmethod
	def tearDownClass(self):
		driver.quit()
	# @take_screen_shot
	# def test_case_01_open(self):
	#     text = driver.find_element_by_id('com.google.android.calculator:id/formula').text
	#     assert_equal(text,"")
	@take_screen_shot
	def test_case_01_plus(self):
		driver.find_element_by_id('com.google.android.calculator:id/digit_1').click()
		driver.find_element_by_id('com.google.android.calculator:id/op_add').click()
		driver.find_element_by_id('com.google.android.calculator:id/digit_2').click()
		driver.find_element_by_id('com.google.android.calculator:id/eq').click()
		text = driver.find_element_by_xpath('//*[@resource-id="com.google.android.calculator:id/formula_container"]').text
		assert_equal(text,"3")
	@take_screen_shot
	def test_case_02_sub(self):
		driver.find_element_by_id('com.google.android.calculator:id/digit_5').click()
		driver.find_element_by_id('com.google.android.calculator:id/op_sub').click()
		driver.find_element_by_id('com.google.android.calculator:id/digit_3').click()
		driver.find_element_by_id('com.google.android.calculator:id/eq').click()
		text = driver.find_element_by_xpath('//*[@resource-id="com.google.android.calculator:id/formula_container"]').text
		assert_equal(text,"2")
	@take_screen_shot
	def test_case_03_mul(self):
		driver.find_element_by_id('com.google.android.calculator:id/digit_2').click()
		driver.find_element_by_id('com.google.android.calculator:id/op_mul').click()
		driver.find_element_by_id('com.google.android.calculator:id/digit_3').click()
		driver.find_element_by_id('com.google.android.calculator:id/eq').click()
		text = driver.find_element_by_xpath('//*[@resource-id="com.google.android.calculator:id/formula_container"]').text
		assert_equal(text,"6")
	@take_screen_shot
	def test_case_04_div(self):
		driver.find_element_by_id('com.google.android.calculator:id/digit_9').click()
		driver.find_element_by_id('com.google.android.calculator:id/op_div').click()
		driver.find_element_by_id('com.google.android.calculator:id/digit_3').click()
		driver.find_element_by_id('com.google.android.calculator:id/eq').click()
		text = driver.find_element_by_xpath('//*[@resource-id="com.google.android.calculator:id/formula_container"]').text
		assert_equal(text,"3")

if __name__ == '__main__':
	# unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='report',
	# 													   report_title='Android计算器测试报告',encoding='utf-8'))
	report_dir = r'CalculatorTest.html'
	re_open = open(report_dir,'wb')
	suite = unittest.TestLoader().loadTestsFromTestCase(CalTestCase)
	runner = HTMLTestRunner(stream=re_open,
							title=u'Android 计算器自动化',
							description=u'测试报告')
	runner.run(suite)