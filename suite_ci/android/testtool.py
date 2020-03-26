# -*- coding: utf-8 -*-
'''
Created on 2020/03/21
Modified on 2020/03/26

@author: ZL Chen
@title: testtool adb command merge
'''

import os
import sys

def adb_shell_cmd(shell_cmds):
	try:
		os.system('adb shell ' + shell_cmds)
		pass
	except Exception as e:
		raise e

def adb_push_cmd(shell_cmds):
	try:
		os.system('adb push ' + shell_cmds)
		pass
	except Exception as e:
		raise e	

def adb_pull_cmd(shell_cmds):
	try:
		os.system('adb pull ' + shell_cmds)
		pass
	except Exception as e:
		raise e	

def adb_cmd(cmds):
	try:
		os.system('adb ' + cmds)
		pass
	except Exception as e:
		raise e

def log_export():

	adb_shell_cmd('\"cd /data/testtool; ls *.sh\"' + ' > project_name.log')

	project_name = (open('project_name.log', 'r').read()).split('\n')
	for loop in range(len(project_name)):
		# print(len(project_name))
		# print(project_name[loop])
		if project_name[loop] == '':
			break
		adb_shell_cmd('/data/testtool/' + project_name[loop])
		print('/data/testtool/' + project_name[loop])

	adb_shell_cmd('\"cd /data/testtool; ls *.log\"' + ' > project_name.log')

	project_name = (open('project_name.log', 'r').read()).split('\n')
	for loop in range(len(project_name)):
		# print(len(project_name))
		# print(project_name[loop])
		if project_name[loop] == '':
			break
		adb_pull_cmd('/data/testtool/' + project_name[loop] + ' testtool/')
		print('/data/testtool/' + project_name[loop] + ' testtool/')

os.system('del /f /q testtool\\*.log')
os.system('del /f /q *.log')
os.system('del /f /q adb.exe')
adb_cmd('kill-server')
adb_cmd('start-server')
adb_cmd('adb devices')
adb_cmd('connect ' + sys.argv[1])
adb_cmd('root')
adb_shell_cmd('rm -rf /data/testtool')
adb_shell_cmd('mkdir /data/testtool')
os.system('adb push testtool /data/')
adb_shell_cmd('chmod 777 /data/testtool/*')
log_export()