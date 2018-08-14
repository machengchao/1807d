class Dog():
	def __init__(self,name):
		self.name=name
		print("init")
	def __str__(self):
		return "我叫str"
	def __del__(self):
		print("我叫del")

dog=Dog("汤姆")
print(dog)
dog1=dog
del dog
print("哈哈")

