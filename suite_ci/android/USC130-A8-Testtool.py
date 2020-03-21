# -*- coding: utf-8 -*-
'''
Created on 2020/03/21

@author: ZL Chen
@title: USC130-A8-Testtool adb command merge
'''

import os

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

adb_cmd('kill-server')
adb_cmd('start-server')
adb_cmd('root')
adb_shell_cmd('rm -rf /data/USC130-A8-Testtool')
adb_shell_cmd('mkdir /data/USC130-A8-Testtool')
os.system('adb push USC130-A8-Testtool /data/')
adb_shell_cmd('chmod 777 /data/USC130-A8-Testtool/*')


adb_shell_cmd('/data/USC130-A8-Testtool/USC130-A8_SystemInformation.sh > USC130-A8-Testtool/USC130-A8_SystemInformation.log')
adb_shell_cmd('/data/USC130-A8-Testtool/USC130-A8_Storage_eMMC.sh > USC130-A8-Testtool/USC130-A8_Storage_eMMC.log')
adb_shell_cmd('/data/USC130-A8-Testtool/USC130-A8_Backlight.sh > USC130-A8-Testtool/USC130-A8_Backlight.log')
adb_shell_cmd('/data/USC130-A8-Testtool/USC130-A8_RTC.sh > USC130-A8-Testtool/USC130-A8_RTC.log')
adb_shell_cmd('/data/USC130-A8-Testtool/USC130-A8_UsbDisk_Sdcard.sh > USC130-A8-Testtool/USC130-A8_UsbDisk_Sdcard.log')

adb_push_cmd('USC130-A8-Testtool/USC130-A8_SystemInformation.log /data/USC130-A8-Testtool/' )
adb_push_cmd('USC130-A8-Testtool/USC130-A8_Storage_eMMC.log /data/USC130-A8-Testtool/' )
adb_push_cmd('USC130-A8-Testtool/USC130-A8_Backlight.log /data/USC130-A8-Testtool/' )
adb_push_cmd('USC130-A8-Testtool/USC130-A8_RTC.log /data/USC130-A8-Testtool/' )
adb_push_cmd('USC130-A8-Testtool/USC130-A8_UsbDisk_Sdcard.log /data/USC130-A8-Testtool/' )
