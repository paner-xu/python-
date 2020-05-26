# 模块可以导入全局变量、函数、类
def say_hello():
    print("你好，你好，我是say hello")
# 如果直接执行模块， __main__
# __name__属性可以做到，测试模块的代码只有在测试情况下被执行，
# 而在被导入时不会被执行！
if __name__ == "__main__":
    print(__name__)
    print("我是小明")
    say_hello()