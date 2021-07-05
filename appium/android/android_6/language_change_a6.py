# -*- coding: utf-8 -*-
'''
Created on 2021/03/24

@author: ZL Chen
@title: Unittest Language change by appium server.
'''

from appium import webdriver
from nose.tools import *
from HTMLTestRunner import *
from appium.webdriver.common.touch_action import TouchAction
import os, time, uiautomator2

class take_screen_shot():
	def __init__(self, func):
		self.func = func
		self.name = func.__name__ + '.png'
	def __call__(self, *args):
		try:
			self.func(self, *args)
		finally:
			driver.get_screenshot_as_file(self.name)

class Language(unittest.TestCase):
	@classmethod
	def setUpClass(self):
		desired_caps = {}
		desired_caps['platformName'] = 'Android'
		desired_caps['platformVersion'] = '6.0'
		desired_caps['deviceName'] = 'rk3288_usc130'
		desired_caps['appPackage'] = 'com.android.settings'
		desired_caps['appActivity'] = 'com.android.settings.Settings'
		global driver
		driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

	@classmethod
	def tearDownClass(self):
		driver.quit()

	@take_screen_shot
	def test_case_01_Chinese(self):
		width = driver.get_window_size()['width']
		height = driver.get_window_size()['height']
		i = 0
		while i < 10:
			try:
				driver.find_element_by_xpath('//*[@text="Languages & input"]').click()
				break
			except Exception as e:
				driver.swipe(width / 2, height * 0.8, width / 2, height * 0.2)
				i = i + 1
		time.sleep(2)
		driver.find_element_by_xpath('//*[@text="Languages"]').click()
		time.sleep(2)
		driver.find_element_by_xpath('//*[@resource-id="com.android.settings:id/add_language"]').click()
		time.sleep(2)
		p = 0
		while p < 30:
			try:
				driver.find_element_by_xpath('//*[@text="简体中文"]').click()
				break
			except Exception as e:
				driver.swipe(width / 2, height * 0.9, width / 2, height * 0.1)
				p = p + 1
		time.sleep(1)
		driver.find_element_by_xpath('//*[@text="中国"]').click()
		time.sleep(2)
		el_0 = driver.find_element_by_xpath('//*[@resource-id="com.android.settings:id/dragList"]/android.widget.RelativeLayout[1]/android.widget.ImageView[1]')
		el_1 = driver.find_element_by_xpath('//*[@resource-id="com.android.settings:id/add_language"]')
		driver.scroll(el_0,el_1)
		time.sleep(2)
		test = driver.find_element_by_id('com.android.settings:id/add_language').text
		assert_equal(test,'添加语言')

	@take_screen_shot
	def test_case_02_English(self):
		# os.popen('adb shell am start com.android.settings/.Settings')
		# width = driver.get_window_size()['width']
		# height = driver.get_window_size()['height']
		# i = 0
		# while i < 10:
		#     try:
		#         driver.find_element_by_xpath('//*[@text="语言和输入法"]').click()
		#         break
		#     except Exception as e:
		#         driver.swipe(width / 2, height * 0.8, width / 2, height * 0.2)
		#         i = i + 1
		# time.sleep(2)
		# driver.find_element_by_xpath('//*[@text="语言"]').click()
		# time.sleep(2)
		el_0 = driver.find_element_by_xpath('//*[@content-desc="1, 简体中文（中国）"]/android.widget.ImageView[1]')
		el_1 = driver.find_element_by_xpath('//*[@resource-id="com.android.settings:id/add_language"]')
		driver.scroll(el_0,el_1)
		time.sleep(2)
		test = driver.find_element_by_id('com.android.settings:id/add_language').text
		assert_equal(test,'Add a language')

if __name__ == '__main__':
	os.system('adb shell killall atx-agent')
	report_dir=r'languagechange.html'
	re_open=open(report_dir,'wb')
	suite=unittest.TestLoader().loadTestsFromTestCase(Language)
	runner=HTMLTestRunner(
						stream=re_open,
						title=u'Android系统语言切换测试',
						description=u'测试报告')
	runner.run(suite)