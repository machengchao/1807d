class dog():
	def __init__(self,name,age):
		self.name=name
		self.__age = 0
	def shiyou(self,age):
		if age > 15 and age <1:
			print("不")
		else:
			self.__age=age
	def getAge(self):
		return self.__age			
		

	


hsq=dog("隋静",13)
#Dog=dog("隋靖",18)
#sj=dog("隋静",21)
#print(Dog.name,Dog.age)
#print(sj.name,sj.age)
hsq.setAge(12)
print(hsq.getAge())



