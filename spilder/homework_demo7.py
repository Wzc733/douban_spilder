# -*- codeing = utf-8 -*-
# @Time : 2022/9/7 15:57
# @Author : wzc
# @File : homework_demo7.py
# @Software : PyCharm

def printLine(num):
    print("-"*num)

printLine(10)

def sumThreeNum(a,b,c):
    return a+b+c

result=sumThreeNum(1,2,3)
print(result)

def avage(a,b,c):
    return sumThreeNum(a,b,c)/3
print(avage(1,2,3))