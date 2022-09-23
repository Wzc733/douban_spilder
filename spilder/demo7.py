# -*- codeing = utf-8 -*-
# @Time : 2022/9/7 15:48
# @Author : wzc
# @File : demo7.py
# @Software : PyCharm

#函数的定义
def printInfo():
    print("-"*30)
    print("今天吃饭用Python")
    print("-"*30)

#函数的调用
printInfo()

#带参数的函数
def add2Num(a,b):
    c=a+b
    print(c)

add2Num(11,22)

#带返回值的函数
def add2Num(a,b):
    return a+b
print(add2Num(11,22))


#返回多个值的函数
def divid(a,b):
    shang=a/b
    yushu=a%b
    return shang,yushu #多个返回值用逗号分隔

sh,yu=divid(5,2)  #需要多个值来保存返回内容
print(sh,yu)

#在函数中修改全局变量
a=100
def test1():
    global a   #使用global关键字声明在函数中使用全局变量
    print("修改前：%d"%a)
    a=200
    print("修改后：%d" % a)

def test2():
    print("a的值为：%d"%a)

test1()
test2()