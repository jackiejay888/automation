# -*- coding: utf-8 -*-
'''
Created on 2021/03/24

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
		desired_caps['platformVersion'] = '6.0'
		desired_caps['deviceName'] = 'rk3288_usc130'
		desired_caps['appPackage'] = 'com.android.deskclock'
		desired_caps['appActivity'] = 'com.android.deskclock.DeskClock'
		global driver
		driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

	@classmethod
	def tearDownClass(self):
		driver.quit()

	@take_screen_shot
	def test_case_01_Openclock(self):
		text = driver.find_element_by_xpath('//*[@resource-id="com.android.deskclock:id/fab"]').text
		assert_equal(text,"")
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
		time.sleep(3)
		text = driver.find_element_by_xpath('//*[@text="8:30 AM"]').text
		assert_equal(text, "8:30 AM")

if __name__ == '__main__':
	os.system('adb shell killall atx-agent')
	report_dir=r'clockapp.html'
	re_open=open(report_dir,'wb')
	suite=unittest.TestLoader().loadTestsFromTestCase(Clock)
	runner=HTMLTestRunner(
						stream=re_open,
						title=u'Android ClockAppTest',
						description=u'测试报告')
	runner.run(suite)