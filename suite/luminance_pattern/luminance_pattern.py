# -*- coding: utf-8 -*-
'''
Create on 2019/08/01

@Author: ZL Chen
@Title: Drawing the graphic base on the panel.
'''

import cv2


class luminance_pattern(object):

	def execute(self):
		shape_length = input('Please input the Length (mm): ')
		shape_width = input('Please input the Width (mm): ')
		print('The shape is', shape_width, '*', shape_length)
		aliquots = input('Please input the Aliquots : ')
		choose = input('Do you want join the distance edge. (y/n)? ')
		if choose == 'n':
			self.drawing(shape_length, shape_width, aliquots)
		elif choose == 'y':
			distance_edge = input('Please input the distance edge. (mm): ')
			self.drawing_join(shape_length, shape_width,
							  aliquots, distance_edge)
		else:
			raise Exception

	def drawing(self, shape_length, shape_width, aliquots):
		print(int(shape_length), int(shape_width), int(aliquots))

	def drawing_join(self, shape_length, shape_width, aliquots, distance_edge):
		print(int(shape_length), int(shape_width),
			  int(aliquots), int(distance_edge))


if __name__ == '__main__':
	lp = luminance_pattern()
	lp.execute()
