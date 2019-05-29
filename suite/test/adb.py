
import subprocess, time, os

class adb():

	global sum_pass
	global sum_fail
	sum_pass = 0
	sum_fail = 0

	def _adb_shell(self, shell_cmds):
		global stdout, lines
		try:
			shell_cmds = shell_cmds + '; echo $?'
			cmds = ['adb', 'shell', shell_cmds]
			stdout = subprocess.Popen(cmds, stdout=subprocess.PIPE).communicate()[0].rstrip()
			lines = stdout.splitlines()
			# print('The adb shell was finished - PASS')
			# print(stdout)
			return stdout
		except:
			raise Exception('The adb shell was not finished - FAIL')

	def adb_command_set(self, value_dict):
		self._adb_shell(value_dict)

	def adb_response_get(self, value_dict):
		global sum_pass
		global sum_fail

		if value_dict in str(stdout):
			for get in range(16):
				if get == 8 or get == 15:
					print(str(lines[get]).split('b\'')[1])
					os.system('echo ' + echo + ' >> ping_server.txt')
				if get == 0 or get == 2 or get == 4 or get == 6 or get == 10 or get == 12 or get == 14:
					print(str(lines[get]).split('b\'')[1])
					echo = str(lines[get]).split('b\'')[1]
					os.system('echo ' + echo + ' >> ping_server.txt')
				else:
					pass
			sum_pass += 1
			print(sum_pass)
			print('Passed')
		else:
			echo = str(lines[0]).split('b\'')[1]
			os.system('echo ' + echo + ' >> ping_server.txt')
			sum_fail += 1
			print(sum_fail)
			print('Failed')

if __name__ == '__main__':
	os.system('del /s /q ping_server.txt')
	a = adb()
	av = int(input('Please input the \'Cycle Times\' you want : '))
	for loop in range(av):
		a.adb_command_set('ping -w 3 8.8.8.8')
		a.adb_response_get('0% packet loss')
	# print(str(av)+'................')
	# print(str(sum_pass)+'..................')
	# print(str(sum_fail)+'..................')
	os.system('echo ' + 'Cycle Times: ' + str(av) + ', Passed: ' + str(sum_pass) + ', Failed: ' + str(sum_fail) + ' >> ping_server.txt')
	print('Cycle Times: ' + str(av) + ', Passed: ' + str(sum_pass) + ', Failed: ' + str(sum_fail))