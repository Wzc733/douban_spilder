# -*- codeing = utf-8 -*-
# @Time : 2022/9/7 16:18
# @Author : wzc
# @File : demo8.py
# @Software : PyCharm

# f.open("test.txt")  #默认只读模式
# f=open("test.txt","w")  #打开文件，W模式（写模式），文件不存在则自动创建
# f.write("hello , my god")  #将字符串写入文件中
# f.close()  #关闭文件

#读取指定数量的字符，开始时定位在头部，会随着执行次数定位往后移动
f=open("test.txt")
content=f.read(5)
print(content)  #hello
content=f.read(5)
print(content)  # , my
f.close()

f=open("test.txt")
content=f.readlines() #一次性读取全部字符串，每行作为数组的一个字符串元素
print(content)

for i,temp in enumerate(content):
    print("%d:%s"%(i,temp))

f.close()

import os  #包含非常多的文件操作功能
os.rename("test.txt","text.txt")