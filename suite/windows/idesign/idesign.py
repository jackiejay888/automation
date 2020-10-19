# -*- coding: utf-8 -*-
'''
Created on 2020/10/19

@author: ZL Chen
@title: The iDesign task create.
'''

from selenium import webdriver
import time
import configparser

config = configparser.ConfigParser()
config.read('idesign.config')

def run():
	print('Create the iDesign task.')
	try:
		options = webdriver.ChromeOptions()  # Maximization of Chrome browser
		options.add_argument('--start-maximized')
		options.add_argument('-incognito')  # Open in incognito mode
		multi_dl_prefs = {}
		multi_dl_prefs['profile.default_content_settings.multiple-automatic-downloads'] = 1
		options.add_experimental_option('prefs', multi_dl_prefs)  # Enable multiple download
		driver = webdriver.Chrome(chrome_options=options)
		driver.get(config.get('login', 'index'))
		driver.implicitly_wait(5)
		login_path = '#idesign-login-view > div:nth-child(2) > div > div > div > div > '
		driver.find_element_by_css_selector(login_path + 'div:nth-child(1) > input').send_keys(config.get('login', 'ac'))
		driver.find_element_by_css_selector(login_path + 'div:nth-child(2) > input').send_keys(config.get('login', 'pw'))
		driver.find_element_by_css_selector(login_path + 'div:nth-child(3) > button').click()
		pass
	except Exception as e:
		raise e
		
run()
