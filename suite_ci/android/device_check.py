# -*- coding: utf-8 -*-
'''
Created on 2020/04/09

@author: ZL Chen
@title: Verify the device check and parameter setting.
'''

import configparser
from time import sleep


class Device_check(object):

	# device_check.ini 取出 Disable 的 key
	def verify(self):
		device_check_list_disable = []
		device_check_list_enable = []
		device_check = configparser.ConfigParser()
		device_check.read('.\ini\\device_check.ini', encoding='utf-8')
		suite_disable = device_check.items('suite_disable')

		length_suite_disable = len(suite_disable)
		for p in range(length_suite_disable):
			# print(suite_disable[p][0])
			device_check_list_disable.append(suite_disable[p][0])
		print('Disable section: ', device_check_list_disable)

		suite_enable = device_check.items('suite_enable')

		length_suite_enable = len(suite_enable)
		for p in range(length_suite_enable):
			# print(suite_enable[p][0])
			device_check_list_enable.append(suite_enable[p][0])
		print('Enable section: ', device_check_list_enable)
		return device_check_list_enable

	# device_check.ini 取出 Disable 的 key
	def verify_py(self):
		device_check_list_disable = []
		device_check_list_enable = []
		device_check = configparser.ConfigParser()
		device_check.read('.\ini\\device_check.ini', encoding='utf-8')
		suite_py_disable = device_check.items('suite_py_disable')

		length_suite_py_disable = len(suite_py_disable)
		for p in range(length_suite_py_disable):
			# print(suite_py_disable[p][0])
			device_check_list_disable.append(suite_py_disable[p][0])
		print('Disable section: ', device_check_list_disable)

		suite_py_enable = device_check.items('suite_py_enable')

		length_suite_py_enable = len(suite_py_enable)
		for p in range(length_suite_py_enable):
			# print(suite_py_enable[p][0])
			device_check_list_enable.append(suite_py_enable[p][0])
		print('Enable section: ', device_check_list_enable)
		return device_check_list_enable


if __name__ == '__main__':
	device_check = device_check()
	device_check.verify()
	device_check.verify_py()
