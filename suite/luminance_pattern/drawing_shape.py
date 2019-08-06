'''
Created on 2019/08/02

@Author: ZL Chen
@Title: Drawing the graphic and make sure the Continuity.
'''

import turtle


class drawing_shape(object):

	def drawing(self):

		pixel = int(input('Input the pixel internal unit : '))
		square = int(input('Input the number of square : '))
		forward = 1
		turtle.hideturtle()
		turtle.color('red')

		for i in range(square*4):
		    turtle.forward(forward)
		    turtle.right(90)
		    forward += pixel

if __name__ == '__main__':
	dr = drawing_shape()
	dr.drawing()