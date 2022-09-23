# -*- codeing = utf-8 -*-
# @Time : 2022/9/12 20:48
# @Author : wzc
# @File : testBs4.py
# @Software : PyCharm
import re

from bs4 import BeautifulSoup
file = open("./baidu.html","rb")
html = file.read().decode("utf-8")
bs = BeautifulSoup(html,"html.parser")

'''
#1. Tag  标签及其内容 ：拿到它所找到的第一个内容
print(bs.title)  #<title>百度一下，你就知道</title>
print(type(bs.title))  #<class 'bs4.element.Tag'>

#2. NavigableString  标签里的内容(字符串)
print(bs.title.string)  #百度一下，你就知道
print(type(bs.title.string))  #<class 'bs4.element.NavigableString'>

# 找到Tag的所有属性
print(bs.a.attrs) #{'href': 'http://news.baidu.com/', 'target': '_blank', 'class': ['mnav', 'c-font-normal', 'c-color-t']}

#3. BeautifulSoup代表整个html文档的内容
print(type(bs))  #<class 'bs4.BeautifulSoup'>
print(bs)

#4. Comment 是特殊的NavigableString，输出的内容不包含注释符号 <!--新闻-->
print(bs.a.string)
print(type(bs.a.string)) #<class 'bs4.element.Comment'>



#__________________________________________

#输出head标签中的所有元素(列表形式)
print(bs.head.contents) 
print(bs.head.contents[1])
'''

#文档搜索
#1.find_all()
# 字符串过滤 ： 查找与字符串完全匹配的标签
t_list = bs.find_all("img")
print(t_list)

#正则表达式搜索：匹配具有指定内容的标签
t_list = bs.find_all(re.compile("dy"))
print(t_list)
'''
#方法：传入一个函数，根据函数的要求来搜索（了解）
def name_isExists(tag):
    return tag.has_attr("http-equiv")
t_list=bs.find_all(name_isExists)
print(t_list)


#2. kwargs 参数
t_list = bs.find_all(id="head")
t_list = bs.find_all(href="http://news.baidu.com/")
t_list = bs.find_all(class_=True)
for i  in t_list:
    print(i)


#3.text参数   在标签里的字符串找出指定的内容 如果有则输出
t_list = bs.find_all(text= "贴吧")
t_list = bs.find_all(text= ["贴吧","地图","hao123"])
t_list = bs.find_all(text= re.compile("\d"))
for i  in t_list:
    print(i)

#4. limit参数
t_list = bs.find_all("a",limit=3)
for i  in t_list:
    print(i)

# css选择器
t_list = bs.select("title") #通过标签来查找
t_list = bs.select(".s-top-more-title") #通过类名来查找
t_list = bs.select("#s_tab")  #通过id来查找
t_list = bs.select("a[class='img-spacing']")  #通过属性查找
t_list = bs.select("head > title")  #通过子标签来查找
t_list = bs.select(".s-top-wrap ~ .s-top-left-new")  #通过兄弟结点查找
print(t_list[0].get_text())  #获取内容
'''