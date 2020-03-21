# -*- coding: utf-8 -*-
'''
Created on 2020/03/20

@author: ZL Chen
@title: Parser Log
'''

import os
import datetime
import subprocess


class parser_log(object):

	# Initial test case name
	global testcase_list, Backlight, rtc, storage_emmc, systeminformation, usbdisk_sdcard
	Backlight = 'USC130-A8_Backlight'
	rtc = 'USC130-A8_RTC'
	storage_emmc = 'USC130-A8_Storage_eMMC'
	systeminformation = 'USC130-A8_SystemInformation'
	usbdisk_sdcard = 'USC130-A8_UsbDisk_Sdcard'
	testcase_list = [Backlight, rtc, storage_emmc,
					 systeminformation, usbdisk_sdcard]

	def _adb_shell(self, shell_cmds):
		try:
			cmds = ['adb', 'shell', shell_cmds]
			# print(cmds)
			stdout = subprocess.Popen(
				cmds, stdout=subprocess.PIPE).communicate()[0].rstrip()
			lines = stdout.splitlines()
			# print('stdout......', stdout)
			# print('lines.......', lines)
			pass
		except:
			raise Exception('The adb shell is failed.')

	def _adb_shell_cmd(self, shell_cmds):
		try:
			os.system('adb shell ' + shell_cmds)
			pass
		except Exception as e:
			raise e

	def adbparser(self):
		self._outside_file_exist()

	# Parser the DUT's file log by adb command
	def _outside_file_exist(self):
		self._delete_local_file('outside_file_exist.log')
		for testcase_n in range(len(testcase_list)):
			print(testcase_list[testcase_n])
			self._adb_shell_cmd('ls /data/USC130-A8-Testtool | findstr ' +
								testcase_list[testcase_n] + '.log >> outside_file_exist.log')
		for download_file in testcase_list:
			os.system('adb pull /data/USC130-A8-Testtool/' +
					  download_file + '.log')

	# Make sure the parser log content
	def local_parser(self):
		file_log = open('outside_file_exist.log').read()
		for testcase_n in range(len(testcase_list)):
			file_log = open('outside_file_exist.log').read()
			file_log_split = file_log.split('\n')[testcase_n]
			content_log = open(file_log_split).read()
			# Get the timer by datetime api
			timer = self.timer()
			report_log = open('report_' + timer + '.log', 'a')
			if 'PASS' in content_log:
				report_log.write(content_log)
				report_log.write('The test case is passed.' + '\n\n')
			elif '(KB)' in content_log:
				report_log.write(content_log)
				report_log.write('The test case is completed.' + '\n\n')
			else:
				report_log.write(content_log)
				report_log.write('The test case is failed.' + '\n\n')

	def timer(self):
		now_time = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
		return now_time

	def _delete_local_file(self, filename):
		os.system('del /f q ' + filename)
		print('del /f /q ' + filename)


if __name__ == '__main__':
	os.system('del /f /q *txt *.log')
	parser_log = parser_log()
	parser_log.adbparser()
	parser_log.local_parser()
