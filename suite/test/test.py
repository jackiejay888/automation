# import datetime,time

# # a = time.strftime("%Y-%m-%d_%H%M%S", time.localtime())

# # t1 = datetime.datetime.strptime("10:30:00", "%H:%M:%S")
# t1 = datetime.datetime.now()
# print(t1)

# time.sleep(5)
# t2 = datetime.datetime.now()
# print(t2)

# # t1 = datetime.datetime.strptime("10:30:00", "%H:%M:%S")
# # t2 = datetime.datetime.strptime("11:30:00", "%H:%M:%S")

# interval_time = (t2 - t1).seconds

# print(interval_time)
# 


'''------------------------------------------------------------------'''
import os
import time

# os.system('backup_log.bat')
# import datetime
# repeater_a = '192.168.50.111'
# repeater_b = '192.168.50.196'
# ipv4_start_time_secs = datetime.datetime.now()
# print('The start time of ip address catched : ' + str(ipv4_start_time_secs))
# # logging.info('The start time of ip address catched : ' + str(ipv4_start_time_secs))
# try:
# 	# for arp_loop in range(20):
# 	while True:
# 		os.system('arp -a 192.168.50.111 > ip_address_check.txt')
# 		if repeater_a in open('ip_address_check.txt').read():
# 			print("Catch the ip address of 192.168.50.111")
# 			# logging.warning("Catch the ip address of 192.168.50.111")
# 			ipv4_end_time_secs = datetime.datetime.now()
# 			print('The end time of ip address catched : ' + str(ipv4_end_time_secs))
# 			# logging.info('The end time of ip address catched : ' + str(ipv4_end_time_secs))
# 			break
# 		os.system('arp -a 192.168.50.196 > ip_address_check.txt')
# 		if repeater_b in open('ip_address_check.txt').read():
# 			print("Catch the ip address of 192.168.50.196")
# 			# logging.warning("Catch the ip address of 192.168.50.196")
# 			ipv4_end_time_secs = datetime.datetime.now()
# 			print('The end time of ip address catched : ' + str(ipv4_end_time_secs))
# 			# logging.info('The end time of ip address catched : ' + str(ipv4_end_time_secs))
# 			break
# 		print('Waiting for find the repeter ip address...')
# 	ipv4_interval_time_seconds = (ipv4_end_time_secs - ipv4_start_time_secs).seconds
# 	ipv4_interval_time_microseconds = (ipv4_end_time_secs - ipv4_start_time_secs).microseconds
# 	print('The interval time of swith to repeater is ' + str(ipv4_interval_time_seconds) +
# 		  '.' + str(ipv4_interval_time_microseconds) + ' seconds.')
# 	# logging.info('The interval time of swith to repeater is ' + str(ipv4_interval_time_seconds) +
# 		  # '.' + str(ipv4_interval_time_microseconds) + ' seconds.')
# 	pass
# except Exception as e:
# 	raise e

# os.system('arp_clear.bat')

# class te(object):

# 	def __init__(self):
# 		'''
# 		Constructor
# 		'''
# 		pass

# 	def test(self):
# 		# global the
# 		the = '1111'


# 	def test2(self):
# 		# global the
# 		print(the)

# if __name__ == '__main__':
# 	aaa = te()
# 	aaa.test()
# 	aaa.test2()


