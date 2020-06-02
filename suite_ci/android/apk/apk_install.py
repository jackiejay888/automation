# -*- coding: utf-8 -*-
'''
Created on 2020/06/01

@author: ZL Chen
@title: APK installation
'''

import os
import sys
from time import sleep
from subprocess import check_output


class apk_install(object):

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

	def adb_cmd(self, cmds):
		try:
			print('adb ' + cmds)
			os.system('adb ' + cmds)
		except Exception as e:
			raise e

	def read_title_str(self):
		f = open('apk_install.config', mode='w')
		for root, dirs, files in os.walk('..\\apk'):
			for i in range(len(files)):
				if '.apk' in files[i]:
					f.write(files[i].split('.apk')[0] + '\n')
		f.close()

	def install(self):
		f = open('apk_install.config', mode='r').read()
		f = f.split('\n')
		for i in range(len(f)):
			if f[i] == '':
				break
			self.adb_cmd('shell pm uninstall -k \"' + f[i] + '\"')
			self.adb_cmd('install \"' + f[i] + '.apk\"')


if __name__ == '__main__':
	try:
		os.system('del /f /q adb.exe')
		apk_install = apk_install()
		apk_install.adb_cmd('kill-server')
		apk_install.adb_cmd('start-server')
		apk_install.adb_cmd('devices')
		j = apk_install.finddevices_set()
		if j is False:
			apk_install.adb_cmd('connect ' + sys.argv[1])
		apk_install.adb_cmd('root')
		apk_install.read_title_str()
		apk_install.install()
	except Exception as e:
		raise e
