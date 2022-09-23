# -*- codeing = utf-8 -*-
# @Time : 2022/9/6 21:50
# @Author : wzc
# @File : demo4.py
# @Software : PyCharm

word='字符串'
sentence="这是一个句子"
paragraph="""
    这是一个段落
    可以由多行组成
"""

print(word)
print(sentence)
print(paragraph)

str="chengdu"
print(str)
print(str[0:6]) # chengd [起始位置：结束位置：步进值]
print(str[0:6:2]) #ceg
print(str[3:])  #起始位置开始全部的字符
print(str[:3])
print("你好,"+str) #你好,chengdu
print(str*3)

print(r"hello\nshantou")  #无视转义字符 原始字符串都会保存下来
