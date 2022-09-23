# -*- codeing = utf-8 -*-
# @Time : 2022/9/6 15:35
# @Author : wzc
# @File : demo3.py
# @Software : PyCharm

#有个冒号
for i in range(5) :
    print(i)

#从0开始到10结束(不包括10) 步进值为1
for i in range(0,10,1) :
    print(i)

for i in range(-10,-100,-40) :
    print(i)

name="shantou"
for x in name :
    print(x)

a=["aa","bb","cc"]
for i in range(len(a)) :
    print(a[i])

x=0
while x<5 :
    print("当前是：%d"%(x))
    x+=1

#1-100求和
i=1
sum=0
while i<=100 :
    sum+=i
    i+=1
print(sum)

sum=0
i=1
for i in range(101) :
     sum+=i
     i+=1
print(sum)

count=0
while count<5 :
    print(count,"小于5")
    count+=2
else:
    print(count,"大于等于5")

i=0
while i<10:
    i+=1
    print("-"*30)
    if i==5:
        break
    print(i)


