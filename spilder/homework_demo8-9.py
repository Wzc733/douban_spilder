# -*- codeing = utf-8 -*-
# @Time : 2022/9/7 19:05
# @Author : wzc
# @File : homework_demo8-9.py
# @Software : PyCharm

def writeFile():
    try:
        f=open("gushi.txt","w",encoding="utf-8")
        try:
            f.write("今朝有酒今朝醉")
        except Exception as exceptionResl:
            print("捕获到了异常：", exceptionResl)
        finally:
            f.close()
    except Exception as exceptionResl:
        print("捕获到了异常：",exceptionResl)

def readFile():
    try:
        f1=open("gushi.txt",encoding="utf-8")
        f2=open("copt.txt","w",encoding="utf-8")
        try:
            contents=f1.readlines()
            for content in contents:
               f2.write(content)
            print("复制完毕")
        except Exception as exceptionResl:
            print("捕获到了异常：", exceptionResl)
        finally:
            f1.close()
            f2.close()
    except Exception as exceptionResl:
        print("捕获到了异常：", exceptionResl)

readFile()