import random
class yuexi():
	def bihua(self):

#1------石头
#2------剪刀
#3------布
		com = random.randint(1,3)#系统随机出拳
		com1 = int(input("请您出拳: 1.石头.2剪刀.3布"))
		if com<4 and com > 0:
			if (com==1 and com1==2) or (com==2 and com1==3) or (com==3 and com1==1):
				print("系统赢")
			elif com == com1:
				print("平局")
			else:
				print("玩家赢")
		else:
			print("输入不合法")
wj=yuexi()
wj.bihua()















