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


class cv(object):

	def screenshot(self, screenshot):
		image = pyscreenshot.grab()
		image.save(screenshot)
		pass

	def compare_image(self, original, other):
		self.image_original = cv2.imread(original)
		self.image_other = cv2.imread(other)
		self.gray_original = cv2.cvtColor(
			self.image_original, cv2.COLOR_BGR2GRAY)
		self.gray_other = cv2.cvtColor(self.image_other, cv2.COLOR_BGR2GRAY)
		boolean = self._diff()
		self._find_diff(boolean)
		pass

	def _diff(self):
		(score, self.diff) = compare_ssim(
			self.gray_original, self.gray_other, full=True)
		self.diff = (self.diff * 255).astype('uint8')
		print('SSIM: {}'.format(score))
		if score == 1.0:
			return True
		else:
			return False

	def _find_diff(self, boolean):
		thresh = cv2.threshold(
			self.diff, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
		cnts = cv2.findContours(
			thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
		cnts = cnts[0]
		for c in cnts:
			(x, y, w, h) = cv2.boundingRect(c)
			cv2.rectangle(self.image_original, (x, y),
						  (x+w, y+h), (0, 0, 255), 2)
			cv2.rectangle(self.image_other, (x, y), (x+w, y+h), (0, 0, 255), 2)
		cv2.imwrite('result.jpg', self.image_other)
		if boolean == False:
			cv2.imshow('result', self.image_other)
			cv2.waitKey(0)
			raise Exception('The compare image is failed.')
		else:
			print('The compare image is passed.')
			pass


if __name__ == '__main__':
	os.system('del /f /q *.jpg')
	cv = cv()
	screenshot_count = int(input('Please input the compare times you want: '))
	cv.screenshot('original.jpg')
	print('Screenshot the original.jpg')
	for count in range(screenshot_count):
		print('Compare Times: ' + str(count + 1))
		if count == screenshot_count:
			break
		for loop in range(5):
			print('Waiting.')
			time.sleep(1)
		cv.screenshot('other_' + str(count + 1) + '.jpg')
		print('Screenshot the others_' + str(count + 1) + '.jpg')
		cv.compare_image('original.jpg', 'other_' + str(count + 1) + '.jpg')
	os.system('.\\backup_log.bat')
