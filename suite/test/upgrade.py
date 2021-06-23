# Package Upgrade
# Author: ZL Chen

def run():
	while True:
		number = input("1. 104 2. Advantech :")
		if number == str(1):
			origin = input("Monthly Package: ")
			years = input("Number of years: ")
			percentage = float(input("Percentage: "))
			origin = float(origin)
			print("Now, your package is " + str(origin))
			for i in range(int(years)):
				origin *= 1+percentage
				summary = str(origin)
				print("The " + str(i+1) + " years later, your package is " + summary)
		elif number == str(2):
			origin = input("Monthly Package: ")
			years = input("Number of years: ")
			Add = 2000
			origin = float(origin)
			print("Now, your package is " + str(origin))
			for i in range(int(years)):
				origin += Add
				summary = str(origin)
				print("The " + str(i+1) + " years later, your package is " + summary)
		elif number == 'exit':
			break
		else:
			pass

run()