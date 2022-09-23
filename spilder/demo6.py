# -*- codeing = utf-8 -*-
# @Time : 2022/9/7 11:04
# @Author : wzc
# @File : demo6.py
# @Software : PyCharm
'''
    元祖：元祖与list类似，不同之处在于元祖的元素不能修改，但可以包含可变对象
'''

tup1=()  #创建空的元祖  <class 'tuple'>
tup2=(50)  #<class 'int'>
print(type(tup2))
print(type(tup1))
tup2=(50,)  #<class 'tuple'>
print(type(tup2))

tup1=("a","b","c",11,55,"zz")
print(tup1[0])
print(tup1[-1]) #访问最后一个元素
print(tup1[1:5])  #左闭右开

#增
tup1=(1,33,45)
tup2=("ac","ww")
tup=tup1+tup2 #创建一个新的元祖 内容为tup1和tup2连接
print(tup)


#删 只能删除整个元素
tup1=(1,33,45)
print(tup1)
del tup1  #删除了整个元祖变量，不仅仅是删除元素
#print(tup1)  #name 'tup1' is not defined

#改 不能改
# tup3=(12,3,56)
# tup3[0]=100  #报错，不允许修改

#查

#字典的定义
info={"name":"吴彦祖","age":18}

print(info["name"])

#访问不存在 的键
# print(info["gender"])  #直接访问不存在的键会报错
print(info.get("gender")) #使用get方法没有找到对应的键默认返回null
print(info.get("sex","男")) #没有找到可以返回设置的默认值

#增
newID=input("请输入新的学号：")
info["id"]=newID
print(info["id"])

#删 del
print("删除前：%s"%info["name"])
del info["name"]
# del info
print("删除后 ：%s"%info.get("name"))

#clear 清空
info={"name":"吴彦祖","age":18}
print("清空前：%s"%info)
info.clear()
# del info
print("清空后 ：%s"%info)

#修改
info={"name":"吴彦祖","age":18}
info["age"]=20
print(info["age"])

#查
info={"name":"吴彦祖","age":18}
print(info.keys()) #拿到所有键
print(info.values()) #拿到所有的值
print(info.items()) #得到所有的项

#遍历所有的值
for key in info.keys():
    print(key)

#遍历所有的项
for key,value in info.items():
    print("key=%s,value=%s"%(key,value))

myList=["a","b","c","d"]
for i,x in enumerate(myList):  #使用枚举函数 同时拿到列表中的下标和元素内容
    print(i,x)

