import os
import time

class Envir_Install(object):
	
	def Delete_Head(self):
		with open('source.txt', 'r') as fin:
			data = fin.read().splitlines(True)
		with open('local.txt', 'w') as fout:
			fout.writelines(data[2:])

	def Split_Package(self):
		with open('local.txt', 'r') as f: 
			global newlines
			filename = "local.txt"		
			myfile = open(filename) 
			newlines = len(myfile.readlines()) 

			data = f.read().split('\n')
			os.system("del install_package.txt")
			for i in range(0,newlines):
				a = data[i]
				b = a.split(' ')[0]	
				hs = open("install_package.txt","a")
				hs.write(b+"\n")
				hs.close() 

	def Install_Package(self):
		filename = "install_package.txt"		
		myfile = open(filename) 
		newlines = len(myfile.readlines()) 
		for i in range(0,newlines):
			f1 = open('install_package.txt', 'r').readlines()
			os.system('pip install '+f1[i])

	def Install_pip(self,filename):
		os.system('python -m pip install --upgrade '+filename)

if __name__ == "__main__":
	TC = Envir_Install()
	TC.Install_pip('pip')
	TC.Install_pip('setuptools')
	time.sleep(2)
	TC.Delete_Head()
	time.sleep(2)
	TC.Split_Package()
	time.sleep(2)
	TC.Install_Package()

