# -*- codeing = utf-8 -*-
# @Time : 2022/9/9 0:32
# @Author : wzc
# @File : testUrllib.py
# @Software : PyCharm

import urllib.request

#获取一个get请求
# response=urllib.request.urlopen("http://www.baidu.com")
# print(response.read().decode("utf-8"))  #对获取到的网页源码进行utf-8解码

# 获取一个post请求
#

#爬取豆瓣的信息被發現，因爲userAagent直接告訴豆瓣我們是爬蟲，我們需要僞裝一下
url = "https://www.douban.com"
headers = {
"User-Agent":  "Mozilla/5.0 (Linux; Android 11; Pixel 5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.91 Mobile Safari/537.36 Edg/105.0.0.0"
}
req = urllib.request.Request(url=url,headers=headers)
response = urllib.request.urlopen(req)
print(response.read().decode("utf-8"))