class car():
	def __init__(self,yan,xing):
		self.yan = yan	
		self.xing = xing
	def __str__(self):
		a = ("我的颜色是%s,我的型号是%s"%(self.yan,self.xing))
		return a

	def yi(self):
		print("跑")
	def ting(self):
		print("我的祖国")

che=car("黑色","宝马x6")
che.yi()
che.ting()
#print("我的颜色是:%s"%(che.yan))
#print("我的型号是:%s"%(che.xing))
print(che)













