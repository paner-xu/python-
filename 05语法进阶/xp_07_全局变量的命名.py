# 为了避免全局变量和局部变量出现混淆，
# 有些公司要求在定义全局变量时，在变量前面加上g_或gl_
gl_num = 10
gl_title = "河马程序员"
gl_name = "小明明"
def demo():
    num = 99
    print("%d" % num)
    print("%s" % gl_title)
    print("%s" % gl_name)
# title = "河马程序员"
demo()
# name = "小明明"