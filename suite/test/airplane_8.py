import os
import time
import subprocess


def ethernet():
	_adb_connect('disconnect', ' ')
	_adb_connect('connect', '192.168.32.229')
	time.sleep(6)
	print('The ethernet is finished.')


def _adb_connect(connect, shell_cmds):
	global stdout
	global lines
	shell_cmds = shell_cmds + '; echo $?'
	cmds = ['adb', connect, shell_cmds]
	stdout = subprocess.Popen(
		cmds, stdout=subprocess.PIPE).communicate()[0].rstrip()
	lines = stdout.splitlines()


def _adb_shell(shell_cmds):
	global stdout
	global lines
	shell_cmds = shell_cmds + '; echo $?'
	cmds = ['adb', 'shell', shell_cmds]
	stdout = subprocess.Popen(cmds, stdout=subprocess.PIPE).communicate()[0].rstrip()
	lines = stdout.splitlines()

def start_airplane():
	try:
		_adb_shell('settings put global airplane_mode_on 1')
		_adb_shell('su 0 am broadcast -a android.intent.action.AIRPLANE_MODE --ez state true')
		time.sleep(6)
		print('The Start airplane is finished.')
		pass
	except Exception as e:
		raise e


def stop_airplane():
	try:
		_adb_shell('settings put global airplane_mode_on 0')
		_adb_shell('su 0 am broadcast -a android.intent.action.AIRPLANE_MODE --ez state false')
		time.sleep(6)
		print('The Stop airplane is finished.')
		pass
	except Exception as e:
		raise e


ethernet()
for x in range(1):
	start_airplane()
	stop_airplane()
