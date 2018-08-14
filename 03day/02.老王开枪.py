class ren():
	def __init__(self,name):
		self.name=name
	def zhangzidan(self,dj,qiang):	
		dj.addqiang(qiang)
	
class qiang():
	def __init__(self,name):
		self.name=name
	def zhuangdanjia(self,dj,qiang):
		qiang.adddj(dj)
	def adddanjia(self,dj):
		self.dj=dj


class danjia():
	def __init__(self,rong):
		self.rong=rong
		self.zds = []
	def zhaungzidan(zd):
		self.zds.append(zd)
	

class zhidan():
	def __init__(self,shanghai,xinghao):
		self.shanghai=shanghai
		self.xinghao=xinghao




lapwang = ren("老王")
q=qiang("ak47")
dj=danjia(40)
for i in range(40):
	zd=zhidan(35,7.62)
	laowang.zhaungzidan(dj,zd)
laownag.zhuangzidan("ak47",40)













