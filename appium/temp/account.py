class Account():
	def __init__(self, number, name):
		self.number = number
		# print(self.number)
		# print(number)
		self.name = name
		self.balance = 0
	
	def deposit(self, amount):  #存款動作: amount代表存入金額
		# print(self.number)
		if amount <= 0:
			raise ValueError('must be positive')
		self.balance += amount
	
	def withdraw(self, amount): #取款動作: amount代表取款金額
		if amount <= self.balance:
			self.balance -= amount
		else:
			raise RuntimeError('balance not enough')

acct1 = Account('123–456–789', 'Justin') #開一個帳戶
acct1.deposit(100)
acct1.withdraw(30)
print(acct1.balance) #餘額是 70