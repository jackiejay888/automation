# -*- coding: utf-8 -*-
'''
Created on 2020/08/18
Modified on 2020/08/24

@author: ZL Chen
@title: Verify the DUT on/off times after reboot.
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


class reboot_check_py(object):

	def create_log(self):
		os.system('echo The reboot check result. > testtool\\' + self.strftime())

	def check(self, reboot_times):
		os.system('echo Start:\tWaiting the device reboot ' + parameter_setting.get(
			'reboot_check_py', 'adb_wait_secs') + ' secs. >> testtool\\' + self.strftime())
		print('Start:\tWaiting the device reboot', parameter_setting.get(
			'reboot_check_py', 'adb_wait_secs'), 'secs.')
		for reboot in range(int(parameter_setting.get('reboot_check_py', 'adb_wait_secs'))):
			sleep(1)
			if (reboot + 1) % int(parameter_setting.get('reboot_check_py', 'adb_wait_secs')) == 0 and reboot != 0:
				os.system('echo It\'s already wait the ' + str(reboot +
															   1) + ' secs. >> testtool\\' + self.strftime())
				print('It\'s already wait the', str(reboot + 1), 'secs.')
				boolean = self.serial_number_check(reboot_times)
		os.system('echo End:\tWaiting the device reboot ' + parameter_setting.get(
			'reboot_check_py', 'adb_wait_secs') + ' secs is done. >> testtool\\' + self.strftime())
		print('End:\tWaiting the device reboot', parameter_setting.get(
			'reboot_check_py', 'adb_wait_secs'), 'secs is done.')
		return boolean

	def serial_number_check(self, reboot_times):
		adb_ouput = check_output(["adb", "devices"])
		devices_id = str(adb_ouput.split()[-2])
		if devices_id == 'b\'devices\'':
			os.system('echo Not Find a new device. >> testtool\\' +
					  self.strftime())
			print('Not Find a new device.')
			return False
		else:
			os.system('echo Find a new device. >> testtool\\' + self.strftime())
			print('Find a new device:', devices_id.split('b')[-1])
			return True

	def screenshot(self, reboot_times):
		screen_time = 'airplane_' + reboot_times + '.png'
		self.screen(
			r'adb shell /system/bin/screencap -p /mnt/sdcard/' + screen_time)
		self.screen(r'adb pull /mnt/sdcard/' + screen_time +
					' ./testtool/' + screen_time)
		os.system('adb shell rm -rf /mnt/sdcard/' + screen_time)

	def strftime(self):
		return parameter_setting.get('project_name', 'name') + '_reboot_check_py_' + datetime + '.log'

	def screen(self, cmd):
		screenExecute = subprocess.Popen(
			str(cmd), stderr=subprocess.PIPE, stdout=subprocess.PIPE, shell=True)
		stdout, stderr = screenExecute.communicate()

	def run(self):
		self.create_log()
		for reboot_times in range(int(parameter_setting.get('reboot_check_py', 'reboot_times'))):
			os.system('adb shell reboot')
			print('The system is rebooting.')
			os.system('echo Reboot times: ' + str(reboot_times + 1) +
					  ' >> testtool\\' + self.strftime())
			print('Reboot times: ' + str(reboot_times + 1))
			boolean = self.check(str(reboot_times + 1))
			if boolean == False:
				os.system(
					'echo The reboot check is failed. >> testtool\\' + self.strftime())
				print('The reboot check is failed.')
				os.system('echo FAIL >> testtool\\' + self.strftime())
				os.system('echo ' + self.strftime() + ' >> project_name.log')
				break
			if boolean == True:
				os.system(
					'echo The reboot check is passed. >> testtool\\' + self.strftime())
				print('The reboot check is passed.')
				self.screenshot(str(reboot_times + 1))
		if boolean == True:
			os.system('echo PASS >> testtool\\' + self.strftime())
			os.system('echo ' + self.strftime() + ' >> project_name.log')

if __name__ == '__main__':
	reboot_check_py = reboot_check_py()
	reboot_check_py.run()
