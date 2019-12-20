# class Animal():
# 	def __init__(self, name):
# 		self.name = name


# a = Animal("dog")  # 建立一個名叫dog的Animal實體(物件)
# print(a.name)



class main():

	def __init__(self, name=default):
		self.name = name
		# print(self.name)

	def who(self):
		return self.name

if __name__ == '__main__':
	# main('dog')
	a = main('dog')
	print(a.who)