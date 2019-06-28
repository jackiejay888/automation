# -*- coding: utf-8 -*-
'''
Created on 2019/06/28

@author: ZL Chen
@title: Judgment the screenshot is same or different.
'''

import os
import time
import cv2
import argparse
import imutils
import pyscreenshot
from skimage.measure import compare_ssim


class cv_devicefinder(object):

	def screenshot(self, screenshot):
		image = pyscreenshot.grab()
		image.save(screenshot)
		pass

	def compare_image(self, screenshot_1, screenshot_2):
		self.imageA = cv2.imread(screenshot_1)
		self.imageB = cv2.imread(screenshot_2)
		self.grayA = cv2.cvtColor(self.imageA, cv2.COLOR_BGR2GRAY)
		self.grayB = cv2.cvtColor(self.imageB, cv2.COLOR_BGR2GRAY)
		self._diff()
		self._find_diff()
		pass

	def _diff(self):
		(score, self.diff) = compare_ssim(self.grayA, self.grayB, full=True)
		self.diff = (self.diff * 255).astype('uint8')
		print('SSIM: {}'.format(score))
		if score == 1.0:
			print('The screenshot is same with 1 and 2.')
		else:
			print('The screenshot is different with 1 and 2.')
		pass

	def _find_diff(self):
		thresh = cv2.threshold(
			self.diff, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
		cnts = cv2.findContours(
			thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
		cnts = cnts[0]
		for c in cnts:
			(x, y, w, h) = cv2.boundingRect(c)
			cv2.rectangle(self.imageA, (x, y), (x+w, y+h), (0, 0, 255), 2)
			cv2.rectangle(self.imageB, (x, y), (x+w, y+h), (0, 0, 255), 2)
		cv2.imwrite('compare_resulte.jpg', self.imageB)
		cv2.imshow('compare_resulte', self.imageB)
		cv2.waitKey(0)
		pass


if __name__ == '__main__':
	os.system('del /f /q *.jpg')
	opencv = cv_devicefinder()
	for count in range(2):
		for wait in range(10):
			time.sleep(1)
			print('Waiting...')
		opencv.screenshot('screenshot_' + str(count + 1) + '.jpg')
		print('Screenshot the ' + '\'screenshot_' + str(count + 1) + '.jpg\'')
	opencv.compare_image('screenshot_1.jpg', 'screenshot_2.jpg')
