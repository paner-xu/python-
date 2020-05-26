def demo1():
    # 定义一个内部变量
    # 1>出生：下方代码被执行时，才会被创建
    # 2>死亡：代码执行完后，生命周期结束
    num = 10
    print("在demo1函数内部的变量是 %d" % num)
# 在函数内部定义的变量不能在其他位置使用
# print("demo1内的变量%d" % num)
def demo2():
    # 定义一个相同的局部变量
    num = 99
    print("demo2 ==> %d" % num)
demo1()
demo2()