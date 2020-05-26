class Cat:
    def __init__(self):
        print("这是一个初始化方法")
        #使用self.属性名=属性的初始值
        self.name = "Tom"
    def eat(self):
        print("%s爱吃鱼" % self.name)
# 使用类名（）创建对象时，会自动执行__init__初始化方法
tom = Cat()
tom.eat()
