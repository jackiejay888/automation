# -*- coding: utf-8 -*-
'''
Created on 2020/03/21

@author: ZL Chen
@title: USC130-A8-Testtool adb command merge
'''

import os
import sys
sys.path.append('..\\parser_log')
from testcase_db import testcase_db

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

def adb_cmd(cmds):
	try:
		os.system('adb ' + cmds)
		pass
	except Exception as e:
		raise e

def log_export(testcase_list):
	for testcase_n in range(len(testcase_list)):
		adb_shell_cmd('/data/USC130-A8-Testtool/' + respone_testcase[testcase_n] + '.sh' \
						' > USC130-A8-Testtool/' + respone_testcase[testcase_n] + '.log')
		print('/data/USC130-A8-Testtool/' + respone_testcase[testcase_n] + '.sh' \
						' > USC130-A8-Testtool/' + respone_testcase[testcase_n] + '.log')
		adb_push_cmd('USC130-A8-Testtool/' + respone_testcase[testcase_n] + '.log' \
						' /data/USC130-A8-Testtool/')
		print('USC130-A8-Testtool/' + respone_testcase[testcase_n] + '.log' \
						' /data/USC130-A8-Testtool/')

os.system('del /f /q USC130-A8-Testtool\\*.log')
adb_cmd('kill-server')
adb_cmd('start-server')
adb_cmd('root')
adb_shell_cmd('rm -rf /data/USC130-A8-Testtool')
adb_shell_cmd('mkdir /data/USC130-A8-Testtool')
os.system('adb push USC130-A8-Testtool /data/')
adb_shell_cmd('chmod 777 /data/USC130-A8-Testtool/*')

testcase_db = testcase_db()
respone_testcase = testcase_db.db_parser('..\\db\\testcase.db')
log_export(respone_testcase)


# adb_shell_cmd('/data/USC130-A8-Testtool/USC130-A8_SystemInformation.sh > USC130-A8-Testtool/USC130-A8_SystemInformation.log')
# adb_shell_cmd('/data/USC130-A8-Testtool/USC130-A8_Storage_eMMC.sh > USC130-A8-Testtool/USC130-A8_Storage_eMMC.log')
# adb_shell_cmd('/data/USC130-A8-Testtool/USC130-A8_Backlight.sh > USC130-A8-Testtool/USC130-A8_Backlight.log')
# adb_shell_cmd('/data/USC130-A8-Testtool/USC130-A8_RTC.sh > USC130-A8-Testtool/USC130-A8_RTC.log')
# adb_shell_cmd('/data/USC130-A8-Testtool/USC130-A8_UsbDisk_Sdcard.sh > USC130-A8-Testtool/USC130-A8_UsbDisk_Sdcard.log')

# # Add Carmera, RFID, Wifi shell script
# adb_shell_cmd('/data/USC130-A8-Testtool/USC130-A8_Camera.sh > USC130-A8-Testtool/USC130-A8_Camera.log')
# adb_shell_cmd('/data/USC130-A8-Testtool/USC130-A8_RFID.sh > USC130-A8-Testtool/USC130-A8_RFID.log')
# adb_shell_cmd('/data/USC130-A8-Testtool/USC130-A8_Wifi.sh > USC130-A8-Testtool/USC130-A8_Wifi.log')

# adb_push_cmd('USC130-A8-Testtool/USC130-A8_SystemInformation.log /data/USC130-A8-Testtool/')
# adb_push_cmd('USC130-A8-Testtool/USC130-A8_Storage_eMMC.log /data/USC130-A8-Testtool/')
# adb_push_cmd('USC130-A8-Testtool/USC130-A8_Backlight.log /data/USC130-A8-Testtool/')
# adb_push_cmd('USC130-A8-Testtool/USC130-A8_RTC.log /data/USC130-A8-Testtool/')
# adb_push_cmd('USC130-A8-Testtool/USC130-A8_UsbDisk_Sdcard.log /data/USC130-A8-Testtool/')

# # Push Carmera, RFID, Wifi shell script
# adb_push_cmd('USC130-A8-Testtool/USC130-A8_Camera.log /data/USC130-A8-Testtool/')
# adb_push_cmd('USC130-A8-Testtool/USC130-A8_RFID.log /data/USC130-A8-Testtool/')
# adb_push_cmd('USC130-A8-Testtool/USC130-A8_Wifi.log /data/USC130-A8-Testtool/')
