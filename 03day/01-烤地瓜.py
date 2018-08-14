class DiGua():
	def __init__(self):
		self.zt = "生的"
		self.times = 0
	def __str__(self):	
		a = "我烤的程度 "
	def cook(self,time):
		self.times+=time
		if self.times >= 1 and self.times <= 3:
			self.zt = "生的"
		elif self.times >= 4 and self.times <= 6:
			self.zt = "不熟"
		elif self.times >= 7 and self.times <= 9:
			self.zt = "半生不熟"
		elif self.times >= 10 and self.times <= 12:
			self.zt = "熟"			
		elif self.times >= 13:
			self.zt = "焦了"


diguo=DiGua()
diguo.cook




