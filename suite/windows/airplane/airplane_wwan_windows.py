# -*- coding: utf-8 -*-
'''
Created on 2019/11/05

@Author: ZL Chen
@Title: Airplane mode on/off base on windows environment.
'''

import os
import time
import subprocess
import pyscreenshot as ImageGrab


class airplane_wwan_windows(object):

	global sum_pass
	global sum_fail
	sum_pass = 0
	sum_fail = 0

	def run(self, cycle):
		on = self.arp_airplane_on()
		screenshot = on + '_' + cycle
		self.screenshot(screenshot)
		off = self.arp_airplane_off()
		screenshot = off + '_' + cycle
		self.screenshot(screenshot)

	# ping the google server by windows command
	def windows_command_set(self, windows_cmds):
		global stdout
		global lines
		try:
			cmds = windows_cmds
			stdout = subprocess.Popen(
				cmds, stdout=subprocess.PIPE).communicate()[0].rstrip()
			lines = stdout.splitlines()
			# print(stdout)
			# os.system('echo stdout: ' + str(stdout) + ' >> ping_server.txt')
			# print(lines)
			# os.system('echo lines: ' + str(lines) + ' >> ping_server.txt')
			# print('length is', len(lines))
		except:
			raise Exception('The windows command is failed.')

	# reponse messgae by windows command
	def windows_response_get(self, value):
		global sum_pass
		global sum_fail
		if '100% loss' in str(stdout):
			self._get_value(len(lines))
			sum_fail += 1
			os.system('echo The connection is Failed.(FAIL) >> ping_server.txt')
			print('The connection is Failed.(FAIL)')
		elif value in str(stdout):
			self._get_value(len(lines))
			sum_pass += 1
			os.system('echo The connection is Passed.(PASS) >> ping_server.txt')
			print('The connection is Passed.(PASS)')
		elif '25% loss' in str(stdout):
			self._get_value(len(lines))
			sum_pass += 1
			os.system('echo The connection is Passed.(PASS) >> ping_server.txt')
			print('The connection is Passed.(PASS)')
		elif '50% loss' in str(stdout):
			self._get_value(len(lines))
			sum_pass += 1
			os.system('echo The connection is Passed.(PASS) >> ping_server.txt')
			print('The connection is Passed.(PASS)')
		elif '75% loss' in str(stdout):
			self._get_value(len(lines))
			sum_pass += 1
			os.system('echo The connection is Passed.(PASS) >> ping_server.txt')
			print('The connection is Passed.(PASS)')
		else:
			self._get_value(len(lines))
			sum_fail += 1
			os.system('echo The connection is Failed.(FAIL) >> ping_server.txt')
			print('The connection is Failed.(FAIL)')

	def _get_value(self, round_times):
		try:
			for get in range(round_times):
				if get:
					echo = str(lines[get]).split('b\'')[1]
					os.system('echo ' + echo + ' >> ping_server.txt')
		except:
			raise Exception('Cannot get the response message.')

	def arp_airplane_on(self):
		os.system('arp_airplane_on.bat')
		time.sleep(13)
		return 'airplane_on'

	def arp_airplane_off(self):
		os.system('arp_airplane_off.bat')
		time.sleep(21)
		return 'airplane_off'

	def screenshot(self, times):
		now = time.strftime('%Y%m%d_%H%M%S', time.localtime(time.time()))
		path = times + '_' + now + '.jpg'
		ImageGrab.grab().save(path)


if __name__ == '__main__':
	os.system('del /f /q *.jpg')
	os.system('del /f /q *.txt')
	times = int(input('Cycle times: '))
	gateway = input('Please input the gateway : ')
	for cycle in range(int(times)):
		windows = airplane_wwan_windows()
		windows.run(str(cycle+1))
		windows.windows_command_set('ping -w 4 ' + gateway)
		windows.windows_response_get('0% loss')
		os.system('echo ' + 'Cycle Times: ' + str(cycle + 1) + ', Passed: ' +
				  str(sum_pass) + ', Failed: ' + str(sum_fail) + ' >> ping_server.txt')
		print('Cycle Times: ' + str(cycle + 1) + ', Passed: ' +
			  str(sum_pass) + ', Failed: ' + str(sum_fail))
	os.system('echo ' + 'Total Cycle Times: ' + str(times) + ', Passed: ' +
			  str(sum_pass) + ', Failed: ' + str(sum_fail) + ' >> ping_server.txt')
	print('Total Cycle Times: ' + str(times) + ', Passed: ' +
		  str(sum_pass) + ', Failed: ' + str(sum_fail))
	os.system('.\\backup_log.bat')
