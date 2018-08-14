class Bank():
	def __init__(self,name,acc,pwd):
		self.name=name
		self.acc=acc
		self.__pwd=pwd

	def getPwd(self):
		return self.__pwd

	def setPwd(self,pwd):
		self.__pwd=pwd

	



bank = Bank("隋静","123","456")
print(bank.name)
print(bank.acc)

print(bank.getPwd())



