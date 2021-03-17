# -*- coding: utf-8 -*-
'''
Created on 2021/03/17

@author: ZL Chen
@title: Auto Test.
'''

import os

def run():
	abspath = os.path.abspath('.')
	listdir = os.listdir(abspath)
	listdir.remove('auto{py}'.format(py='.py'))
	listdir.remove('readme')
	# print(listdir)
	if listdir:
		for execute in range(len(listdir)):
			print('{run}'.format(run=listdir[execute]).strip('.py'), 'is execute.')
			os.system('python {run}'.format(run=listdir[execute]))
	else:
		print('{}'.format('None'))
		pass

run()