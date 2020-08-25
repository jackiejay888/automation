# -*- coding: utf-8 -*-
'''
Created on 2020/03/20
Modified on 2020/03/23

@author: ZL Chen
@title: Parser Log
'''

import os
import sys
import csv
import time
import datetime
import subprocess
import configparser
import pandas as pd
from subprocess import check_output

parameter_setting = configparser.ConfigParser()
parameter_setting.read('..\\android\\ini\\parameter_setting.ini', encoding='utf-8')

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
			# 新增簡易總表 #
			summary_time = 'summary_' + timer + '.csv'
			report_summary = open(summary_time, 'a', newline='')
			writer = csv.writer(report_summary, delimiter=',')
			writer.writerow(['Test case', 'Status'])
			passed = 0
			failed = 0
			exceptioned = 0
			#-------------#
			current_time = 'report_' + timer + '.txt'
			report_log = open(current_time, 'a', encoding='utf-8')
			for loop in range(len(file_log)):
				# print(len(file_log))
				# print(file_log[loop])
				# 新增簡易總表 #
				if file_log[loop] == '':
					writer.writerow([' ', ' '])
					writer.writerow(['Total', passed + failed + exceptioned])
					writer.writerow(['Pass', passed])
					writer.writerow(['Fail', failed])
					writer.writerow(['Exception', exceptioned])
					print('Total: ' + str(passed + failed + exceptioned) + '\n' + \
							'Pass: ' + str(passed) + ', Fail: ' + str(failed) + \
							', Exception: ' + str(exceptioned) + '\n-------------------------------------------------\n')
					break
				#-------------#
				content_log_open = open(file_log[loop], 'r', encoding='utf-8')
				content_log = content_log_open.read()
				report_log.write(
					'*********************************************************\n' +
					'Test Case: ' + file_log[loop] + '\n'
					'*********************************************************\n')
				if 'PASS' in content_log:
					report_log.write(content_log)
					print(content_log)
					report_log.write(
						'********************************\n' +
						'----The test case is PASS.----\n' +
						'********************************\n')
					print(
						'********************************\n' +
						'----The test case is PASS.----\n' +
						'********************************\n')
					# 新增簡易總表 PASS #
					writer.writerow([file_log[loop].split('.log')[0], 'Pass'])
					print('' + file_log[loop].split('.log')[0] + '\t(Pass)\n'+ \
						'-------------------------------------------------\n')
					passed += 1
					#-------------#
				elif 'FAIL' in content_log:
					report_log.write(content_log)
					print(content_log)
					report_log.write(
						'********************************\n' +
						'----The test case is FAIL.----\n' +
						'********************************\n')
					print(
						'********************************\n' +
						'----The test case is FAIL.----\n' +
						'********************************\n')
					# 新增簡易總表 FAIL #
					writer.writerow([file_log[loop].split('.log')[0], 'Fail'])
					print('' + file_log[loop].split('.log')[0] + '\t(Fail)\n'+ \
						'-------------------------------------------------\n')
					failed += 1
					#-------------#
				else:
					report_log.write(content_log)
					print(content_log)
					report_log.write(
						'********************************\n' +
						'---The Shell Script is EXCEPTION.---\n' +
						'********************************\n')
					print(
						'********************************\n' +
						'---The Shell Script is EXCEPTION.---\n' +
						'********************************\n')
					# 新增簡易總表 EXCEPTION #
					writer.writerow([file_log[loop].split('.log')[0], 'Exception'])
					print(
						'' + file_log[loop].split('.log')[0] + '\t(Exception)\n'+ \
						'-------------------------------------------------\n')
					exception += 1
					#-------------#
				time.sleep(0.2)
				content_log_open.close()
			report_log.close()
			# 新增簡易總表 close() #
			report_summary.close()
			#-------------#
			# 新增簡易總表 close() #
			pd.set_option('display.width', 1000)
			pd.set_option('colheader_justify', 'left')
			df = pd.read_csv('summary_' + timer + '.csv')
			df.to_html('summary_' + timer + '.html', index = False)
			#-------------#
			# ADB push the file to devices
			os.system('adb push ' + 'report_' + timer + '.txt' +
									' /data/testtool/')
			os.system('adb push ' + 'summary_' + timer + '.csv' +
									' /data/testtool/')
			os.system('adb push ' + 'summary_' + timer + '.html' +
									' /data/testtool/')
			file_log_open.close()
			return timer
		except Exception as e:
			raise e

	def timer(self):
		now_time = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
		return now_time

	def folder_name(self):
		project_name = parameter_setting.get('project_name', 'name')
		return project_name + '_' + self.timer()

	def delete_local_file(self, filename):
		os.system('del /f /q ' + filename)
		print('del /f /q ' + filename)	

	def finddevices_set(self):
		try:
			adb_ouput = check_output(["adb", "devices"])
			devices_id = str(adb_ouput.split()[-2])
			if devices_id == 'b\'devices\'':
				print('Not Find a new device.')
				return False
			else:
				print('Find a new device.')
				return True
		except Exception as e:
			raise e

if __name__ == '__main__':
	try:
		os.system('del /f /q *.log')
		os.system('del /f /q *.txt')
		os.system('del /f /q *.csv')
		os.system('del /f /q *.html')
		os.system('del /f /q *.ini')
		os.system('del /f /q *.png')
		os.system('adb devices')
		os.system('adb disconnect')
		parser_log = parser_log()
		j = parser_log.finddevices_set()
		if j is False:
			print('False')
			os.system('adb connect ' + sys.argv[1])
		os.system('adb root')
		parser_log.copy_log_file('..\\android\\testtool\\*.log', '.')
		parser_log.copy_log_file('..\\android\\*.log', '.')
		parser_log.copy_log_file('..\\android\\ini\\*.ini', '.')
		parser_log.copy_log_file('..\\android\\testtool\\*.png', '.')
		current_time = parser_log.log_parser()
		folder_name = parser_log.folder_name()
		os.system('mkdir backup\\' + folder_name)
		parser_log.copy_log_file('*.log', 'backup\\' + folder_name)
		parser_log.copy_log_file('*.txt', 'backup\\' + folder_name)
		parser_log.copy_log_file('*.csv', 'backup\\' + folder_name)
		parser_log.copy_log_file('*.html', 'backup\\' + folder_name)
		parser_log.copy_log_file('*.ini', 'backup\\' + folder_name)
		parser_log.copy_log_file('*.png', 'backup\\' + folder_name)
		parser_log.delete_local_file('*.log')
		parser_log.delete_local_file('*.txt')
		parser_log.delete_local_file('*.csv')
		parser_log.delete_local_file('*.html')
		parser_log.delete_local_file('*.ini')
		parser_log.delete_local_file('*.png')
	except Exception as e:
		raise e
