# -*- codeing = utf-8 -*-
# @Time : 2022/9/7 10:30
# @Author : wzc
# @File : homework_demo5.py
# @Software : PyCharm

products=[["iphone",6888],["MacPro",14800],["小米6",2499],["Coffee",31],["Book",60]]
print("-"*6+"   商品列表   "+"-"*6)

i=0
for product in products:
        product.insert(0,i)
        print("%d %s %d"%(product[0],product[1],product[2]))
        i+=1

sum=0
shopList=[]
productId=input("请输入要购买的商品编号:")
while productId!="q":
    for product in products:
        if product[0]==(int(productId)):
            shopList.append(product[1])
            sum+=product[2]
            print("添加成功")
            break
    productId = input("请继续输入要购买的商品编号:")
for shop in shopList:
    print(shop)
print(sum)