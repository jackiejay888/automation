# -*- coding: utf-8 -*-
'''
Created on 2020/08/18
Modified on 2020/08/24

@author: ZL Chen
@title: Verify the DUT on/off times after shutdown.
'''

import os
import sys
import time
import configparser
import subprocess
from subprocess import check_output
from time import sleep

# parameter_setting.ini
parameter_value = {}
parameter_setting = configparser.ConfigParser()
parameter_setting.read('.\ini\\parameter_setting.ini', encoding='utf-8')
datetime = time.strftime("%Y%m%d_%H%M%S", time.localtime())


class shutdown_check_py(object):

	def create_log(self):
		os.system('echo The shutdown check result. > testtool\\' + self.strftime())

	def check(self, shutdown_time):
		os.system('echo Start:\tWaiting the device shutdown ' + parameter_setting.get('shutdown_check_py', 'adb_wait_secs') + ' secs. >> testtool\\' + self.strftime())
		print('Start:\tWaiting the device shutdown', parameter_setting.get('shutdown_check_py', 'adb_wait_secs'), 'secs.')
		for shutdown in range(int(parameter_setting.get('shutdown_check_py', 'adb_wait_secs'))):
			sleep(1)
			if (shutdown + 1) % int(parameter_setting.get('shutdown_check_py', 'adb_wait_secs')) == 0 and shutdown != 0:
				os.system('echo It\'s already wait the ' + str(shutdown + 1) + ' secs. >> testtool\\' + self.strftime())
				print('It\'s already wait the', str(shutdown + 1), 'secs.')
				boolean = self.serial_number_check(shutdown_time)
		os.system('echo End:\tWaiting the device shutdown ' + parameter_setting.get('shutdown_check_py', 'adb_wait_secs') + ' secs is done. >> testtool\\' + self.strftime())
		print('End:\tWaiting the device shutdown', parameter_setting.get('shutdown_check_py', 'adb_wait_secs'), 'secs is done.')
		return boolean

	def serial_number_check(self, shutdown_time):
		adb_ouput = check_output(["adb", "devices"])
		devices_id = str(adb_ouput.split()[-2])
		if devices_id == 'b\'devices\'':
			os.system('echo Not Find a new device. >> testtool\\' + self.strftime())
			print('Not Find a new device.')
			return False
		else:
			os.system('echo Find a new device. >> testtool\\' + self.strftime())
			print('Find a new device:', devices_id.split('b')[-1])
			return True

	def screenshot(self, shutdown_time):
		screen_time = 'shutdown_' + shutdown_time + '.png'
		self.screen(r'adb shell /system/bin/screencap -p /mnt/sdcard/' + screen_time)
		self.screen(r'adb pull /mnt/sdcard/' + screen_time + ' ./testtool/' + screen_time)
		os.system('adb shell rm -rf /mnt/sdcard/' + screen_time)

	def strftime(self):
		return parameter_setting.get('project_name', 'name') + '_shutdown_check_py_' + datetime + '.log'

	def screen(self, cmd):
		screenExecute = subprocess.Popen(str(cmd), stderr=subprocess.PIPE, stdout=subprocess.PIPE, shell=True)
		stdout, stderr = screenExecute.communicate()

	def run(self):
		self.create_log()
		for shutdown_time in range(int(parameter_setting.get('shutdown_check_py', 'shutdown_time'))):
			os.system('adb shell reboot -p')
			print('The system is shutdowning.')
			os.system('echo shutdown times: ' + str(shutdown_time + 1) + ' >> testtool\\' + self.strftime())
			print('shutdown times: ' + str(shutdown_time + 1))
			boolean = self.check(str(shutdown_time + 1))
			if boolean == False:
				os.system('echo The shutdown check is failed. >> testtool\\' + self.strftime())
				print('The shutdown check is failed.')
				os.system('echo FAIL >> testtool\\' + self.strftime())
				os.system('echo ' + self.strftime() + ' >> project_name.log')
				break
			if boolean == True:
				os.system('echo The shutdown check is passed. >> testtool\\' + self.strftime())
				print('The shutdown check is passed.')
				self.screenshot(str(shutdown_time + 1))
		if boolean == True:
			os.system('echo PASS >> testtool\\' + self.strftime())
			os.system('echo ' + self.strftime() + ' >> project_name.log')

if __name__ == '__main__':
	shutdown_check_py = shutdown_check_py()
	shutdown_check_py.run()
