# -*- coding: utf-8 -*-
'''
Created on 2020/03/20
Modified on 2020/03/23

@author: ZL Chen
@title: Parser Log
'''

import os
import sys
import time
import datetime
import subprocess

class parser_log(object):

	def _adb_shell(self, shell_cmds):
		try:
			cmds = ['adb', 'shell', shell_cmds]
			# print(cmds)
			stdout = subprocess.Popen(cmds, stdout=subprocess.PIPE).communicate()[0].rstrip()
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
			project_name_open = open('..\\android\\project_name.log', 'r', encoding='utf-8')
			project_name = project_name_open.read().split('\n')
			for loop in range(len(project_name)):
				# print(len(project_name))
				# print(project_name[loop])
				if project_name[loop] == '':
					break
			project_name_open.close()
		except Exception as e:
			raise e

	def copy_log_file(self, source_path, distination_path):
		os.system('copy /y ' + source_path + ' ' + distination_path)

	def log_parser(self):
		try:
			file_log_open = open('project_name.log', 'r', encoding='utf-8')
			file_log = file_log_open.read().split('\n')
			# Get the timer by datetime api
			timer = self.timer()
			for loop in range(len(file_log)):
				# print(len(file_log))
				# print(file_log[loop])
				if file_log[loop] == '':
					break
				content_log_open = open(file_log[loop], 'r', encoding='utf-8')
				content_log = content_log_open.read()
				current_time = 'report_' + timer + '.txt'
				report_log = open(current_time, 'a', encoding='utf-8')
				report_log.write(
					'\n*********************************************************' + \
					'\nTest Case: ' + file_log[loop] + \
					'\n*********************************************************' + '\n')
				if 'PASS' in content_log:
					report_log.write(content_log)
					print(content_log)
					report_log.write(
						'********************************\n' + \
						'----The test case is PASSED.----\n' + \
						'********************************\n')
					print(
						'********************************\n' + \
						'----The test case is PASSED.----\n' + \
						'********************************\n')
				elif 'FAIL' in content_log:
					report_log.write(content_log)
					print(content_log)
					report_log.write(
						'********************************\n' + \
						'----The test case is FAILED.----\n' + \
						'********************************\n')
					print(
						'********************************\n' + \
						'----The test case is FAILED.----\n' + \
						'********************************\n')

				else:
					report_log.write(content_log)
					print(content_log)
					report_log.write(
						'********************************\n' + \
						'---The Shell Script is ERRORED.---\n' + \
						'********************************\n')
					print(
						'********************************\n' + \
						'---The Shell Script is ERRORED.---\n' + \
						'********************************\n')
				time.sleep(2)
				content_log_open.close()
				report_log.close()
			# ADB push the file to devices		
			os.system('adb push ' + 'report_' + timer + '.txt' + \
						' /data/testtool/')
			file_log_open.close()			
			return timer
		except Exception as e:
			raise e

	def timer(self):
		now_time = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
		return now_time

	def delete_local_file(self, filename):
		os.system('del /f /q ' + filename)
		print('del /f /q ' + filename)


if __name__ == '__main__':
	try:
		os.system('del /f /q *.log')
		os.system('del /f /q *.txt')
		os.system('adb devices')
		os.system('adb disconnect')
		os.system('adb connect ' + sys.argv[1])
		os.system('adb root')
		parser_log = parser_log()
		parser_log.copy_log_file('..\\android\\testtool\\*.log', '.')
		parser_log.copy_log_file('..\\android\\*.log', '.')
		current_time = parser_log.log_parser()
		os.system('mkdir backup\\' + current_time)
		parser_log.copy_log_file('*.log', 'backup\\' + current_time)
		parser_log.copy_log_file('*.txt', 'backup\\' + current_time)
		parser_log.delete_local_file('*.log')
		parser_log.delete_local_file('*.txt')
	except Exception as e:
		raise e