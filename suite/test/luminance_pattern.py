# -*- coding: utf-8 -*-
'''
Create on 2019/08/01

@Author: ZL Chen
@Title: Drawing the graphic base on the panel.
'''

import turtle as tu
import configparser

config = configparser.ConfigParser()
config.read('luminance_pattern.config')


class luminance_pattern(object):

	def initial_color(self, background_color):
		numbers = {
			1: 'white',
			2: 'green',
			3: 'red',
			4: 'blue',
			5: 'black'
		}
		return numbers.get(background_color, None)

	def initial(self, shape_width, shape_height, ppi, aliquots, background_color):
		global circle_pixel
		circle_pixel = 22.5 / ppi
		choose = input('*Do you want to join the distance edge. (y/n)? ')
		if choose == 'n':
			tu.hideturtle()
			self.drawing(shape_width, shape_height,
						 aliquots, self.initial_color(background_color))
		elif choose == 'y':
			distance_edge = int(
				input('*Please input the distance edge. (mm): '))
			distance_edge = distance_edge / ppi
			tu.hideturtle()
			self.drawing(shape_width, shape_height,
						 aliquots, self.initial_color(background_color))
			self.drawing_join(shape_width, shape_height,
							  aliquots, distance_edge)
		else:
			raise Exception
		tu.exitonclick()

	def drawing(self, shape_width, shape_height, aliquots, color):
		width = shape_width / aliquots
		height = shape_height / aliquots
		tu.setup(width=shape_width, height=shape_height,
				 startx=None, starty=None)
		tu.pensize(5)
		tu.bgcolor(color)
		if color == 'white':
			tu.pencolor('red')
		else:
			tu.pencolor('white')
		tu.speed('fastest')
		if point == '1':
			self.pen_drawing(0, 0)
		elif point == '5':
			self.pen_drawing(0, 0)
			self.pen_drawing(width, height)
			self.pen_drawing(width, -height)
			self.pen_drawing(-width, height)
			self.pen_drawing(-width, -height)
		elif point == '9':
			self.pen_drawing(0, 0)
			self.pen_drawing(width, height)
			self.pen_drawing(width, -height)
			self.pen_drawing(-width, height)
			self.pen_drawing(-width, -height)
			self.pen_drawing(width, 0)
			self.pen_drawing(-width, 0)
			self.pen_drawing(0, height)
			self.pen_drawing(0, -height)
		else:
			raise Exception

	def drawing_join(self, shape_width, shape_height, aliquots, distance_edge):
		aliquots = shape_width / distance_edge
		width = shape_width - (shape_width / aliquots)
		height = shape_height - (shape_height / aliquots)
		self.pen_drawing(0, 0)
		self.pen_drawing(width, height)
		self.pen_drawing(width, -height)
		self.pen_drawing(-width, height)
		self.pen_drawing(-width, -height)
		self.pen_drawing(width, 0)
		self.pen_drawing(-width, 0)
		self.pen_drawing(0, height)
		self.pen_drawing(0, -height)

	def pen_drawing(self, goto_x, goto_y):
		tu.penup()
		tu.goto(goto_x, goto_y)
		tu.pendown()
		tu.circle(circle_pixel)


if __name__ == '__main__':
	global point
	shape_width = int(config.get('luminance_pattern', 'shape_width'))
	shape_height = int(config.get('luminance_pattern', 'shape_height'))
	ppi = float(config.get('luminance_pattern', 'ppi'))
	aliquots = int(config.get('luminance_pattern', 'aliquots'))
	point = config.get('luminance_pattern', 'point')
	background_color = int(input(
		'*Please select the background color. (1 or 2 or 3 or 4 or 5)\n1.White 2.Green 3.Red 4.Blue 5.Black: '))
	lp = luminance_pattern()
	lp.initial(shape_width, shape_height, ppi, aliquots, background_color)
