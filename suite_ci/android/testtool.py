# -*- coding: utf-8 -*-
'''
Created on 2020/03/21
Modified on 2020/03/26
Add the class on 2020/04/09
Modified the log_export method on 2020/04/10

@author: ZL Chen
@title: testtool adb command merge
'''

import os
import sys
import configparser
from device_check import Device_check
from time import sleep

# parameter_setting.ini
parameter_value = {}
parameter_setting = configparser.ConfigParser()
parameter_setting.read('.\ini\\parameter_setting.ini', encoding='utf-8')


class testtool(object):

	def adb_shell_cmd(self, shell_cmds):
		try:
			os.system('adb shell ' + shell_cmds)
			pass
		except Exception as e:
			raise e

	def adb_push_cmd(self, shell_cmds):
		try:
			os.system('adb push ' + shell_cmds)
			pass
		except Exception as e:
			raise e

	def adb_pull_cmd(self, shell_cmds):
		try:
			os.system('adb pull ' + shell_cmds)
			pass
		except Exception as e:
			raise e

	def adb_cmd(self, cmds):
		try:
			os.system('adb ' + cmds)
			pass
		except Exception as e:
			raise e

	def log_export(self, device_check_value):
		try:
			# 把 Disable 的 .sh 存入 project_name.log
			for sh in range(len(device_check_value)):
				self.adb_shell_cmd('\"cd /data/testtool; ls ' + device_check_value[sh] + '.sh\"' + ' >> project_name.log')

			project_name_open = open('project_name.log', 'r', encoding='utf-8')
			project_name = project_name_open.read().split('\n')  # 讀出 project_name.log 的名稱 (xxx.sh)

			for loop in range(len(project_name)):
				# print(len(project_name))
				# print(project_name[loop])
				device_check_value_sh = project_name[loop].split('.sh')[0]  # 去除 split('.sh')

				if device_check_value_sh == '':  # 發現空字串直接跳出
					break

				alist = []  # 宣告空 list
				# 判斷有幾個 key 並且透過 config.get 出 value
				for p in range(len(parameter_setting.options(device_check_value_sh))):  # 判斷有幾個 key
					value = parameter_setting.get(device_check_value_sh, parameter_setting.options(
								device_check_value_sh)[p])  # 取出指定的 key value
					alist.append(value)  # key value 寫入 alist

				# 取出字串內容寫入 temp.log
				for print_alist in range(len(alist)):
					os.system('echo ' + alist[print_alist] + ' >> temp.log')

				temp_open = open('temp.log', 'r', encoding='utf-8')
				temp = temp_open.read().split('\n')

				value_parameter = ''  # 宣告空字串
				for n in range(len(temp)):  # 判斷幾個值
					if temp[n] == '':
						break
					value_parameter = value_parameter + temp[n]  # Value 字串合併
				temp_open.close()

				if project_name[loop] == '':
					break

				# 執行字串斷行
				cr_delete = 'sed -i \'s/\\r$//g\''
				self.adb_shell_cmd(cr_delete + ' ' + '/data/testtool/' + project_name[loop])
				print(cr_delete + ' ' + '/data/testtool/' + project_name[loop])

				# 執行腳本 (帶入 config 指定 value)
				self.adb_shell_cmd('/data/testtool/' + project_name[loop] + ' ' + value_parameter)
				print('/data/testtool/' + project_name[loop] + ' ' + value_parameter)

				os.system('del /f /q temp.log')
				alist.clear()

			self.adb_shell_cmd(
				'\"cd /data/testtool; ls *.log\"' + ' > project_name.log')

			project_name = (open('project_name.log', 'r', encoding='utf-8').read()).split('\n')
			for loop in range(len(project_name)):
				# print(len(project_name))
				# print(project_name[loop])
				if project_name[loop] == '':
					break
				self.adb_pull_cmd('/data/testtool/' + project_name[loop] + ' testtool/')
				print('/data/testtool/' + project_name[loop] + ' testtool/')
		except Exception as e:
			raise e


if __name__ == '__main__':
	try:
		os.system('del /f /q testtool\\*.log')
		os.system('del /f /q *.log')
		os.system('del /f /q adb.exe')
		testtool = testtool()
		testtool.adb_cmd('kill-server')
		testtool.adb_cmd('start-server')
		testtool.adb_cmd('adb devices')
		testtool.adb_cmd('connect ' + sys.argv[1])
		testtool.adb_cmd('root')
		testtool.adb_shell_cmd('rm -rf /data/testtool')
		testtool.adb_shell_cmd('mkdir /data/testtool')
		os.system('adb push testtool /data/')
		testtool.adb_shell_cmd('chmod 777 /data/testtool/*')
		device_check = Device_check()
		device_check_value = device_check.verify()
		testtool.log_export(device_check_value)
	except Exception as e:
		raise e
