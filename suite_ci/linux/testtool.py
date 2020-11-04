# -*- coding: utf-8 -*-
'''
Created on 2020/10/26

@author: ZL Chen
@title: testtool ssh and scp command merge
'''

import os
import sys
import configparser
from time import sleep
from device_check import Device_check
from subprocess import check_output

# parameter_setting.ini
parameter_value = {}
parameter_setting = configparser.ConfigParser()
parameter_setting.read('.\\ini\\parameter_setting.ini', encoding='utf-8')


class testtool(object):

	def adb_shell_split(self, j):
		# 如果 adb shell 做字串處理
		if j is not False:
			read_list_content = list()
			with open('project_name.log', 'r', encoding='utf-8') as project_name:
				read = project_name.read()
				read_list = read.split('\n')
				# print(read_list)
				for space in range(len(read_list)):
					if read_list[space] == '':
						pass
					else:
						read_list_content.append(read_list[space])
			# print(read_list_content)
			with open('project_name.log', 'w', encoding='utf-8') as project_name:
				for times in range(len(read_list_content)):
					project_name.write(read_list_content[times] + '\n')

	def log_export(self, device_check_value, j):
		try:
			# 把 Enable 的 .sh 存入 project_name.log
			for sh in range(len(device_check_value)):
				os.system(self._ssh() + 'root@' +
						  sys.argv[1] + ' \"cd /data/testtool; ls ' + device_check_value[sh] + '.sh\"' + ' >> project_name.log')
				print(self._ssh() + 'root@' +
					  sys.argv[1] + ' \"cd /data/testtool; ls ' + device_check_value[sh] + '.sh\"' + ' >> project_name.log')

			self.adb_shell_split(j)

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
					value = parameter_setting.get(device_check_value_sh, parameter_setting.options(device_check_value_sh)[p])  # 取出指定的 key value
					alist.append(value)  # key value 寫入 alist

				if alist == []:  # 如果 key is none
					alist.append('none')

				# 取出字串內容寫入 temp.log
				for print_alist in range(len(alist)):
					os.system('echo ' + alist[print_alist] + ' >> temp.log')

				temp_open = open('temp.log', 'r', encoding='utf-8')
				temp = temp_open.read().split('\n')

				value_parameter = ''  # 宣告空字串
				for n in range(len(temp)):  # 判斷幾個值
					if temp[n] == 'none ':  # 如果 temp[0] 為 none 回傳 ''
						value_parameter = ''
						break
					value_parameter = value_parameter + temp[n]  # Value 字串合併
				temp_open.close()

				if project_name[loop] == '':
					raise ValueError('The system is raised.')

				# 執行字串斷行
				cr_delete = 'sed -i \'s/\\r$//g\''
				os.system(self._ssh() + 'root@' + sys.argv[1] + ' \"' + cr_delete + ' /data/testtool/' + project_name[loop] + '\"')
				print(self._ssh() + 'root@' + sys.argv[1] + ' \"' + cr_delete + ' /data/testtool/' + project_name[loop] + '\"')

				# 執行腳本 (帶入 config 指定 value)
				os.system(self._ssh() + 'root@' + sys.argv[1] + ' \"/data/testtool/' + project_name[loop] + '\"' + ' ' + value_parameter)
				print(self._ssh() + 'root@' + sys.argv[1] + ' \"/data/testtool/' + project_name[loop] + '\"' + ' ' + value_parameter)

				os.system('del /f /q temp.log')
				alist.clear()

			os.system(self._ssh() + 'root@' + sys.argv[1] + ' \"cd /data/testtool; ls *.log\" > project_name.log')
			print(self._ssh() + 'root@' + sys.argv[1] + ' \"cd /data/testtool; ls *.log\" > project_name.log')

			self.adb_shell_split(j)

			project_name = (open('project_name.log', 'r', encoding='utf-8').read()).split('\n')
			for loop in range(len(project_name)):
				# print(len(project_name))
				# print(project_name[loop])
				if project_name[loop] == '':
					break
				os.system(self._scp() + 'root@' + sys.argv[1] + ':/data/testtool/' + project_name[loop] + ' .\\testtool\\')
				print(self._scp() + 'root@' + sys.argv[1] + ':/data/testtool/' + project_name[loop] + ' .\\testtool\\')
		except Exception as e:
			raise e

	def log_export_py(self, device_check_py_value):
		os.system('del /f /q testtool\\*.bat')
		if device_check_py_value != []:
			for py in range(len(device_check_py_value)):
				# 判斷有幾個 key 並且透過 config.get 出 value
				total_value = ''
				# 判斷有幾個 key
				for p in range(len(parameter_setting.options(device_check_py_value[py]))):
					value = parameter_setting.get(device_check_py_value[py], parameter_setting.options(
						device_check_py_value[py])[p])  # 取出指定的 key value
					total_value += ' ' + value
				# print(total_value)
				os.system('echo testtool\\' + device_check_py_value[py] + '.pyc' + total_value + ' >> testtool\\py.bat')
		else:
			pass
		os.system('testtool\\py.bat')

	def taskkill(self, name):
		os.system('taskkill /f /im ' + name)

	def _ssh(self):
		return '.\\app\\ssh.exe -o StrictHostKeyChecking=no '

	def _scp(self):
		return '.\\app\\scp.exe -o StrictHostKeyChecking=no '

	def ssh_root(self, ssh_cmd):
		os.system('.\\app\\ssh.exe -o StrictHostKeyChecking=no ' + ssh_cmd)

	def scp_root(self, scp_cmd):
		os.system('.\\app\\scp.exe -o StrictHostKeyChecking=no ' + scp_cmd)


if __name__ == '__main__':
	try:
		os.system('del /f /q testtool\\*.log')
		os.system('del /f /q *.log')
		testtool = testtool()
		testtool.taskkill('ssh.exe')
		testtool.taskkill('scp.exe')
		testtool.ssh_root('root@' + sys.argv[1] + ' \"rm -rf /data\"')
		testtool.ssh_root('root@' + sys.argv[1] + ' \"mkdir /data"')
		testtool.scp_root('-r testtool root@' + sys.argv[1] + ':/data')
		testtool.ssh_root('root@' + sys.argv[1] + ' \"chmod a+x /data/testtool/*\"')
		device_check = Device_check()
		device_check_value = device_check.verify()
		testtool.log_export(device_check_value, False)
		device_check_py_value = device_check.verify_py()
		testtool.log_export_py(device_check_py_value)
	except Exception as e:
		raise e
