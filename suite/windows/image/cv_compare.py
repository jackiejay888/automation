# -*- coding: utf-8 -*-
'''
Created on 2019/07/05

@author: ZL Chen
@title: Judgment the screenshot is same or different.
'''

import os
import time
import cv2
import argparse
import imutils
import pyscreenshot
import configparser
from skimage.measure import compare_ssim
from cv_original import cv_original

config = configparser.ConfigParser()
config.read('.\\config\\cv.config')


class cv_compare(object):

	def screenshot(self, screenshot):
		image = pyscreenshot.grab()
		image.save(screenshot)
		pass

	def compare_image(self, original, other, now_time):
		self.image_original = cv2.imread(original)
		self.image_other = cv2.imread(other)
		self.gray_original = cv2.cvtColor(
			self.image_original, cv2.COLOR_BGR2GRAY)
		self.gray_other = cv2.cvtColor(self.image_other, cv2.COLOR_BGR2GRAY)
		boolean = self._diff()
		self._find_diff(boolean, now_time)
		pass

	def _diff(self):
		(score, self.diff) = compare_ssim(
			self.gray_original, self.gray_other, full=True)
		self.diff = (self.diff * 255).astype('uint8')
		# print('SSIM: {}'.format(score))
		if score == 1.0:
			return True
		else:
			return False

	def _find_diff(self, boolean, now_time):
		thresh = cv2.threshold(
			self.diff, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
		cnts = cv2.findContours(
			thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
		cnts = cnts[0]
		for c in cnts:
			(x, y, w, h) = cv2.boundingRect(c)
			cv2.rectangle(self.image_original, (x, y),
						  (x + w, y + h), (0, 0, 255), 2)
			cv2.rectangle(self.image_other, (x, y),
						  (x + w, y + h), (0, 0, 255), 2)
		if boolean == False:
			cv2.imwrite('failed_' + now_time + '.jpg', self.image_other)
			#cv2.imshow('failed_', self.image_other)
			cv2.waitKey(0)
			raise Exception('The compare image is failed.')
		else:
			print('The compare image is passed.')
			pass
			

if __name__ == '__main__':
	cv_original = cv_original()
	cv_compare = cv_compare()
	wait_time = config.get('cv', 'wait_time_secs')
	print('Waiting ' + wait_time + ' secs......')
	for loop in range(int(wait_time)):
		time.sleep(1)
	now_time = time.strftime("%Y-%m-%d_%H%M%S", time.localtime())
	cv_original.screenshot('other_' + now_time + '.jpg')
	print('Screenshot the others.jpg')
	cv_compare.compare_image('original.jpg', 'other_' +
							 now_time + '.jpg', now_time)