# -*- codeing = utf-8 -*-
# @Time : 2022/9/6 15:20
# @Author : wzc
# @Software : PyCharm

shuru=input("请输入石头剪刀布：")
if shuru!="石头" or "剪刀" or "布" :
    print("请正确输入")
elif shuru=="石头" :
    shuru=1
    print("你的输入为石头")
elif shuru=="剪刀" :
    shuru=0
    print("你的输入为剪刀")
else:
    shuru=2
    print("你的输入为布")

import random
x=random.randint(0,2)
print("随机生成的数字为：%d"%x)
if x==shuru :
    print("打平")
elif x==1 and shuru==2 or x==0 and shuru==1 or x==2 and shuru==0:
    print("哈哈，你输了")
elif x==1 and shuru==0 or x==0 and shuru==2 or x==2 and shuru==1:
    print("你赢了")