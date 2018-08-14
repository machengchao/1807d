
import random 
i = 0
num = random.randint(1,100)
while i<9:
	a=int(input("请输入猜的数字:"))
	if a> num:
		print("你猜大了兄弟")
	elif a<num:
		print("你猜小了兄弟")
	else:
		print("你真叼,兄弟")
		break
	i+=1
