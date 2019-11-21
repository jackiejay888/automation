# -*- coding: utf-8 -*-
'''
Created on 2019/11/14

@author: ZL Chen
@title: PXE
'''

import os


class pxe(object):

	global count

	def operational(self):
		count = 0
		try:
			os.system('copy \"%SystemRoot%\\System32\\Winevt\\Logs\\Microsoft-Windows-Deployment-Services-Diagnostics%4Operational.evtx\" "C:\\Users\\Administrator\\Desktop\\Sublime\\pxe\\operational.evtx\"')
			print('Waiting......\nCopy the .evtx to local.')
			os.system(
				'python C:\\Python36\\Scripts\\evtx_dump.py operational.evtx > operational.txt')
			operational = open('operational.txt', 'r')
			for line in operational:
				content = line.split('\n')[0]
				if content == '<EventID Qualifiers="">4112</EventID>':
					count = count + 1
			os.system('echo Passed: ' +
					  str(count) + ' >> operational.txt')
		except Exception as e:
			raise e

	def application(self):
		count = 0
		try:
			os.system('copy \"%SystemRoot%\\System32\\Winevt\\Logs\\Application.evtx\" "C:\\Users\\Administrator\\Desktop\\Sublime\\pxe\\application.evtx\"')
			print('Waiting......\nCopy the .evtx to local.')
			os.system(
				'python C:\\Python36\\Scripts\\evtx_dump.py application.evtx > application.txt')
			application = open('application.txt', 'r')
			for line in application:
				content = line.split('\n')[0]
				if content == '<EventID Qualifiers="49409">772</EventID>':
					count = count + 1
				if content == '<EventID Qualifiers="49152">8198</EventID>':
					count = count + 1
			os.system('echo Error: ' +
					  str(count) + ' >> application.txt')
		except Exception as e:
			raise e


if __name__ == '__main__':
	pxe = pxe()
	pxe.operational()
	pxe.application()
