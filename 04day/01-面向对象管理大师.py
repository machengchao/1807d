import pickle 
list = []

class cai():
	def __init__(self):
		print("1:添加学生信息")
		print("2:查找学生信息")
		print("3:修改学生信息")
		print("4:删除学生信息")
		print("5:退出学生信息系统")

	def finds(self):
		while True:
			num = int(input("请您选择序号:")
			if num == "1":
				student().add()
				f = open("资料库.txt","wb+")
				pickle._dump(list,f)
				f.close()
			
class student():
	def __init__(self):
		name = input("请输入姓名:")
		sex = input("请输入性别:")
		phone = input("请输入您的手机号:")
		
	def add(self):
		list_ad=[self.name,self.sex,self.phone]
		list.append(list_ad)

	def aa(self):
		name = input("请您输入名字:")
		flag= False
		f=open()






















































