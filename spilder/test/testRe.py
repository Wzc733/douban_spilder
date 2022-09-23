# -*- codeing = utf-8 -*-
# @Time : 2022/9/13 21:48
# @Author : wzc
# @File : testRe.py
# @Software : PyCharm

#正则表达式
import  re

#创建模式对象
pat = re.compile("AA")  #此处的AA，是正则表达式，用来校验其它字符串
result = pat.search("AAb")  #search()中的字符串是被校验的内容
print(result)  #<re.Match object; span=(0, 2), match='AA'>
result = pat.search("AAbCCDDAAAAEE") #结果一样 。找到第一个符合模板的字符串
print(result)

#第一个参数为模板 同上效果一样
m = re.search("asd","ASDAasd")
print(m)

print(re.findall("a","ASDasiIHIannia"))  #['a', 'a', 'a']
print(re.findall("[A-Z]","ASDasiIHIannia"))  #['A', 'S', 'D', 'I', 'H', 'I']
#+前一个字符出现一次或多次(在此是一个或多个大写字母则符合)
print(re.findall("[A-Z]+","ASDasiIHIannia")) #['ASD', 'IHI']

#sub
print(re.sub("a","A","asdiouhioa"))  #找到a则用A替换

#建议在正则表达式中，被比较的字符前面加上r，不用担心转移字符问题
a=r"\asd\'\-"
print(a)