# -*- coding: utf-8 -*-
'''
Created on 2020/03/20
Modified on 2020/03/23

@author: ZL Chen
@title: Parser Log
'''

import os
import datetime
import subprocess
from testcase_db import testcase_db


class parser_log(object):

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

	# Parser the DUT's file log by adb command
	def adbparser_outside_file_exist(self, testcase_list):
		try:
			self._delete_local_file('outside_file_exist.log')
			for testcase_n in range(len(testcase_list)):
				# print(testcase_list[testcase_n])
				self._adb_shell_cmd('ls /data/USC130-A8-Testtool | findstr ' +
									testcase_list[testcase_n] + '.log >> outside_file_exist.log')

			for download_file in testcase_list:
				os.system('adb pull /data/USC130-A8-Testtool/' +
						  download_file + '.log')
		except Exception as e:
			raise e

	# Make sure the parser log content
	def local_parser(self, testcase_list):
		try:
			file_log = open('outside_file_exist.log').read()
			for testcase_n in range(len(testcase_list)):
				file_log = open('outside_file_exist.log').read()
				file_log_split = file_log.split('\n')[testcase_n]
				# print(file_log_split)
				content_log = open(file_log_split).read()
				# Get the timer by datetime api
				timer = self.timer()
				report_log = open('report_' + timer + '.txt', 'a')
				report_log.write(
					'\n------------------------------------------' + \
					'\nTest Case: ' + testcase_list[testcase_n] + \
					'\n------------------------------------------' + '\n')
				if 'PASS' in content_log:
					report_log.write(content_log)
					report_log.write(
						'--------------------------------\n'
						'----The test case is PASSED.----\n' + \
						'--------------------------------\n')
				elif '(KB)' in content_log:
					report_log.write(content_log)
					report_log.write(
						'-------------------------------\n'
						'--The test case is COMPLETED.--\n' + \
						'-------------------------------\n')
				elif 'FAIL' in content_log:
					report_log.write(content_log)
					report_log.write(
						'--------------------------------\n'
						'----The test case is FAILED.----\n' + \
						'--------------------------------\n')
				else:
					report_log.write(content_log)
					report_log.write(
						'--------------------------------\n'
						'----The Shell Script is ERROR.----\n' + \
						'--------------------------------\n')
		except Exception as e:
			raise e

	def timer(self):
		now_time = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
		return now_time

	def _delete_local_file(self, filename):
		os.system('del /f q ' + filename)
		print('del /f /q ' + filename)


if __name__ == '__main__':
	try:
		os.system('del /f /q *.log')
		testcase_db = testcase_db()
		respone_testcase = testcase_db.db_parser('..\\db\\testcase.db')
		parser_log = parser_log()
		parser_log.adbparser_outside_file_exist(respone_testcase)
		parser_log.local_parser(respone_testcase)
	except Exception as e:
		raise e
