# -*- coding: utf-8 -*-
'''
Created on 2021/03/05

@author: ZL Chen
@title: Unittest by appium server.
'''

from appium import webdriver
from nose.tools import *
from HTMLTestRunner import *
import os

class take_screen_shot():
	def __init__(self, func):
		self.func = func
		self.name = func.__name__ + '.png'
	def __call__(self, *args):
		try:
			self.func(self, *args)
		finally:
			driver.get_screenshot_as_file(self.name)

class Clock(unittest.TestCase):
	@classmethod
	def setUpClass(self):
		desired_caps = {}
		desired_caps['platformName'] = 'Android'
		# desired_caps['platformVersion'] = '8.1.0'
		desired_caps['platformVersion'] = '9'
		# desired_caps['deviceName'] = 'usc130_160'
		desired_caps['deviceName'] = 'sda660_q200'
		desired_caps['automationName'] = 'UiAutomator2'
		desired_caps['appPackage'] = 'com.android.deskclock'
		desired_caps['appActivity'] = 'com.android.deskclock.DeskClock'
		global driver
		driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

	@classmethod
	def tearDownClass(self):
		driver.quit()

	@take_screen_shot
	def test_case_01_Openclock(self):		
		driver.find_element_by_xpath('//*[@text="ALLOW"]').click()
		time.sleep(1)
		text = driver.find_element_by_xpath('//*[@resource-id="com.android.deskclock:id/fab"]').text
		assert_equal(text, '')
		time.sleep(2)

	@take_screen_shot
	def test_case_02_Alarm(self):
		driver.find_element_by_xpath('//*[@content-desc="Alarm"]').click()
		time.sleep(1)
		driver.find_element_by_id('com.android.deskclock:id/onoff').click()
		time.sleep(1)
		driver.find_element_by_xpath('//*[@text="8:30 AM"]').click()
		time.sleep(1)
		driver.find_element_by_xpath('//*[@content-desc="10"]').click()
		time.sleep(1)
		driver.find_element_by_xpath('//*[@content-desc="20"]').click()
		time.sleep(1)
		driver.find_element_by_xpath('//*[@resource-id="android:id/button1"]').click()
		time.sleep(1)
		text = driver.find_element_by_xpath('//*[@text="10:20 AM"]').text
		assert_equal(text, "10:20 AM")
		time.sleep(2)

	@take_screen_shot
	def test_case_03_CloseAlarm(self):
		driver.find_element_by_xpath('//*[@text="10:20 AM"]').click()
		time.sleep(1)
		driver.find_element_by_xpath('//*[@content-desc="8"]').click()
		time.sleep(1)
		driver.find_element_by_xpath('//*[@content-desc="30"]').click()
		time.sleep(1)
		driver.find_element_by_xpath('//*[@resource-id="android:id/button1"]').click()
		time.sleep(3)
		# driver.find_element_by_xpath('//*[@text="On"]').click()
		driver.find_element_by_xpath('//*[@text="ON"]').click()
		time.sleep(3)
		text = driver.find_element_by_xpath('//*[@text="8:30 AM"]').text
		assert_equal(text, "8:30 AM")

if __name__ == '__main__':
	os.system('adb shell killall atx-agent')
	# os.system('del *.png *.html')
	report_dir = r'clock_app.html'
	re_open = open(report_dir,'wb')
	suite = unittest.TestLoader().loadTestsFromTestCase(Clock)
	runner = HTMLTestRunner(stream=re_open,
							title=u'Automated testing of android environment by ZL',
							description=u'The test report as below.')
	runner.run(suite)
