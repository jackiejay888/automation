# -*- coding: utf-8 -*-
'''
Created on 2019/04/22

@author: ZL Chen
@title: Verify the test cases of Repeater Mode should be worked after the repeater is interrupted.
'''

import os
import sys
import time
import datetime
import threading
import logging
import logging.handlers
import configparser
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

config = configparser.ConfigParser()
config.read('..\\..\\config\\wifi_roaming.config')  # File name of log file
log_name = 'info_' + \
	time.strftime("%Y-%m-%d_%H%M%S", time.localtime()) + '.log'
logging.handlers.RotatingFileHandler(
	log_name, encoding='utf-8')  # For Chinese decode
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s : %(message)s',
					filename=log_name)  # Date and time of Log file


class wifi_roaming(object):

	def __init__(self):
		'''
		Constructor
		'''
		pass

	def open_the_browser(self, boolean):
		global driver
		global start_time_secs
		if boolean == '0':
			start_time_secs = datetime.datetime.now()
			logging.warning('Start time is: %s' % time.ctime())
		try:
			options = webdriver.ChromeOptions()  # Maximization of Chrome browser
			options.add_argument('--start-maximized')
			options.add_argument('-incognito')  # Open in incognito mode
			multi_dl_prefs = {}
			multi_dl_prefs['profile.default_content_settings.multiple-automatic-downloads'] = 1
			options.add_experimental_option(
				'prefs', multi_dl_prefs)  # Enable multiple download
			time.sleep(5)
			driver = webdriver.Chrome(chrome_options=options)
			driver.get('http://router.asus.com')
			driver.implicitly_wait(5)
			try:
				driver.find_element_by_id('login_filed')
				logging.warning('Catch the login filed.')
			except:
				for refresh in range(10):
					self.close_the_browser()
					logging.info('Refresh the page: ' + str(refresh+1))
					driver = webdriver.Chrome(chrome_options=options)
					driver.get('http://router.asus.com')
					driver.implicitly_wait(5)  # Wait for catch the windows
					time.sleep(0.5)
					try:
						driver.find_element_by_id('login_filed')
						logging.warning('Catch the login filed.')
						break
					except:
						pass
				if refresh == 9:
					logging.critical(
						'Switch Failed, please make sure the AP is launched.')
					raise
			end_time = time.ctime()
			end_time_secs = datetime.datetime.now()  # Seconds of End Time
			logging.warning('End time: %s' % end_time)
			logging.info('The AP is switch to other.')
			if boolean == '1':
				interval_time = (end_time_secs - start_time_secs).seconds
				logging.warning('The interval time is ' +
								str(interval_time) + ' seconds.')
			logging.info('The browser is opened.')
			pass
		except Exception as e:
			raise e

	def login(self):
		try:
			login_username = driver.find_element_by_id('login_username')
			print('Find the username textbox.')
			login_password = driver.find_element_by_name('login_passwd')
			print('Find the password textbox.')
			login_button = driver.find_element_by_css_selector(
				'#login_filed > div.button')
			print('Find the login button.')
			login_username.click()
			login_username.send_keys('admin')
			login_password.click()
			login_password.send_keys('ad20151225')
			login_button.click()
			pass
		except Exception as e:
			raise e

	def mac_address_check(self):
		global ip_address
		try:
			time.sleep(5)
			# Switch to subframe for mac address check
			driver.switch_to_frame(2)
			mac_address = driver.find_element_by_id('MAC')
			logging.warning('The MAC address is \"' + mac_address.text + '\"')
			if mac_address.text == '4C:ED:FB:A4:54:58':
				ip_address = '192.168.50.111'
				logging.info(
					'The AP switch to the 192.168.50.111.(Sueecssed)')
				pass
			if mac_address.text == '40:B0:76:37:BC:78':
				ip_address = '192.168.50.196'
				logging.info(
					'The AP switch to the 192.168.50.196.(Sueecssed)')
				pass
		except Exception as e:
			logging.critical('Switch failed.')
			raise e

	def reboot(self):
		global start_time_secs
		global ipv4_start_time_secs
		driver.switch_to_default_content()  # Switch to main frame for reboot button
		reboot = driver.find_element_by_css_selector(
			'#TopBanner > div > a:nth-child(4) > div > span')
		reboot.click()
		try:
			alert = driver.switch_to_alert()  # Switch to Alert elemnet
			alert.accept()  # Make the accpet of pop up
			print('Please waiting for AP to reboot......')
			start_time = time.ctime()
			# Seconds of Start Time for catch the mac address
			start_time_secs = datetime.datetime.now()
			logging.warning('Start time is: %s' % start_time)
			for percentage in range(30):
				wait_string = driver.find_element_by_css_selector(
					'#proceeding_main_txt')
				reboot_percentage = driver.find_element_by_css_selector(
					'#proceeding_txt')
				time.sleep(3)
				os.system('arp_clear.bat')  # Clear the arp cache
				# Seconds of Start Time for cache the ip address
				ipv4_start_time_secs = datetime.datetime.now()
				if reboot_percentage.text == '5% 處理中' or reboot_percentage.text == '6% 處理中':
					print('The start time of ip address catched : ' +
						  str(ipv4_start_time_secs))
					logging.warning(
						'The start time of ip address catched : ' + str(ipv4_start_time_secs))
					self.ipv4_check()
					logging.info('The Repeater is already reboot.')
					break
			self.ipv4_done()
			pass
		except Exception as e:
			raise e

	def close_the_browser(self):
		driver.implicitly_wait(5)
		driver.close()
		logging.info('The browser is Closed.')
		pass

	def ipv4_check(self):
		global thread_ipv4
		thread_ipv4 = threading.Thread(target=self._ipv4_session)
		thread_ipv4.start()
		pass

	def _ipv4_session(self):
		global ipv4_start_time_secs
		global ip_address
		global lock_ipv4
		lock_ipv4 = threading.Lock()
		lock_ipv4.acquire()
		if ip_address == '192.168.50.111':
			ip_address = '192.168.50.196'
		else:
			ip_address = '192.168.50.111'
		try:
			for arp_loop in range(10):
				os.system('ping ' + ip_address + ' -n 1')
				os.system('arp -a ' + ip_address + ' > ip_address_check.txt')
				if ip_address in open('ip_address_check.txt').read():
					print('Catch the ip address of ' + ip_address)
					logging.warning('Catch the ip address of ' + ip_address)
					ipv4_end_time_secs = datetime.datetime.now()
					print('The end time of ip address catched : ' +
						  str(ipv4_end_time_secs))
					logging.info(
						'The end time of ip address catched : ' + str(ipv4_end_time_secs))
					break
				print('Waiting for find the repeter ip address...')
			ipv4_interval_time_seconds = (
				ipv4_end_time_secs - ipv4_start_time_secs).seconds
			ipv4_interval_time_microseconds = (
				ipv4_end_time_secs - ipv4_start_time_secs).microseconds
			print('The interval time of swith to repeater is ' + str(ipv4_interval_time_seconds) +
				  '.' + str(ipv4_interval_time_microseconds) + ' seconds.')  # interval time base on ipv4
			logging.info('The interval time of swith to repeater is ' + str(ipv4_interval_time_seconds) +
						 '.' + str(ipv4_interval_time_microseconds) + ' seconds.')  # interval time base on ipv4
			pass
		except Exception as e:
			raise e

	def ipv4_done(self):
		lock_ipv4.release()
		logging.info('Finished the ipv4 thread, the thread is stoped.')
		pass

	def ping_server(self, cycle, switch):
		global thread_ping
		os.system('echo Cycle :' + str(cycle+1) +
				  ' , ' + switch + ' >> ping.txt')
		thread_ping = threading.Thread(target=self._ping_session)
		thread_ping.start()
		pass

	def _ping_session(self):
		global lock
		lock = threading.Lock()
		lock.acquire()
		os.system('ping 8.8.8.8 -t >> ping.txt')

	def ping_done(self):
		lock.release()
		self.kill_exe('ping')
		logging.info('Finished the ping thread, the thread is stoped.')
		pass

	def kill_extension_file(self, filename_extension):
		os.system('del /f /q ..\\roaming\\*.' + filename_extension)
		print('The ' + filename_extension + ' is deleted.')

	def kill_exe(self, filename):
		os.system('taskkill /f /im ' + filename + '.exe')
		print('The ' + filename + '.exe is killed.')

	def shutdown_chromedriver(self):
		self.kill_exe('chromedriver')
		print('The chromedriver is shutdown.')
		pass


if __name__ == '__main__':
	wifi_roaming = wifi_roaming()
	wifi_roaming.kill_extension_file('log')
	wifi_roaming.kill_extension_file('txt')
	wifi_roaming.kill_extension_file('spec')
	print('---------------------------------------------------------------------------------------------')
	print('\nCreated on 2019/04/22\nAuthor: ZL Chen\nTitle: Verify the test cases of Repeater Mode should be worked after the repeater is interrupted.\n')
	logging.shutdown()  # Shutdown the logging
	logging.info(
		'Verify the test cases of Repeater Mode should be worked after the repeater is interrupted.')
	User_Cycle = input('Please input the \'Cycle Times\' you want : ')
	for cycle in range(int(User_Cycle)):
		logging.info('Cycle : ' + str(cycle + 1))
		logging.info('#------------------------------------------------------------------------------------------#')
		logging.info('A switch to B.')
		wifi_roaming.open_the_browser('0')
		wifi_roaming.login()
		wifi_roaming.ping_server(cycle, 'A switch to B.')
		wifi_roaming.mac_address_check()
		wifi_roaming.reboot()
		wifi_roaming.close_the_browser()
		wifi_roaming.shutdown_chromedriver()
		logging.info('Make sure the Mac address is correct.')
		wifi_roaming.open_the_browser('1')
		wifi_roaming.login()
		wifi_roaming.mac_address_check()
		wifi_roaming.ping_done()
		wifi_roaming.close_the_browser()
		wifi_roaming.shutdown_chromedriver()
		logging.info('Waiting the repeater rebooting about 100 secs.')
		time.sleep(100)
		logging.info('The AP is rebooted.')
		logging.info('#------------------------------------------------------------------------------------------#')
		logging.info('B switch to A.')
		wifi_roaming.open_the_browser('0')
		wifi_roaming.login()
		wifi_roaming.ping_server(cycle, 'B switch to A.')
		wifi_roaming.mac_address_check()
		wifi_roaming.reboot()
		wifi_roaming.close_the_browser()
		wifi_roaming.shutdown_chromedriver()
		logging.info('Make sure the Mac address is correct.')
		wifi_roaming.open_the_browser('1')
		wifi_roaming.login()
		wifi_roaming.mac_address_check()
		wifi_roaming.ping_done()
		wifi_roaming.close_the_browser()
		wifi_roaming.shutdown_chromedriver()
		logging.info('Waiting the repeater rebooting about 100 secs.')
		time.sleep(100)
		logging.info('The AP is rebooted.')
	logging.info('The test suite of wifi_roaming is finished.')
	os.system('backup_log.bat')