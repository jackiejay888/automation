# -*- coding: utf-8 -*-
'''
Created on 2019/05/28

@author: ZL Chen
@title: Verify the test cases of Cisco AP mode by A to B switch should be worked.
'''

from selenium import webdriver
import time, os

class roaming_cisco(object):

	def setup(self):
		self._taskkill('chromedriver.exe')
		self.driver = webdriver.ChromeOptions()  # Maximization of Chrome browser
		self.driver.add_argument('--start-maximized')
		self.driver.add_argument('-incognito')  # Open in incognito mode
		multi_dl_prefs = {}
		multi_dl_prefs['profile.default_content_settings.multiple-automatic-downloads'] = 1
		self.driver.add_experimental_option(
			'prefs', multi_dl_prefs)  # Enable multiple download
		self.driver = webdriver.Chrome(chrome_options=self.driver)

	def launch(self):
		try:
			driver = self.driver
			user_passwd = 'Cisco'
			host_ip = '192.168.0.21'
			port = '80'
			str_link = 'ap_network-if_802-11_c.shtml'
			hyperlink = 'http://' + user_passwd + ':' + user_passwd + \
				'@' + host_ip + ':' + port + '/' + str_link
			driver.get(hyperlink)
			driver.implicitly_wait(30)
			self.setting()
			pass
		except Exception as e:
			raise e

	def setting(self):
		driver = self.driver
		driver.find_element_by_name('radio_gain_cf').click()
		driver.find_element_by_name('text_resultant_ant_gain').send_keys('100')
		driver.find_element_by_name('apply').click()
		self.accept_next_alert = True
		self._alert()
		time.sleep(35)

	def _alert(self):
		try:
			alert = self.driver.switch_to_alert()
			if self.accept_next_alert:
				alert.accept()
			else:
				alert.dismiss()
			pass
		finally:
			self.accept_next_alert = True

	def _taskkill(self, name):
		os.system('taskkill /f /im ' + name)

	def shutdown(self):
		self.driver.quit()


if __name__ == '__main__':
	# input_cycle = int(input('Please input the \'Cycle Times\' you want : '))
	input_cycle = 1
	for loop in range(input_cycle):
		cisco = roaming_cisco()
		cisco.setup()
		cisco.launch()
		cisco.shutdown()
