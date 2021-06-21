# -*- coding: utf-8 -*-
'''
Created on 2020/12/25
Finished on 2020/12/28

@author: ZL Chen
@title: The iDesign task create.
'''

import os
import sys
import time
import datetime
import configparser
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

config = configparser.ConfigParser()
config.read('idesign_register.ini')
current_time = time.strftime("%m%d", time.localtime())
date_current_time = str(datetime.date.today())
date_current_time_future = str(datetime.date.today() + datetime.timedelta(days=int(config.get('idesign', 'days'))-1))

class idesign_register(object):
	
	def initial(self):
		global driver
		idesign_url = "http://idesign.advantech.com/iDesignMVC3/LoginController/"
		options = webdriver.ChromeOptions() 
		options.add_argument("--incognito")
		options.add_argument("start-maximized")
		driver = webdriver.Chrome(options=options, executable_path="chromedriver.exe")
		driver.get(idesign_url)
		driver.implicitly_wait(3)

	def run(self):
		# Login
		self.click(By.NAME, "email")
		driver.find_element_by_name("email").send_keys(config.get('idesign', 'email'))
		self.click(By.NAME, "password")
		driver.find_element_by_name("password").send_keys(sys.argv[1])
		self.click(By.XPATH, "//*[@id='idesign-login-view']/div[2]/div/div/div/div/div[3]/button")
		# Switch to My project list
		self.click(By.XPATH, "//*[@id='idesign-sidebar']/nav/ul/li[3]/a")
		self.click(By.XPATH, "//*[@id='idesign-sidebar']/nav/ul/li[3]/ul/li[1]/a/span")
		# New request
		self.click(By.XPATH, "//*[@id='idesign-filter-and-table-view']/form/div[3]/div/div/table/tbody/tr/td[10]/a/img")
		# Request Information
		self.click(By.XPATH, "//*[@id='requestInfoCard']/div[4]/div/select/option[6]")
		driver.find_element_by_xpath("(//input[@type='text'])[3]").send_keys("DQA_" + config.get('idesign', 'name') + "_" + current_time)
		self.click(By.XPATH, "//*[@id='requestInfoCard']/div[5]/div/div/div[2]/button")
		self.click(By.XPATH, "//*[@id='header-and-sidebar-view']/div/section/main")
		self.click(By.XPATH, "//*[@id='requestInfoCard']/div[6]/div/select/option[6]")
		self.click(By.XPATH, "//*[@id='requestInfoCard']/div[7]/div/div/div[2]")
		self.click(By.XPATH, "//*[@id='requestInfoCard']/div[7]/div/div/div[3]/ul/li/span/span")
		self.click(By.XPATH, "//*[@id='requestInfoCard']/div[8]/div/select/option")
		# ACL_DQA_SAG
		self.click(By.XPATH, "//*[@id='requestInfoCard']/div[10]/div/select/option[10]")
		driver.find_element_by_name("ACL_DQA_SAGSample_Quantity").send_keys("1")
		Select(driver.find_element_by_name("ACL_DQA_SAGTest_team_leader")).select_by_visible_text("raymond.huang@advantech.com.tw")
		driver.find_element_by_name("ACL_DQA_SAGEstimate_Start_Date_").send_keys(date_current_time)
		driver.find_element_by_name("ACL_DQA_SAGEstimate_End_Date").send_keys(date_current_time_future)
		# PCB Information
		self.click(By.XPATH, "//*[@id='pcbInfoCard']/div[2]/div/div[1]/input")
		# Test Information
		driver.find_element_by_name("Test_Description").send_keys("DQA weekly non-project task management")
		self.click(By.XPATH, "//*[@id='requestInfoCard']/div[3]/div/i")
		for delete in range(int(config.get('idesign', 'members'))):
			self.click(By.XPATH, "//*[@id='requestInfoCard']/div[3]/div/div/div[2]/div[1]/span[1]/i")
			print('Delete the ', delete+1, 'times.')
		self.click(By.XPATH, "//*[@id='requestInfoCard']/div[3]/div/div/div[1]")
		driver.find_element_by_name("Request_Member_").clear()
		driver.find_element_by_name("Request_Member_").send_keys(config.get('idesign', 'email'))
		self.click(By.XPATH, "//*[@id='requestInfoCard']/div[3]/div/div/div[3]/ul/li[1]/span")
		sleep(2)
		self.click(By.NAME, "cont")
		# # Check the request if finished or not.
		# 	# Switch to My project list
		# self.click(By.XPATH, "//*[@id='idesign-sidebar']/nav/ul/li[3]/a")
		# self.click(By.XPATH, "//*[@id='idesign-sidebar']/nav/ul/li[3]/ul/li[1]/a/span")
		# self.click(By.XPATH, "//*[@id='idesign-filter-and-table-view']/form/div[3]/div[1]/div/table/tbody/tr/td[11]/a/img")
		# sleep(2)
		# driver.save_screenshot(date_current_time + '.png')

	def click(self, by, parameter_list):
		try:
			WebDriverWait(driver, 20).until(EC.element_to_be_clickable((by, parameter_list))).click()
			sleep(1)
		except:
			raise

	def quit(self):
		sleep(1)
		driver.quit()

if __name__ == "__main__":
	print(
		'''
		Created on 2020/12/25
		Finished on 2020/12/28
		@author: ZL Chen
		@title: The iDesign task create.
		'''
	)
	os.system('del *.png')
	os.system('taskkill /f /im chromedriver.exe')
	idesign = idesign_register()
	idesign.initial()
	idesign.run()
	idesign.quit()
