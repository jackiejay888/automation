'''
Created on 2019/08/13

@Title: Coding the HTML code base on the circle by multi color
@Author: ZL Chen
'''

import os
import imgkit
import configparser

config = configparser.ConfigParser()
config.read('luminance.config')


class luminance_multi(object):

	def fill_color(self, fill_color):
		if fill_color >= 6 or fill_color <= 0:
			raise
		numbers = {
			1: 'white',
			2: 'green',
			3: 'red',
			4: 'blue',
			5: 'black'
		}
		return numbers.get(fill_color, None)

	def stroke_color(self, stroke_color):
		if stroke_color >= 6 or stroke_color <= 0:
			raise
		numbers = {
			1: 'black',
			2: 'white',
			3: 'white',
			4: 'white',
			5: 'white'
		}
		return numbers.get(stroke_color, None)

	def initial(self):
		global fill_color, stroke_color
		try:
			w = int(config.get('luminance', 'w'))
			h = int(config.get('luminance', 'h'))
			aliquots = int(config.get('luminance', 'aliquots'))
			pixel_pitch = float(config.get('luminance', 'pixel_pitch'))
			point = int(input('Point (1 or 5 or 9) : '))
			solid_radius = float(config.get(
				'luminance', 'radius')) / pixel_pitch
			ask_edge_point = input('Edge point (y/n) ? ')

			if ask_edge_point == 'y':
				ask_edge_dis = input('MM or Pixel (mm or pixel) ? ')
				if ask_edge_dis == 'mm':
					edge = float(input('Edge (mm) ? ')) / pixel_pitch
				if ask_edge_dis == 'pixel':
					edge = float(input('Edge (pixel) ? '))

			for fill_color in range(1, 6):
				stroke_color = self.stroke_color(fill_color)
				fill_color = self.fill_color(fill_color)

				start = '<!DOCTYPE html>\n<html>\n<head>\n</head>\n<body bgcolor=\"' + \
					str(fill_color)+'\">\n'
				resolution = '<svg width=\"' + \
					str(w)+'\" height=\"' + str(h) + '\">\n'
				end = '</svg>\n</body>\n</html>\n'

				if ask_edge_point == 'y':
					body_edge = self.calculator_edge(
						w, h, edge, solid_radius, stroke_color, fill_color)
					fp = open(fill_color + '_edge.html', 'w')
					fp.write(start)
					fp.write(resolution)
					fp.write(body_edge)
					fp.write(end)

				body = self.calculator(w, h, aliquots, point,
									   solid_radius, stroke_color, fill_color)
				fp = open(fill_color + '.html', 'w')
				fp.write(start)
				fp.write(resolution)
				fp.write(body)
				fp.write(end)
		except Exception as e:
			raise e

	def calculator(self, w, h, aliquots, point, solid_radius, stroke_color, fill_color):
		coordinate_x = [w/aliquots, w/2, (aliquots-1)*w/aliquots]
		coordinate_y = [h/aliquots, h/2, (aliquots-1)*h/aliquots]
		try:
			if point == 1:
				print('('+str(coordinate_x[1])+','+str(coordinate_y[1])+')')
				return '<circle cx=\"'+str(coordinate_x[1])+'\" cy=\"'+str(coordinate_y[1])+'\" r=\"'+str(solid_radius)+'\" stroke=\"'+str(stroke_color)+'\" stroke-width=\"2'+'\" fill=\"'+str(fill_color) + '\" />\n'
			elif point == 5:
				print('('+str(coordinate_x[1])+','+str(coordinate_y[1])+')')
				print('('+str(coordinate_x[0])+','+str(coordinate_y[0])+')')
				print('('+str(coordinate_x[0])+','+str(coordinate_y[2])+')')
				print('('+str(coordinate_x[2])+','+str(coordinate_y[0])+')')
				print('('+str(coordinate_x[2])+','+str(coordinate_y[2])+')')
				return '<circle cx=\"'+str(coordinate_x[1])+'\" cy=\"'+str(coordinate_y[1])+'\" r=\"'+str(solid_radius) + \
					'\" stroke=\"'+str(stroke_color)+'\" stroke-width=\"2'+'\" fill=\"'+str(fill_color) + '\" />\n' + \
					'<circle cx=\"'+str(coordinate_x[0])+'\" cy=\"'+str(coordinate_y[0])+'\" r=\"'+str(solid_radius) + \
					'\" stroke=\"'+str(stroke_color)+'\" stroke-width=\"2'+'\" fill=\"'+str(fill_color) + '\" />\n' + \
					'<circle cx=\"'+str(coordinate_x[0])+'\" cy=\"'+str(coordinate_y[2])+'\" r=\"'+str(solid_radius) + \
					'\" stroke=\"'+str(stroke_color)+'\" stroke-width=\"2'+'\" fill=\"'+str(fill_color) + '\" />\n' + \
					'<circle cx=\"'+str(coordinate_x[2])+'\" cy=\"'+str(coordinate_y[0])+'\" r=\"'+str(solid_radius) + \
					'\" stroke=\"'+str(stroke_color)+'\" stroke-width=\"2'+'\" fill=\"'+str(fill_color) + '\" />\n' + \
					'<circle cx=\"'+str(coordinate_x[2])+'\" cy=\"'+str(coordinate_y[2])+'\" r=\"'+str(solid_radius) + \
					'\" stroke=\"' + \
					str(stroke_color)+'\" stroke-width=\"2' + \
					'\" fill=\"'+str(fill_color) + '\" />\n'
			elif point == 9:
				print('('+str(coordinate_x[1])+','+str(coordinate_y[1])+')')
				print('('+str(coordinate_x[1])+','+str(coordinate_y[1])+')')
				print('('+str(coordinate_x[1])+','+str(coordinate_y[0])+')')
				print('('+str(coordinate_x[1])+','+str(coordinate_y[2])+')')
				print('('+str(coordinate_x[0])+','+str(coordinate_y[1])+')')
				print('('+str(coordinate_x[2])+','+str(coordinate_y[1])+')')
				return '<circle cx=\"'+str(coordinate_x[1])+'\" cy=\"'+str(coordinate_y[1])+'\" r=\"'+str(solid_radius) + \
					'\" stroke=\"'+str(stroke_color)+'\" stroke-width=\"2'+'\" fill=\"'+str(fill_color) + '\" />\n' + \
					'<circle cx=\"'+str(coordinate_x[0])+'\" cy=\"'+str(coordinate_y[0])+'\" r=\"'+str(solid_radius) + \
					'\" stroke=\"'+str(stroke_color)+'\" stroke-width=\"2'+'\" fill=\"'+str(fill_color) + '\" />\n' + \
					'<circle cx=\"'+str(coordinate_x[0])+'\" cy=\"'+str(coordinate_y[2])+'\" r=\"'+str(solid_radius) + \
					'\" stroke=\"'+str(stroke_color)+'\" stroke-width=\"2'+'\" fill=\"'+str(fill_color) + '\" />\n' + \
					'<circle cx=\"'+str(coordinate_x[2])+'\" cy=\"'+str(coordinate_y[0])+'\" r=\"'+str(solid_radius) + \
					'\" stroke=\"'+str(stroke_color)+'\" stroke-width=\"2'+'\" fill=\"'+str(fill_color) + '\" />\n' + \
					'<circle cx=\"'+str(coordinate_x[2])+'\" cy=\"'+str(coordinate_y[2])+'\" r=\"'+str(solid_radius) + \
					'\" stroke=\"'+str(stroke_color)+'\" stroke-width=\"2'+'\" fill=\"'+str(fill_color) + '\" />\n' + \
					'<circle cx=\"'+str(coordinate_x[1])+'\" cy=\"'+str(coordinate_y[0])+'\" r=\"'+str(solid_radius) + \
					'\" stroke=\"'+str(stroke_color)+'\" stroke-width=\"2'+'\" fill=\"'+str(fill_color) + '\" />\n' + \
					'<circle cx=\"'+str(coordinate_x[1])+'\" cy=\"'+str(coordinate_y[2])+'\" r=\"'+str(solid_radius) + \
					'\" stroke=\"'+str(stroke_color)+'\" stroke-width=\"2'+'\" fill=\"'+str(fill_color) + '\" />\n' + \
					'<circle cx=\"'+str(coordinate_x[0])+'\" cy=\"'+str(coordinate_y[1])+'\" r=\"'+str(solid_radius) + \
					'\" stroke=\"'+str(stroke_color)+'\" stroke-width=\"2'+'\" fill=\"'+str(fill_color) + '\" />\n' + \
					'<circle cx=\"'+str(coordinate_x[2])+'\" cy=\"'+str(coordinate_y[1])+'\" r=\"'+str(solid_radius) + \
					'\" stroke=\"' + \
					str(stroke_color)+'\" stroke-width=\"2' + \
					'\" fill=\"'+str(fill_color) + '\" />\n'
			else:
				raise Exception('Failed.')
		except Exception as e:
			raise e

	def calculator_edge(self, w, h, edge, solid_radius, stroke_color, fill_color):
		edge_x = [edge, w/2, w-edge]
		edge_y = [edge, h/2, h-edge]
		try:
			print('('+str(edge_x[0])+','+str(edge_y[0])+')')
			print('('+str(edge_x[0])+','+str(edge_y[1])+')')
			print('('+str(edge_x[0])+','+str(edge_y[2])+')')
			print('('+str(edge_x[1])+','+str(edge_y[0])+')')
			print('('+str(edge_x[1])+','+str(edge_y[2])+')')
			print('('+str(edge_x[2])+','+str(edge_y[0])+')')
			print('('+str(edge_x[2])+','+str(edge_y[1])+')')
			print('('+str(edge_x[2])+','+str(edge_y[2])+')')
			return '<circle cx=\"'+str(edge_x[0])+'\" cy=\"'+str(edge_y[0])+'\" r=\"'+str(solid_radius) + \
				'\" stroke=\"'+str(stroke_color)+'\" stroke-width=\"2'+'\" fill=\"'+str(fill_color)+'\" />\n' + \
				'<circle cx=\"'+str(edge_x[0])+'\" cy=\"'+str(edge_y[1])+'\" r=\"'+str(solid_radius) + \
				'\" stroke=\"'+str(stroke_color)+'\" stroke-width=\"2'+'\" fill=\"'+str(fill_color)+'\" />\n' + \
				'<circle cx=\"'+str(edge_x[0])+'\" cy=\"'+str(edge_y[2])+'\" r=\"'+str(solid_radius) + \
				'\" stroke=\"'+str(stroke_color)+'\" stroke-width=\"2'+'\" fill=\"'+str(fill_color)+'\" />\n' + \
				'<circle cx=\"'+str(edge_x[1])+'\" cy=\"'+str(edge_y[0])+'\" r=\"'+str(solid_radius) + \
				'\" stroke=\"'+str(stroke_color)+'\" stroke-width=\"2'+'\" fill=\"'+str(fill_color)+'\" />\n' + \
				'<circle cx=\"'+str(edge_x[1])+'\" cy=\"'+str(edge_y[2])+'\" r=\"'+str(solid_radius) + \
				'\" stroke=\"'+str(stroke_color)+'\" stroke-width=\"2'+'\" fill=\"'+str(fill_color)+'\" />\n' + \
				'<circle cx=\"'+str(edge_x[2])+'\" cy=\"'+str(edge_y[0])+'\" r=\"'+str(solid_radius) + \
				'\" stroke=\"'+str(stroke_color)+'\" stroke-width=\"2'+'\" fill=\"'+str(fill_color)+'\" />\n' + \
				'<circle cx=\"'+str(edge_x[2])+'\" cy=\"'+str(edge_y[1])+'\" r=\"'+str(solid_radius) + \
				'\" stroke=\"'+str(stroke_color)+'\" stroke-width=\"2'+'\" fill=\"'+str(fill_color)+'\" />\n' + \
				'<circle cx=\"'+str(edge_x[2])+'\" cy=\"'+str(edge_y[2])+'\" r=\"'+str(solid_radius) + \
				'\" stroke=\"'+str(stroke_color)+'\" stroke-width=\"2' + \
				'\" fill=\"'+str(fill_color) + '\" />\n'
		except Exception as e:
			raise e

	def htmltoimage(self, fill_color):
		if os.path.isfile(self.fill_color(fill_color) + '.html'):
			imgkit.from_file(self.fill_color(fill_color) +
							 '.html', self.fill_color(fill_color) + '.jpg')
		else:
			pass

	def htmltoimage_edge(self, fill_color):
		if os.path.isfile(self.fill_color(fill_color) + '_edge.html'):
			imgkit.from_file(self.fill_color(
				fill_color) + '_edge.html', self.fill_color(fill_color) + '_edge.jpg')
		else:
			pass


if __name__ == '__main__':
	os.system('del /f /q *.html')
	os.system('del /f /q *.jpg')
	luminance = luminance_multi()
	luminance.initial()
	for fill_color in range(1, 6):
		luminance.htmltoimage(fill_color)
		luminance.htmltoimage_edge(fill_color)
	os.system('del /f /q *.html')
