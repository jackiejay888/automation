# -*- coding: utf-8 -*-
'''
Created on 2020/06/01

@author: ZL Chen
@title: iperf test item
'''

import os
import sys
import time
import threading
import configparser
from subprocess import check_output

# parameter_setting.ini
parameter_value = {}
parameter_setting = configparser.ConfigParser()
parameter_setting.read('.\ini\\parameter_setting.ini', encoding='utf-8')
datetime = time.strftime("%Y%m%d_%H%M%S", time.localtime())

class eth_iperf_py(object):

	def iperf_server(self):
		print('iperf server is starting.')
		os.system('adb shell /data/testtool/iperf -s -i 5')
		pass

	def iperf_client(self):
		print('iperf client is starting.\nPlease waiting ' +
			  sys.argv[3] + ' secs.')
		os.system('app\\iperf -c ' + sys.argv[1] + ' -w ' + sys.argv[2] + ' -t ' +
				  sys.argv[3] + ' -i ' + sys.argv[4] + ' -d > ' + 'testtool\\' + self.strftime())
		pass

	def iperf_thread(self):
		self.iperf_kill_server()
		self.iperf_kill_client('iperf.exe')
		iperf_server_thread = threading.Thread(target=self.iperf_server)
		iperf_server_thread.start()
		iperf_client_thread = threading.Thread(target=self.iperf_client)
		iperf_client_thread.start()
		iperf_client_thread.join()
		self.iperf_kill_client('adb.exe')
		self.iperf_kill_client('iperf.exe')

	def iperf_kill_server(self):
		cpu_check = 'adb shell getprop ro.board.platform'
		value = os.popen(cpu_check).read().split('\n')[0]
		if value == 'sdm660':
			iperf_check = 'adb shell \"ps -lA | grep iperf | awk \'{print $4}\'\"'
		else:
			iperf_check = 'adb shell \"ps -lA | grep iperf | busybox awk \'{print $4}\'\"'
		if iperf_check:
			value = os.popen(iperf_check).read().split('\n')[0]
		try:
			os.system('adb shell kill ' + str(value))
			pass
		except Exception as e:
			pass

	def iperf_kill_client(self, name):
		os.system('taskkill /f /im ' + name)

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

	def strftime(self):
		return parameter_setting.get('project_name', 'name') + '_eth_iperf_py_' + \
				datetime + '.log'

if __name__ == '__main__':
	eth_iperf_py = eth_iperf_py()
	eth_iperf_py.iperf_thread()
	os.system('adb kill-server')
	os.system('adb start-server')
	os.system('adb devices')
	j = eth_iperf_py.finddevices_set()
	if j is False:
		os.system('adb connect ' + sys.argv[1] + ':5555')
	os.system('adb root')
	print('echo PASS >> testtool\\' + eth_iperf_py.strftime())
	os.system('echo PASS >> testtool\\' + eth_iperf_py.strftime())
	print('echo ' + eth_iperf_py.strftime() + ' >> project_name.log')
	os.system('echo ' + eth_iperf_py.strftime() + ' >> project_name.log')