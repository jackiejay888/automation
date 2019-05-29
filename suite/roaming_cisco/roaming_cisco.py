# -*- coding: utf-8 -*-
'''
Created on 2019/05/28

@author: ZL Chen
@title: Verify the test cases of Cisco AP mode by A to B switch should be worked.
'''

from selenium import webdriver

class roaming_cisco(object):

	def launch_chrome(self):
		global driver
		try:
			options = webdriver.ChromeOptions()  # Maximization of Chrome browser
			options.add_argument('--start-maximized')
			options.add_argument('-incognito')  # Open in incognito mode
			multi_dl_prefs = {}
			multi_dl_prefs['profile.default_content_settings.multiple-automatic-downloads'] = 1
			options.add_experimental_option('prefs', multi_dl_prefs)  # Enable multiple download
			driver = webdriver.Chrome(chrome_options=options)
			driver.get('http://Cisco:Cisco@192.168.0.21:80/')
			driver.implicitly_wait(20)
			alert = driver.switch_to_alert()  # Switch to Alert elemnet
			alert.accept()  # Make the accpet of pop up
			pass
		except Exception as e:
			raise e

	def action(self):
		print('Action')


	def shutdown_chrome(self):
		try:
			driver.implicitly_wait(5)
			driver.close()
			pass
		except Exception as e:
			raise e

	def taskkill(self, name):
		os.system('taskkill /f /im ' + name)

if __name__ == '__main__':
	cisco = roaming_cisco()
	cisco.launch_chrome()
	# cisco.shutdown_chrome()