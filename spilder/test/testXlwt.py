# -*- codeing = utf-8 -*-
# @Time : 2022/9/19 17:04
# @Author : wzc
# @File : testXlwt.py
# @Software : PyCharm

import  xlwt

# wookbook = xlwt.Workbook(encoding="utf-8")  #创建wookbook对象
# worksheet = wookbook.add_sheet('sheet1')  #创建工作表
# worksheet.write(0,0,'hello')  #行，列，内容
# wookbook.save('student.xls')   #保存数据表

wookbook = xlwt.Workbook(encoding="utf-8")  #创建wookbook对象
worksheet = wookbook.add_sheet('sheet1')  #创建工作表
for i in range(0,9):
    for j in range(0,i+1):
        worksheet.write(i,j,"%d * %d = %d "%(i+1,j+1,(i+1)*(j+1)))
wookbook.save('student.xls')