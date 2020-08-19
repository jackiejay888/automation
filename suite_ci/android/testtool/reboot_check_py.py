# -*- coding: utf-8 -*-
'''
Created on 2020/08/18

@author: ZL Chen
@title: Verify the DUT on/off times after reboot.
'''

import os
import sys
import time
import configparser
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

	def check(self):
		print('Start:\tWaiting the device reboot', sys.argv[1], 'secs.')
		for reboot in range(int(sys.argv[1])):
			sleep(1)
			if (reboot + 1) % 30 == 0 and reboot != 0:
				print('It\'s already waiting the', str(reboot + 1), 'secs.')
				os.system('echo It\'s already waiting the ' +
						  str(reboot + 1) + ' secs. >> testtool\\' + self.strftime())
				self.serial_number_check()
		print('End:\tWaiting the device reboot', sys.argv[1], 'secs is done.')

	def serial_number_check(self):
		adb_ouput = check_output(["adb", "devices"])
		devices_id = str(adb_ouput.split()[-2])
		if devices_id == 'b\'devices\'':
			print('Not Find a new device.')
			os.system('echo Not Find a new device. >> testtool\\' +
					  self.strftime())
			return False
		else:
			print('Find a new device.')
			os.system('echo Find a new device. >> testtool\\' + self.strftime())
			return True

	def strftime(self):
		return parameter_setting.get('project_name', 'name') + '_reboot_check_py_' + \
			datetime + '.log'


if __name__ == '__main__':
	reboot_check_py = reboot_check_py()
	reboot_check_py.create_log()
	reboot_check_py.check()
	boolean = reboot_check_py.serial_number_check()
	if boolean == True:
		os.system('echo PASS >> testtool\\' + reboot_check_py.strftime())
		os.system('echo ' + reboot_check_py.strftime() +
				  ' >> project_name.log')
	else:
		os.system('echo FAIL >> testtool\\' + reboot_check_py.strftime())
		os.system('echo ' + reboot_check_py.strftime() +
				  ' >> project_name.log')
