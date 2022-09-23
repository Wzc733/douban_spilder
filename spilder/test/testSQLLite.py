# -*- codeing = utf-8 -*-
# @Time : 2022/9/19 21:19
# @Author : wzc
# @File : testSQLLite.py
# @Software : PyCharm

import  sqlite3

#1.建表
#
# conn = sqlite3.connect("test.db")
# print("打开了数据库")
# c = conn.cursor()  #获取游标
# sql = '''
#     create table company
#         (id int primary key not null,
#         name text not null,
#         age int not null,
#         address char(50),
#         salary real);
#
# '''
# c.execute(sql)  #执行sql
# conn.commit()    #提交数据库操作
# conn.close()       #关闭数据库连接
#
# print("成功建表")


#2.查询数据
conn = sqlite3.connect("test.db")
print("打开了数据库")
c = conn.cursor()  #获取游标
sql = '''
    select id,name,address,salary from company;
'''
cursor = c.execute(sql)  #执行sql

for row in cursor:
    print("id =",row[0])
    print("name =", row[1])
    print("address =", row[2])
    print("salary =", row[3])


conn.close()       #关闭数据库连接