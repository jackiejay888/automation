# -*- coding: utf-8 -*-
'''
Created on 2019/06/28

@author: ZL Chen
@title: Judgment the screenshot is same or different.
'''

import os
import time
import cv2
import pyscreenshot
from skimage.measure import compare_ssim


class cv_devicefinder(object):

	def screenshot(self, screenshot):
		self.image = pyscreenshot.grab()
		self.image.save(screenshot)
		pass

	def compare_image(self, screenshot_1, screenshot_2):
		self.imageA = cv2.imread(screenshot_1)
		self.imageB = cv2.imread(screenshot_2)
		self.grayA = cv2.cvtColor(self.imageA, cv2.COLOR_BGR2GRAY)
		self.grayB = cv2.cvtColor(self.imageB, cv2.COLOR_BGR2GRAY)
		return(self._diff())
		self._find_diff()
		pass

	def _diff(self):
		(score, diff) = compare_ssim(self.grayA, self.grayB, full=True)
		print('SSIM: {}'.format(score))
		if score == 1.0:
			return('The compare is passed.')
		else:
			return('The compare is failed.')
		pass

	def _find_diff(self):
		thresh = cv2.threshold(
			diff, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
		cnts = cv2.findContours(
			thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
		cnts = cnts[0] if imutils.is_cv2() else cnts[1]
		for c in cnts:
			(x, y, w, h) = cv2.boundingRect(c)
			cv2.rectangle(imageA, (x, y), (x+w, y+h), (0, 0, 255), 2)
			cv2.rectangle(imageB, (x, y), (x+w, y+h), (0, 0, 255), 2)
		cv2.imshow('Modified', imageB)
		cv2.imwrite('haha2.jpg', imageB)
		cv2.waitKey(0)


if __name__ == '__main__':
	# os.system('del /f /q *.jpg')
	opencv = cv_devicefinder()
	# for count in range(2):
	# 	opencv.screenshot('screenshot_' + str(count + 1) + '.jpg')
	# 	print('Screenshot the ' + '\'screenshot_' + str(count + 1) + '.jpg\'')
	print(opencv.compare_image('screenshot_1.jpg', 'screenshot_2.jpg'))
