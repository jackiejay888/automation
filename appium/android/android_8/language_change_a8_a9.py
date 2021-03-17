# -*- coding: utf-8 -*-
'''
Created on 2021/03/05

@author: ZL Chen
@title: Unittest Language change by appium server.
'''

from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from nose.tools import *
from HTMLTestRunner import *
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
		desired_caps['platformVersion'] = '8.1.0'
		# desired_caps['platformVersion'] = '9'
		desired_caps['deviceName'] = 'usc130_160'
		# desired_caps['deviceName'] = 'sda660_q200'
		desired_caps['automationName'] = 'UiAutomator2'
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
				driver.find_element_by_xpath('//*[@text="System"]').click()
				break
			except Exception as e:
				driver.swipe(width / 2, height * 0.8, width / 2, height * 0.2)
				i = i + 1
		while i < 10:
			try:
				driver.find_element_by_xpath('//*[@text="Languages & input"]').click()
				break
			except Exception as e:
				driver.swipe(width / 2, height * 0.8, width / 2, height * 0.2)
				i = i + 1
		time.sleep(1)
		driver.find_element_by_xpath('//*[@text="Languages"]').click()
		time.sleep(1)
		driver.find_element_by_xpath('//*[@resource-id="com.android.settings:id/add_language"]').click()
		time.sleep(1)
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
		driver.scroll(el_0, el_1)
		time.sleep(2)
		test = driver.find_element_by_id('com.android.settings:id/add_language').text
		'''
		ZL Add
		'''
		time.sleep(1)
		driver.find_element_by_xpath('//*[@content-desc="向上导航"]').click()
		time.sleep(1)
		driver.find_element_by_xpath('//*[@text="语言"]').click()
		time.sleep(1)		
		''''''
		assert_equal(test, '添加语言')

	@take_screen_shot
	def test_case_02_English(self):
		# os.popen('adb shell am start com.android.settings/.Settings')
		# width = driver.get_window_size()['width']
		# height = driver.get_window_size()['height']
		# i = 0
		# while i < 10:
		# 	try:
		# 		driver.find_element_by_xpath('//*[@text="语言和输入法"]').click()
		# 		break
		# 	except Exception as e:
		# 		driver.swipe(width / 2, height * 0.8, width / 2, height * 0.2)
		# 		i = i + 1
		# time.sleep(2)
		# driver.find_element_by_xpath('//*[@text="语言"]').click()
		# time.sleep(2)
		el_0 = driver.find_element_by_xpath('//*[@content-desc="1, 简体中文（中国）"]/android.widget.ImageView[1]')
		el_1 = driver.find_element_by_xpath('//*[@resource-id="com.android.settings:id/add_language"]')
		driver.scroll(el_0, el_1)
		time.sleep(2)
		test = driver.find_element_by_id('com.android.settings:id/add_language').text
		# assert_equal(test, '添加语言')
		'''
		ZL Add
		'''
		time.sleep(1)
		driver.find_element_by_xpath('//*[@content-desc="Navigate up"]').click()
		time.sleep(1)
		driver.find_element_by_xpath('//*[@text="Languages"]').click()
		time.sleep(1)
		''''''
		assert_equal(test, 'Add a language')

	@take_screen_shot
	def test_case_03_initial(self):
		'''
		ZL Add
		'''
		time.sleep(1)
		driver.find_element_by_xpath('//*[@content-desc="More options"]').click()
		time.sleep(1)
		driver.find_element_by_xpath('//android.widget.FrameLayout[1]').click()
		time.sleep(1)
		driver.find_element_by_xpath('//*[@text="简体中文（中国）"]').click()
		time.sleep(1)
		driver.find_element_by_xpath('//*[@content-desc="Remove"]').click()
		time.sleep(1)
		# driver.find_element_by_xpath('//*[@resource-id="com.android.settings:id/content_frame"]').click() # Switch the subsettings
		# time.sleep(1)
		driver.find_element_by_xpath('//*[@resource-id="android:id/button1"]').click()
		# try:
		# 	if driver.find_element_by_xpath('//*[@text="简体中文（中国）"]'):
		# 		raise
		# except:
		# 	if driver.find_element_by_xpath('//*[@text="English (United States)"]'):
		# 		pass


if __name__ == '__main__':
	os.system('adb shell killall atx-agent')
	# os.system('del *.png *.html')
	report_dir = r'language_change.html'
	re_open = open(report_dir, 'wb')
	suite = unittest.TestLoader().loadTestsFromTestCase(Language)
	runner = HTMLTestRunner(stream=re_open,
							title=u'Android system language change by ZL',
							description=u'The test report as below.')
	runner.run(suite)
