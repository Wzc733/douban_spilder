# -*- codeing = utf-8 -*-
# @Time : 2022/9/6 13:56
# @Author : wzc
# @File : demo2.py
# @Software : PyCharm

#0和False表示为假 其它为真
if True:
    print("True")
else:
    print("False")
print("end")

score=77
if score>=90 :
    print("等级为A")
elif score>=60 and score<=90 :
    print("及格")
else:
    print("不及格")

import random  #引入随机库
x= random.randint(0,2) #随机生成0到2之间的随机整数
print(x)
