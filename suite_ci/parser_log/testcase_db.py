# -*- coding: utf-8 -*-
'''
Created on 2020/03/21

@author: ZL Chen
@title: testcase database
'''

import os
import sqlite3


class testcase_db(object):
	# # Initial test case name
	# global testcase_list, backlight, rtc, storage_emmc, systeminformation, usbdisk_sdcard
	# backlight = 'USC130-A8_Backlight'
	# rtc = 'USC130-A8_RTC'
	# storage_emmc = 'USC130-A8_Storage_eMMC'
	# systeminformation = 'USC130-A8_SystemInformation'
	# usbdisk_sdcard = 'USC130-A8_UsbDisk_Sdcard'
	# testcase_list = [backlight, rtc, storage_emmc,
	# 				 systeminformation, usbdisk_sdcard]

	def db_parser(self, db_location):
		sum_list = []
		# os.system('del testcase.db')
		try:
			conn = sqlite3.connect(db_location)
			connect = conn.cursor()
			# # Create table
			# connect.execute('CREATE TABLE testcase (testcase text)')
			# # Insert a row of data
			# for testcase_loop in range(len(testcase_list)):
			# 	connect.execute(
			# 		'INSERT INTO testcase VALUES (\"' + testcase_list[testcase_loop] + '\")')
			# # Save (commit) the changes
			# conn.commit()
			for row in connect.execute('SELECT * FROM testcase'):
				sum_list.append(row[0])
			return sum_list
			conn.close()
			print('The data is insert to the database.')
			pass
		except Exception as e:
			raise e


if __name__ == '__main__':
	testcase_db = testcase_db()
	testcase_db_content = testcase_db.db_parser('..\\db\\testcase.db')
	for loop in range(len(testcase_db_content)):
		print(testcase_db_content[loop])
