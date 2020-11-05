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
		os.system(self._ssh() + 'root@' + sys.argv[1] + ' \"/data/testtool/iperf -s -i 5\"')
		print(self._ssh() + 'root@' + sys.argv[1] + ' \"/data/testtool/iperf -s -i 5\"')
		pass

	def iperf_client(self):
		print('iperf client is starting.\nPlease waiting ' + sys.argv[3] + ' secs.')
		os.system('.\\app\\iperf.exe -c ' + sys.argv[1] + ' -w ' + sys.argv[2] + ' -t ' + 
					sys.argv[3] + ' -i ' + sys.argv[4] + ' -d > ' + 'testtool\\' + self.strftime())
		print('.\\app\\iperf.exe -c ' + sys.argv[1] + ' -w ' + sys.argv[2] + ' -t ' + 
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
		self.iperf_kill_client('ssh.exe')
		self.iperf_kill_client('scp.exe')
		self.iperf_kill_client('iperf.exe')

	def iperf_kill_server(self):
		os.system(self._ssh() + 'root@' + sys.argv[1] + ' \"killall iperf\"')
		print(self._ssh() + 'root@' + sys.argv[1] + ' \"killall iperf\"')

	def iperf_kill_client(self, name):
		os.system('taskkill /f /im ' + name)

	def strftime(self):
		return parameter_setting.get('project_name', 'name') + '_eth_iperf_py_' + datetime + '.log'

	def _ssh(self):
		return '.\\app\\ssh.exe -o StrictHostKeyChecking=no '

if __name__ == '__main__':
	eth_iperf_py = eth_iperf_py()
	eth_iperf_py.iperf_thread()
	print('echo PASS >> testtool\\' + eth_iperf_py.strftime())
	os.system('echo PASS >> testtool\\' + eth_iperf_py.strftime())
	print('echo ' + eth_iperf_py.strftime() + ' >> project_name.log')
	os.system('echo ' + eth_iperf_py.strftime() + ' >> project_name.log')