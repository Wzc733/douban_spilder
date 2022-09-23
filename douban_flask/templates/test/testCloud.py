# -*- codeing = utf-8 -*-
# @Time : 2022/9/22 10:30
# @Author : wzc
# @File : testCloud.py
# @Software : PyCharm

import jieba   #分词
from wordcloud import WordCloud    #词云
from PIL import Image    #图片处理
import numpy as np    #矩阵运算
import sqlite3    #数据库
from matplotlib import pyplot as plt
import matplotlib
matplotlib.use('TkAgg')

#准备所需的文字
con = sqlite3.connect('../../movieTop250.db')
cur = con.cursor()
sql = "select instroduction from movieTop250"
data = cur.execute(sql)
text = ""
for item in data:
    text = text + item[0]
cur.close()
con.close()

#进行分词
cut = jieba.cut(text)
string = ' '.join(cut)
print(string)

img = Image.open('cloud.jpg')
img_array = np.array(img)   #将图片转化为数组
wc = WordCloud(
    background_color='white',
    mask=img_array,
    font_path='STXIHEI.TTF'
)
wc.generate_from_text(string)

#绘制图片
plt.figure(1)
plt.imshow(wc)
plt.axis('off')  #是否显示坐标轴


# plt.show()
plt.savefig(r'../../static/assets/img/cloud.jpg',dpi=800)