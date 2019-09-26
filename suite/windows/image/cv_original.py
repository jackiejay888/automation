# -*- coding: utf-8 -*-
'''
Created on 2019/07/05

@author: ZL Chen
@title: Screenshot the original.
'''

import os
import pyscreenshot


class cv_original(object):

	def screenshot(self, screenshot):
		image = pyscreenshot.grab()
		image.save(screenshot)
		pass

	def screenshot_original(self):
		os.system('del /f /q *.jpg')
		self.screenshot('original.jpg')
		print('Screenshot the original.jpg')


if __name__ == '__main__':
	cv = cv_original()
	cv.screenshot_original()
