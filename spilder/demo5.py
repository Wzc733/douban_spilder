# -*- codeing = utf-8 -*-
# @Time : 2022/9/6 22:39
# @Author : wzc
# @File : demo5.py
# @Software : PyCharm

nameList=[]  #定义一个空列表
nameList=["小张","小王","小李"]
print(nameList[0])
nameList=[1,"测试"]
print(nameList[1]) #列表中可以存放多种类型数据（并不会转换）

for i in nameList :
    print(i)
#实现比for循环麻烦，但是可以通过下标进行进一步处理
length=len(nameList)
i=0
while i<length:
    print(nameList[i])
    i+=1

'''
#增： [append]
print("------增加前,名单列表的数据-----")
for name in nameList:
    print(name)

nametemp=input("请输入新增加：")
nameList.append(nametemp)

print("------增加后,名单列表的数据-----")
for name in nameList:
    print(name)
'''

#增： [extend]
a=[1,2]
b=[3,4]
a.append(b)  #将列表当做一个元素
print(a)  #[1, 2, [3, 4]]
a.extend(b)   #将列表中所有元素逐一添加
print(a)  #[1, 2, [3, 4], 3, 4]

#增： [insert]
a=[0,1,2]
a.insert(1,3) #参数一表示下标，参数二表示插入的元素
print(a)

#删： [del]
movieName=["指环王","指环王","加勒比海盗","第一滴血"]
print("------删除前,电影列表的数据-----")
for name in movieName:
    print(name)

del movieName[2] #指定位置删除一个元素
movieName.pop()  #弹出最后一个元素
movieName.remove("指环王")  #直接删除指定内容的元素(找到的第一个符合条件的元素)

print("------删除后,名电影列表的数据-----")
for name in movieName:
    print(name)

#改 : []
print("------增加前,名单列表的数据-----")
for name in nameList:
    print(name)

nameList[1]="小五"  #指定下标修改元素

print("------增加后,名单列表的数据-----")
for name in nameList:
    print(name)
'''
#查 : [in,not in]
findName=input("请输入你要查找的学生姓名：")
if findName in nameList:
    print("在学员名单种找到了相同的名字")
else:
    print("没有找到")

a=["a","b","c","a","b"]
print(a.index("a",1,4))  #可以查找指定下标范围的元素，并返回找到对应元素的下标
print(a.index("a",1,3))  #范围是左闭右开 找不到会报错
'''

a=["a","b","c","a","b"]
print(a.count("a"))  #统计元素出现的次数

a=[1,4,2,3]
print(a)
a.reverse()  #将列表所有元素反转（自身）
print(a)

a.sort()  #升序排序
a.sort(reverse=True) #降序排序
print(a)

schoolNames=[[],[],[]]
schoolNames=[["北京大学","深圳大学"],["清华大学","山东大学"],["哈哈大学"]]
print(schoolNames[0][0])

import random
offices=[[],[],[]]
names=["a","b","c","d","e","f","g","h"]
for name in names:
    index=random.randint(0,2) #左闭右闭
    offices[index].append(name)
print(offices)

i=1
for office in offices:
    print("办公室%d的人数：%d"%(i,len(office)))
    i+=1
    for name in office:
        print("%s"%name,end="\t")
    print("\n")
    print("-" * 20)
