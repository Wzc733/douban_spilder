# -*- codeing = utf-8 -*-
# @Time : 2022/9/6 13:26
# @Author : wzc
# @File : demo1.py
# @Software : PyCharm

#这是第一个python注释
print("Hello world!")
'''
    这是多行注释
'''
'''
a=10
print("这是变量：",a)

#格式化输出
age=19
print("我的年纪是：%d岁"%age)
print("我的名字是:%s,我的国籍是:%s"%("小张","中国"));

print("aaa","bbb","ccc") #aaa bbb ccc
print("www","baidu","com",sep=".") #www.baidu.com
print("hello",end="") #不换行
print("world",end="\t") #空一格
print("python",end="\n") #换行
print("end")
'''

'''
password= input("请输入密码：")
print("您刚刚输入的密码是：",password)
'''

#获得变量类型
a=10
print(type(a))

password= input("请输入密码：")
print(type(password))

#强制类型转换
a=int("123")
b=a+100
print(b)