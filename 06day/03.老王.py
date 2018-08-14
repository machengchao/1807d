class showError(Exception):
	def __init__(self,name):
		self.name =name
class _input():
	def my_input(self):	
		name = input("请输入您的姓名:")
		try:
			if name == "老王":
				raise showError(name)
		except showError as ret:
			print("不能输入老王%s"%ret.name)

im = _input()
im.my_input()















