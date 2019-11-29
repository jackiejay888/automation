# -*- coding: utf-8 -*-
'''
Created on 2019/11/14

@author: ZL Chen
@title: PXE
'''

import os
import datetime


class pxe(object):

	def operational(self):
		count = 0
		timer = []
		try:
			os.system('copy \"%SystemRoot%\\System32\\Winevt\\Logs\\Microsoft-Windows-Deployment-Services-Diagnostics%4Operational.evtx\" "C:\\Users\\Administrator\\Desktop\\Sublime\\pxe\\operational.evtx\"')
			print('Waiting......\nCopy the .evtx to local.')
			os.system(
				'python C:\\Python36\\Scripts\\evtx_dump.py operational.evtx > operational.txt')
			operational = open('operational.txt', 'r')
			for operational_loop in operational:
				content = operational_loop.split('\n')[0]
				if '<EventID Qualifiers="">4112</EventID>' in content:
					count = count + 1
				if content == '</Events>':
					os.system('echo Total pass times: ' +
							  str(count) + ' >> operational_result.txt')
				if 'TimeCreated SystemTime=' in content:
					times = content.split('<')[1].split('>')[0].split(
						'TimeCreated SystemTime=')[1].split('\"')[1].split('.')[0]
					timer.append(times)
			self.timer(timer[0], timer[-1], 'operational_result')
		except Exception as e:
			raise e

	def application(self):
		count_1 = 0
		cound_2 = 0
		timer = []
		try:
			os.system('copy \"%SystemRoot%\\System32\\Winevt\\Logs\\Application.evtx\" "C:\\Users\\Administrator\\Desktop\\Sublime\\pxe\\application.evtx\"')
			print('Waiting......\nCopy the .evtx to local.')
			os.system(
				'python C:\\Python36\\Scripts\\evtx_dump.py application.evtx > application.txt')
			application = open('application.txt', 'r')
			for application_loop in application:
				content = application_loop.split('\n')[0]
				if content == '<EventID Qualifiers="49409">772</EventID>':
					count_1 = count_1 + 1
				if content == '<EventID Qualifiers="49152">8198</EventID>':
					cound_2 = cound_2 + 1
				if content == '</Events>':
					os.system('echo Total ip connection error times: ' +
							  str(count_1) + ' >> application_result.txt')
					os.system('echo Total license error times: ' +
							  str(cound_2) + ' >> application_result.txt')
				if 'TimeCreated SystemTime=' in content:
					times = content.split('<')[1].split('>')[0].split(
						'TimeCreated SystemTime=')[1].split('\"')[1].split('.')[0]
					timer.append(times)
			self.timer(timer[0], timer[-1], 'application_result')
		except Exception as e:
			raise e

	def timer(self, start_time, end_time, txt):
		d1 = datetime.datetime.strptime(start_time, '%Y-%m-%d %H:%M:%S')
		d2 = datetime.datetime.strptime(end_time, '%Y-%m-%d %H:%M:%S')
		delta = d2 - d1
		os.system('echo Start time: ' + start_time + ' >> ' + txt + '.txt')
		os.system('echo End time: ' + end_time + ' >> ' + txt + '.txt')
		os.system('echo Take the Number of days and hours : ' + str(delta.days) + ' days and ' +
				  str(round(float(delta.seconds)/3600, 2)) + ' hours' + ' >> ' + txt + '.txt')


if __name__ == '__main__':
	pxe = pxe()
	os.system('del /f /q ' + '*.evtx *.txt')
	pxe.operational()
	pxe.application()
