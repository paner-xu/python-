# 注意：在开发成程序时，应该把所有全局变量定义在函数的上方
# 这样就可以保证所有的函数都能正常访问到每一个全局变量
num = 10
title = "河马程序员"
name = "小明明"
def demo():
    print("%d" % num)
    print("%s" % title)
    print("%s" % name)
# title = "河马程序员"
demo()
# name = "小明明"