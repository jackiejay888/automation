# -*- coding: utf-8 -*-
'''
Created on 2019/05/21

@author: ZL Chen
@title: The Wireless should be worked after the airplane mode is switch on/off.
'''

import os
import time
import subprocess
from subprocess import check_output
from uiautomator import device as d


class airplane(object):

	global sum_pass
	global sum_fail
	sum_pass = 0
	sum_fail = 0

	def _adb_shell(self, shell_cmds):
		global stdout
		global lines
		try:
			shell_cmds = shell_cmds + '; echo $?'
			cmds = ['adb', 'shell', shell_cmds]
			stdout = subprocess.Popen(cmds, stdout=subprocess.PIPE).communicate()[0].rstrip()
			lines = stdout.splitlines()
			print(stdout)
			print(lines)
		except:
			raise Exception('The adb shell was not finished - FAIL')

	# ping the google servier by adb shell command
	def adb_command_set(self, value, cycle):
		os.system('echo ' + 'Cycle Times: ' + cycle + ' >> ping_server.txt')
		self._adb_shell(value)

	def adb_response_get(self, value):
		global sum_pass
		global sum_fail
		if value in str(stdout):
			self._get_value(16)
			sum_pass += 1
			os.system('echo The connection is Failed.(PASS) >> ping_server.txt')
			print('The connection is Failed.(PASS)')
		elif '25% packet loss' in str(stdout):
			self._get_value(16)
			sum_fail += 1
			os.system('echo The connection is Failed.(FAIL) >> ping_server.txt')
			print('The connection is Failed.(FAIL)')
		elif '75% packet loss' in str(stdout):
			self._get_value(16)
			sum_fail += 1
			os.system('echo The connection is Failed.(FAIL) >> ping_server.txt')
			print('The connection is Failed.(FAIL)')
		elif '100% packet loss' in str(stdout):
			self._get_value(13)
			sum_fail += 1
			os.system('echo The connection is Failed.(FAIL) >> ping_server.txt')
			print('The connection is Failed.(FAIL)')
		else:
			echo = str(lines[0]).split('b\'')[1]
			# print(echo)
			os.system('echo ' + echo + ' >> ping_server.txt')
			sum_fail += 1
			os.system('echo The connection is Failed.(FAIL) >> ping_server.txt')
			print('The connection is Failed.(FAIL)')

	def _get_value(self, round_times):
		for get in range(round_times):
			if get == 8 or get == 15:
				echo = str(lines[get]).split('b\'')[1]
				# print(echo)
				os.system('echo ' + echo + ' >> ping_server.txt')
			if get == 0 or get == 2 or get == 4 or get == 6 or get == 10 or get == 12 or get == 14:
				echo = str(lines[get]).split('b\'')[1]
				# print(echo)
				os.system('echo ' + echo + ' >> ping_server.txt')
			else:
				pass

	def kill_extension_file(self, filename_extension):
		os.system('del /f /q *.' + filename_extension)
		print('The .' + filename_extension + ' is deleted.')


if __name__ == '__main__':
	airplane = airplane()
	airplane.kill_extension_file('txt')
	airplane.kill_extension_file('jpg')
	cycle_time = 1
	for cycle in range(cycle_time):
		print('Cycle Times: ' + str(cycle + 1))
		airplane.adb_command_set('ping -w 4 8.8.8.8', str(cycle + 1))
		airplane.adb_response_get('0% packet loss')
	os.system('echo ' + 'Cycle Times: ' + str(cycle_time) + ', Passed: ' + str(sum_pass) + ', Failed: ' + str(sum_fail) + ' >> ping_server.txt')
	print('Cycle Times: ' + str(cycle_time) + ', Passed: ' + str(sum_pass) + ', Failed: ' + str(sum_fail))
