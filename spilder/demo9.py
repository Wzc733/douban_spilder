# -*- codeing = utf-8 -*-
# @Time : 2022/9/7 16:55
# @Author : wzc
# @File : demo9.py
# @Software : PyCharm

#捕获异常
try:
    print("------test-----1-----")
    f=open("123.txt","r")
    print("-------test-------2")
except (IOError,NameError) as result:  #获取错误描述
    print("成功捕获异常")
    print("错误描述：",result)

#捕获所有异常
try:
    print("------test-----1-----")
    f=open("123.txt","r")
    print("-------test-------2")
except Exception as result:  #获取错误描述
    print("成功捕获异常")
    print("错误描述：",result)