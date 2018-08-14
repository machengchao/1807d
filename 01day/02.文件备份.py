name = input("请输入备注文件(加后缀):")
f = open(name,"r")
content = f.read()

f1 = open("密码备份","w")
f1.write(content)
f.close()
f1.close()


