# -*- codeing = utf-8 -*-
# @Time : 2022/9/9 0:14
# @Author : wzc
# @File : spider.py
# @Software : PyCharm

from bs4 import BeautifulSoup    #网页解析，获取数据
import re     #通过正则表达式进行文字匹配
import urllib.request,urllib.error  #制定url，获取网页数据
import xlwt  #进行excel操作
import sqlite3 #进行SQLite数据库操作



def main():
    baseUrl="https://movie.douban.com/top250?start="
    #1.爬取网页
    dataList=getData(baseUrl)

    #3.保存数据
    savePath = "./豆瓣电影TOP250.xls"
    dbPath = "movieTop250.db"
    saveData(dataList,savePath)
    saveData2DB(dataList,dbPath)

#.*代表字符有n个  ?表示符合的内容出现0次或1次
#影片详情链接规则
findLink=re.compile(r'<a href="(.*?)">')   #创建正则表达式对象模板
# 影片图片的链接规则
findImgSrc = re.compile(r'<img.*src="(.*?)"',re.S)  #.不包括换行符 re.S让换行符也包括在字符中
#影片的片名
findTitle = re.compile(r'<span class="title">(.*)</span>')
#影片的评分
findRating = re.compile(r'<span class="rating_num" property="v:average">(.*?)</span>')
#影片的评价人数
findJudge = re.compile(r'<span>(\d*)人评价</span>')   #\d代表数字 *代表n个
#找到介绍
findInq = re.compile(r'<span class="inq">(.*)</span>')
#找到影片的相关内容
findBd = re.compile(r'<p class="">(.*?)</p>',re.S)


# 爬取网页
def getData(baseUrl):
    dataList=[]
    for i in range(0,10):
        url = baseUrl + str(i*25)
        html = askURL(url)
        # 2.解析数据
        soup = BeautifulSoup(html,"html.parser")
            #查找 div标签 + class="item"
        for item in soup.find_all('div',class_="item"):
            #print(item)  #测试，查看item的全部信息
            data=[]
            item = str(item)

            #提取的内容
            link = re.findall(findLink,item)[0]
            data.append(link)

            imgSrc = re.findall(findImgSrc,item)[0]
            data.append(imgSrc)

            titles = re.findall(findTitle,item)  #片名可能只有一个中文名，没有外国名
            if(len(titles) == 2) :
                ctitle = titles[0]
                data.append(ctitle)
                otitle = titles[1].replace("/","")
                data.append(otitle)
            else:
                data.append(titles[0])
                data.append('  ') #如果只有中文名，那么英文名的那一列要留空

            rating = re.findall(findRating,item)[0]
            data.append(rating)

            judgeNum = re.findall(findJudge,item)[0]
            data.append(judgeNum)

            inq = re.findall(findInq,item)
            if inq:
                data.append(inq[0].replace("。",""))
            else:
                data.append('   ')

            bd = re.findall(findBd,item)[0]
            bd = re.sub('<br(\s+)?/>(/s+)?',"",bd)
            bd = re.sub('/'," ",bd)
            bd = re.sub(' *', "", bd)
            bd = re.sub('(\xa0)*', "", bd)
            data.append(bd.strip())  #去掉前后空格

            dataList.append(data)  #把处理好的一部电影信息放到dataList
    return dataList

# 得到指定的一個url的網頁内容
def askURL(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 11; Pixel 5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.91 Mobile Safari/537.36 Edg/105.0.0.0"
    }
    request = urllib.request.Request(url=url,headers=headers)
    html=""
    try:
        response = urllib.request.urlopen(request)
        html = response.read().decode("utf-8")
        # print(html)
    except urllib.error.URLError as e:
        if hasattr(e,"code"):
            print(e.code)
        if hasattr(e,"reason"):
            print(e.reason)

    return  html


# 保存数据到表格
def saveData(dataList,savePath):
    book = xlwt.Workbook(encoding="utf-8")  # 创建wookbook对象
    sheet = book.add_sheet('豆瓣电影Top250')  # 创建工作表
    col = ("电影详细链接","图片链接","影片中文名","影片英文名","评分","评价数","概况","相关信息")
    for i in range(len(col)):
        sheet.write(0,i,col[i]) #列明
    for i in range(0,250):
        print("第%d条"%(i+1))
        data = dataList[i] #取出一条电影的信息
        for j in range(len(data)):
            sheet.write(i+1,j,data[j])
    book.save(savePath)

# 保存数据到数据库
def saveData2DB(dataList, dbPath):
    #创建表
    init_db(dbPath)
    conn = sqlite3.connect(dbPath)
    c = conn.cursor()  #获取游标

    for data in dataList:
        for index in range(len(data)):
            data[index] = '"'+data[index]+'"'

        sql = '''
                    insert into movieTop250(info_link,pic_link,cname,ename,score,rated,instroduction,info)
                    values(%s);''' % ",".join(data)  #将列表元素通过,连接
        print(sql)

        c.execute(sql)  #执行sql
        conn.commit()    #提交数据库操作

    c.close()
    conn.close()       #关闭数据库连接


def init_db(dbpath):
    conn = sqlite3.connect(dbpath)
    print("打开了数据库")
    c = conn.cursor()  # 获取游标
    sql = '''
            create table movieTop250(
                id integer primary key autoincrement,
                info_link text,
                pic_link text,
                cname text,
                ename text,
                score numeric,
                rated numeric,
                instroduction text,
                info text
            );
    '''
    c.execute(sql)  # 执行sql
    conn.commit()  # 提交数据库操作
    conn.close()  # 关闭数据库连接
    print("创建表成功")

if __name__ == "__main__":
    main()
    print("爬取完毕!")