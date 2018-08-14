class Dog():
	__instance = None
	flog = False
	
	def __init__(self):
	if 
	def __new__(cls):
		if cls.__instance == None:
			cls.__instance=super().__new__(cls)
			return cls.__instance
		else:
			return cls.__instance




	




dog = Dog()
print(id(dog))
dog1 = Dog()
print(id(dog1))


