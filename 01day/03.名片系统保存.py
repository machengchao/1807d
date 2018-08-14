'''
list = [{"name":"老王","age":16},{"name":"老马","age":20}]
f = open("data.data","w")
f.write(str(list))
f.close()
'''


list = []
f1 = open("data.data","r")
content = f1.read()
if len(content)!=0:
	list = eval(content)
	print(type(content))
	for i in list:
		for k,v in i.items():
			print(k,v)

	
	print(list)
f1.close()














