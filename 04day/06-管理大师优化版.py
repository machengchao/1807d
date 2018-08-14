#coding=utf-8
import pickle
list = []
class cai():
    def __init__(self):
        print("\t1.添加学员资料",end = '\t\t')
        print("2.查看学员资料")
        print("")
        print("\t3.修改学员资料",end = '\t\t')
        print("4.删除学员资料")
        print("")
        print("\t5.打印学员名单",end = '\t\t')
        print("6.退出系统")

    def fun(self):
        while True:

            num = input("请选择功能")
            if num == '1':
                student().add()
                f = open("资料库.txt", "wb+")
                pickle._dump(list, f)
                f.close()

            elif num == "2":
                aa().cat()
            elif num == '3':
                aa().change()
            elif num == '4':
                aa().delete()
            elif num == '5':
                aa().all_print()
            elif num == '6':
                break
            else:
                print("输入有误，请重新输入")
class student():

    def __init__(self):
        self.name = input('输入名字')
        self.sex = input('输入性别')
        self.phone = input('手机号')

    def add(self):

        list_add = [self.name,self.sex,self.phone]
        #print(list_add)
        list.append(list_add)
        #print(list)
class aa():
    def cat(self):
        cat_name = input("输入名字")
        flag = False
        f = open("资料库.txt","rb+")
        b = pickle.load(f)
        print(b)
        for i in b:
            if i[0] == cat_name:
                print("姓名：%s\n性别：%s\n手机号：%s"%(i[0],i[1],i[2]))
                flag = True
        if flag == False:
            print("查无此人")
        f.close()
    def change(self):
        change_name = input("输入名字")
        flag = False
        f = open("资料库.txt", "rb+")
        b = pickle.load(f)
        for i in b:
            if i[0] == change_name:
                i[0] = input("输入修改后的名字")
                i[1] = input("输入性别")
                i[2] = input("输入手机号")
                flag = True
        if flag == False:
            print("查无此人")
        f.close()
    def all_print(self):
        f = open("资料库.txt", "rb+")
        b = pickle.load(f)
        print("姓名\t性别\t手机号\t")
        for i in b:
            print(" %s\t\t %s\t\t %s\t\t"%(i[0],i[1],i[2]))
        f.close()
    def delete(self):
        def_name = input("输入名字")
        flag = False
        f = open("资料库.txt", "rb+")
        b = pickle.load(f)
        for position,i in enumerate(b):
            if i[0] == def_name:
                b.pop(position)
                print(b)
                flag = True
        if flag == False:
                print("查无此人")
        f.close()


a = cai()
a.fun()
