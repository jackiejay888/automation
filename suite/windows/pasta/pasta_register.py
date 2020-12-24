# -*- coding: utf-8 -*-
'''
Created on 2020/12/24
Finished on 2020/12/24

@author: ZL Chen
@title: Pasta Registration for Willie
'''

import os
import configparser
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

config = configparser.ConfigParser(allow_no_value=True)
config.read('phone_number.ini')

class pasta(object):

	def initial(self):
		global driver
		pasta_url = "https://ocard.co/q?s=yZEw5x&qtk=pm1kOl"
		options = webdriver.ChromeOptions() 
		options.add_argument("--incognito")
		options.add_argument("start-maximized")
		driver = webdriver.Chrome(options=options, executable_path="chromedriver.exe")
		driver.get(pasta_url)

	def run(self, number):
		self.click(By.ID, "start")
		self.next('2')
		self.click(By.XPATH, "//*[@class=\"next next_\"]")
		self.next('3')
		self.next('4')
		for loop in range(6):
			print("Click the NEXT.", loop+1, "times.")
			self.click(By.XPATH, "//*[@class=\"next next_\"]")
		self.next('10')
		self.next('11')
		self.click(By.XPATH, "//*[@class=\"next complete\"]")
		driver.find_element_by_name("name").send_keys("adv")
		self.click(By.XPATH, "//*[@id=\"infoForm\"]/select/option[2]")
		self.click(By.XPATH, "//*[@id=\"infoForm\"]/input[2]")
		self.click(By.XPATH, "/html/body/div[7]/button")
		self.click(By.XPATH, "//*[@id=\"infoForm\"]/input[3]")
		driver.find_element_by_name("cell").send_keys(number)
		self.click(By.XPATH, "/html/body/div[9]/a")
		driver.save_screenshot(number + '.png')
		self.click(By.XPATH, "//*[@id=\"confirm\"]/div/div/div[2]/button[2]")
		self.click(By.XPATH, "//*[@id=\"alert\"]/div/div/div[2]/button")

	def next(self, parameter_list):
		self.click(By.XPATH, "/html/body/div[2]/div/div/div/div[" + parameter_list + "]/div/div/div/ul/li[1]/a")

	def click(self, by, parameter_list):
		try:
			WebDriverWait(driver, 20).until(EC.element_to_be_clickable((by, parameter_list))).click()
			sleep(1)
		except:
			raise

	def verify(self):
		number = list()
		number_enable = config.items('number')
		length_number_enable = len(number_enable)
		for p in range(length_number_enable):
			number.append(number_enable[p][0])
		return number, length_number_enable

	def quit(self):
		sleep(2)
		driver.quit()

if __name__ == "__main__":
	print(
		'''
		Created on 2020/12/24 10:00 A.M.
		Finished on 2020/12/24 14:00 A.M.
		@author: ZL Chen
		@title: Pasta Registration for Willie.
		'''
	)
	os.system('del *.png')
	os.system('taskkill /f /im chromedriver.exe')
	p = pasta()
	n, l_n_e = p.verify()
	for item in range(l_n_e):
		p.initial()
		p.run(n[item])
		p.quit()
