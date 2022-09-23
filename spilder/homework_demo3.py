# -*- codeing = utf-8 -*-
# @Time : 2022/9/6 17:05
# @Author : wzc
# @Software : PyCharm

i_1=1
while i_1<=9 :
    i_2 = 1
    while i_2 <= i_1:
        print("%d*%d=%d" % (i_1, i_2, i_1 * i_2),end="\t")
        i_2+=1
    print("\n")
    i_1+=1


for i in range(1,10,1):
    for i1 in range(i) :
        print("%d*%d=%d" % (i, i1+1, i * i1+1),end="\t")
    print("\n")
