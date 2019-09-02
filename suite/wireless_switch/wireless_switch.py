# -*- coding: utf-8 -*-
'''
Created on 2019/08/22

@author: ZL Chen
@title: The Wireless should be switched when the mode is changed.
'''

import os
import time
import subprocess
import pyscreenshot as ImageGrab
from selenium import webdriver
from selenium.webdriver.support.ui import Select


class wireless_switch(object):

	global sum_pass
	global sum_fail
	sum_pass = 0
	sum_fail = 0

	def initial(self, ssid_name):
		global driver
		options = webdriver.ChromeOptions()  # Maximization of Chrome browser
		options.add_argument('--start-maximized')
		options.add_argument('-incognito')  # Open in incognito mode
		multi_dl_prefs = {}
		multi_dl_prefs['profile.default_content_settings.multiple-automatic-downloads'] = 1
		options.add_experimental_option(
			'prefs', multi_dl_prefs)  # Enable multiple download
		driver = webdriver.Chrome(chrome_options=options)
		driver.get('http://router.asus.com')
		driver.implicitly_wait(5)
		try:
			driver.find_element_by_id('login_filed')
		except:
			# for refresh in range(10):
			while True:
				self.close_the_browser()
				self.reconnect_wifi(ssid_name)
				driver = webdriver.Chrome(chrome_options=options)
				driver.get('http://router.asus.com')
				driver.implicitly_wait(5)  # Wait for catch the windows
				time.sleep(0.5)
				try:
					driver.find_element_by_id('login_filed')
					break
				except:
					pass
			# if refresh == 9:
			# 	print('Switch Failed, please make sure the AP is launched.')
			# 	raise

	def login(self, user_name, password):
		try:
			driver.find_element_by_id('login_username').send_keys(user_name)
			driver.find_element_by_name('login_passwd').send_keys(password)
			driver.find_element_by_css_selector(
				'#login_filed > div.button').click()
		except Exception as e:
			raise e

	def switch_mode(self, cycle, frequence, mode):
		try:
			driver.find_element_by_id('Advanced_Wireless_Content_menu').click()
			driver.find_element_by_id('Advanced_Wireless_Content_tab').click()
			driver.find_element_by_xpath(
				u'(.//*[normalize-space(text()) and normalize-space(.)=\'頻段\'])[1]/following::select[1]').click()
			if frequence == '2.4':
				Select(driver.find_element_by_xpath(
					u'(.//*[normalize-space(text()) and normalize-space(.)=\'頻段\'])[1]/following::select[1]')).select_by_visible_text("2.4GHz")
			else:
				Select(driver.find_element_by_xpath(
					u'(.//*[normalize-space(text()) and normalize-space(.)=\'頻段\'])[1]/following::select[1]')).select_by_visible_text("5GHz")
			driver.find_element_by_xpath(
				u'(.//*[normalize-space(text()) and normalize-space(.)=\'頻段\'])[1]/following::select[1]').click()
			driver.find_element_by_name('wl_nmode_x').click()
			Select(driver.find_element_by_name('wl_nmode_x')
				   ).select_by_visible_text(mode)
			driver.find_element_by_name('wl_nmode_x').click()
			if mode == 'N/AC mixed':
				mode = 'N_AC mixed'
			self.screenshot('cycle_' + str(cycle+1) +
							'_' + frequence + '_' + mode)
			driver.find_element_by_id('applyButton').click()
		except Exception as e:
			raise e

	def close_the_browser(self):
		for loop in range(10):
			time.sleep(1)
		driver.implicitly_wait(5)
		driver.close()
		print('The browser is closed.')

	# ping the google server by windows command
	def windows_command_set(self, windows_cmds):
		global stdout
		global lines
		try:
			cmds = windows_cmds
			stdout = subprocess.Popen(
				cmds, stdout=subprocess.PIPE).communicate()[0].rstrip()
			lines = stdout.splitlines()
		except:
			raise Exception('The windows command is failed.')

	# reponse messgae by windows command
	def windows_response_get(self, value):
		global sum_pass
		global sum_fail
		if '100% ' in str(stdout):
			self._get_value(len(lines))
			sum_fail += 1
			os.system('echo The connection is Failed.(FAIL) >> ping_server.txt')
			print('The connection is Failed.(FAIL)')
		elif value in str(stdout):
			self._get_value(len(lines))
			sum_pass += 1
			os.system('echo The connection is Passed.(PASS) >> ping_server.txt')
			print('The connection is Passed.(PASS)')
		elif '25% ' in str(stdout):
			self._get_value(len(lines))
			sum_pass += 1
			os.system('echo The connection is Passed.(PASS) >> ping_server.txt')
			print('The connection is Passed.(PASS)')
		elif '50% ' in str(stdout):
			self._get_value(len(lines))
			sum_pass += 1
			os.system('echo The connection is Passed.(PASS) >> ping_server.txt')
			print('The connection is Passed.(PASS)')
		elif '75% ' in str(stdout):
			self._get_value(len(lines))
			sum_pass += 1
			os.system('echo The connection is Passed.(PASS) >> ping_server.txt')
			print('The connection is Passed.(PASS)')
		else:
			self._get_value(len(lines))
			sum_fail += 1
			os.system('echo The connection is Failed.(FAIL) >> ping_server.txt')
			print('The connection is Failed.(FAIL)')

	def _get_value(self, round_times):
		try:
			for get in range(round_times):
				if get:
					echo = str(lines[get]).split('b\'')[1]
					os.system('echo ' + echo + ' >> ping_server.txt')
		except:
			raise Exception('Cannot get the response message.')

	def run_script(self, cycle, frequence, mode, ssid_name, user_name, password):
		self.initial(ssid_name)
		self.login(user_name, password)
		self.switch_mode(cycle, frequence, mode)
		self.close_the_browser()
		self.reconnect_wifi(ssid_name)
		self.windows_command_set('ping -w 4 ' + '8.8.8.8')
		self.windows_response_get('0%')
		os.system('echo ' + 'Cycle Times: ' + str(cycle + 1) + ', Passed: ' +
				  str(sum_pass) + ', Failed: ' + str(sum_fail) + ' >> ping_server.txt')
		print('Cycle Times: ' + str(cycle + 1) + ', Passed: ' +
			  str(sum_pass) + ', Failed: ' + str(sum_fail))

	def reconnect_wifi(self, ssid_name):
		print('Counting Down the number of secs...')
		try:
			for loop in range(3):
				time.sleep(1)
				os.system('netsh wlan disconnect')
				os.system('netsh wlan disconnect')
				time.sleep(1)
				os.system('netsh wlan connect name=\"' + ssid_name + '\"')
				os.system('netsh wlan connect name=\"' + ssid_name + '\"')
				time.sleep(5)
		except Exception as e:
			raise e

	def screenshot(self, times):
		now = time.strftime('%Y%m%d_%H%M%S', time.localtime(time.time()))
		path = times + '_' + now + '.jpg'
		ImageGrab.grab().save(path)


if __name__ == '__main__':
	ws = wireless_switch()
	os.system('del /f /q *.txt')
	os.system('del /f /q *.log')
	os.system('del /f /q *.jpg')
	os.system('taskkill /f /im chromedriver.exe')
	times = int(input('Cycle times: '))
	frequence = input('Frequence (ex: 2.4 or 5): ')
	ssid_name = input('SSID name (ex: siot_dqa): ')
	user_name = input('AP\'s user name (ex: admin): ')
	password = input('AP\'s password (ex: xxxxxxxx): ')
	for cycle in range(int(times)):
		ws.run_script(cycle, frequence, 'N only', ssid_name, user_name, password)
		ws.run_script(cycle, frequence, 'Legacy', ssid_name, user_name, password)
		if frequence == '5':
			ws.run_script(cycle, frequence, 'N/AC mixed', ssid_name, user_name, password)
	os.system('echo ' + 'Total Cycle Times: ' + str(times) + ', Passed: ' +
			  str(sum_pass) + ', Failed: ' + str(sum_fail) + ' >> ping_server.txt')
	print('Total Cycle Times: ' + str(times) + ', Passed: ' +
		  str(sum_pass) + ', Failed: ' + str(sum_fail))
	os.system('.\\backup_log.bat')
