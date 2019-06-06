# -*- coding: utf-8 -*-
'''
Created on 2019/05/21

@author: ZL Chen
@title: The Wireless LAN should be worked after the airplane mode is switch on/off.
'''

import os
import time
import subprocess
from subprocess import check_output
from uiautomator import device as d


class airplane_wlan(object):

	global sum_pass
	global sum_fail
	sum_pass = 0
	sum_fail = 0

	def kill_exe(self, filename_exe):
		os.system('taskkill /f /im ' + filename_exe + '.exe')

	def kill_extension_file(self, filename_extension):
		os.system('del /f /q *.' + filename_extension)

	# APP for back to the desktop -> click the Setting -> click the Wi-Fi button
	def app_launch(self):
		try:
			d.press.home()
			if d(description='Apps').exists:
				d(description='Apps').click()
			time.sleep(1)
			if d(description='Settings').exists:
				d(description='Settings').click()
			time.sleep(1)
			d(scrollable=True).scroll.to(text='Wi‑Fi')
			if d(text='Wi‑Fi').exists:
				d(text='Wi‑Fi').click()
		except:
			raise Exception('The \'' + 'Apps' + 'or' +
							'Wi‑Fi' + '\' doe NOT found')

	# screenshot the android
	def screenshot(self, screenshot):
		now = time.strftime('%Y%m%d_%H%M%S', time.localtime(time.time()))
		path = '.\\' + screenshot + '_' + now + '.jpg'
		d.screenshot(path)

	# ping the google servier by adb shell command
	def adb_command_set(self, value):
		self._adb_shell(value)

	# reponse messgae by adb shell command
	def adb_response_get(self, value):
		global sum_pass
		global sum_fail
		if '100% packet loss' in str(stdout):
			self._get_value(9)
			sum_fail += 1
			os.system('echo The connection is Failed.(FAIL) >> ping_server.txt')
			print('The connection is Failed.(FAIL)')
		elif value in str(stdout):
			self._get_value(16)
			sum_pass += 1
			os.system('echo The connection is Passed.(PASS) >> ping_server.txt')
			print('The connection is Passed.(PASS)')
		elif '25% packet loss' in str(stdout):
			self._get_value(14)
			sum_pass += 1
			os.system('echo The connection is Passed.(PASS) >> ping_server.txt')
			print('The connection is Passed.(PASS)')
		elif '50% packet loss' in str(stdout):
			self._get_value(12)
			sum_pass += 1
			os.system('echo The connection is Passed.(PASS) >> ping_server.txt')
			print('The connection is Passed.(PASS)')
		elif '75% packet loss' in str(stdout):
			self._get_value(10)
			sum_pass += 1
			os.system('echo The connection is Passed.(PASS) >> ping_server.txt')
			print('The connection is Passed.(PASS)')
		else:
			self._get_value(1)
			sum_fail += 1
			os.system('echo The connection is Failed.(FAIL) >> ping_server.txt')
			print('The connection is Failed.(FAIL)')

	def _get_value(self, round_times):
		try:
			for get in range(round_times):
				if get == 8 or get == 15:
					echo = str(lines[get]).split('b\'')[1]
					os.system('echo ' + echo + ' >> ping_server.txt')
				if get == 0 or get == 2 or get == 4 or get == 6 or get == 10 or get == 12 or get == 14:
					echo = str(lines[get]).split('b\'')[1]
					os.system('echo ' + echo + ' >> ping_server.txt')
				if get == 1 or get == 3 or get == 5 or get == 7 or get == 9 or get == 11 or get == 13:
					echo = str(lines[get]).split('b\'')[1]
					os.system('echo ' + echo + ' >> ping_server.txt')
		except:
			raise Exception('Cannot get the response message.')

	def _adb_shell(self, shell_cmds):
		global stdout
		global lines
		try:
			shell_cmds = shell_cmds + '; echo $?'
			cmds = ['adb', 'shell', shell_cmds]
			stdout = subprocess.Popen(
				cmds, stdout=subprocess.PIPE).communicate()[0].rstrip()
			lines = stdout.splitlines()
			# print(stdout)
			# os.system('echo stdout: ' + str(stdout) + ' >> ping_server.txt')
			# print(lines)
			# os.system('echo lines: ' + str(lines) + ' >> ping_server.txt')
		except:
			raise Exception('The adb shell is failed.')

	# launch the airplane mode
	def start_airplane(self):
		try:
			self._adb_shell('settings put global airplane_mode_on 1')
			self._adb_shell(
				'am broadcast -a android.intent.action.AIRPLANE_MODE --ez state true')
			time.sleep(6)
			print('The Start airplane is finished.')
		except:
			raise Exception('The start airplane is not finished.')

	# shutdown the airplane mode
	def stop_airplane(self):
		try:
			self._adb_shell('settings put global airplane_mode_on 0')
			self._adb_shell(
				'am broadcast -a android.intent.action.AIRPLANE_MODE --ez state false')
			time.sleep(15)
			print('The Stop airplane is finished.')
		except:
			raise Exception('The stop airplane is not finished.')


if __name__ == '__main__':
	print('------------------------------------------------------------------------------')
	print('Created on 2019/05/23')
	print('Author: ZL Chen')
	print('Title: The Wi-Fi should be worked after the airplane mode is switch on/off.')
	print('------------------------------------------------------------------------------')
	airplane = airplane_wlan()
	airplane.kill_extension_file('txt')
	airplane.kill_extension_file('jpg')
	cycle_time = int(input('Please input the \'Cycle Times\' you want : '))
	for cycle in range(cycle_time):
		airplane.app_launch()
		os.system(
			'echo ------------------------------------------------------------------------------ >> ping_server.txt')
		print(
			'------------------------------------------------------------------------------')
		os.system('echo ' + 'Cycle Times: ' +
				  str(cycle + 1) + ' >> ping_server.txt')
		print('Cycle Times: ' + str(cycle + 1))
		airplane.start_airplane()
		airplane.screenshot('airplane_on_' + str(cycle + 1))
		airplane.stop_airplane()
		airplane.screenshot('airplane_off_' + str(cycle + 1))
		airplane.adb_command_set('ping -w 4 8.8.8.8')
		airplane.adb_response_get('0% packet loss')
		os.system('echo ' + 'Cycle Times: ' + str(cycle + 1) + ', Passed: ' +
				  str(sum_pass) + ', Failed: ' + str(sum_fail) + ' >> ping_server.txt')
		print('Cycle Times: ' + str(cycle + 1) + ', Passed: ' +
			  str(sum_pass) + ', Failed: ' + str(sum_fail))
	os.system('echo ' + 'Total Cycle Times: ' + str(cycle_time) + ', Passed: ' +
			  str(sum_pass) + ', Failed: ' + str(sum_fail) + ' >> ping_server.txt')
	print('Total Cycle Times: ' + str(cycle_time) + ', Passed: ' +
		  str(sum_pass) + ', Failed: ' + str(sum_fail))
	os.system('.\\backup_log.bat')
	airplane.kill_exe('adb')
