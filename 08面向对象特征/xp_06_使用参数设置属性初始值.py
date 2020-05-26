class Cat:
    def __init__(self, new_name):
        print("这是一个初始化方法")
        #使用self.属性名=属性的初始值
        # self.name = "Tom"
        self.name = new_name

    def eat(self):
        print("%s爱吃鱼" % self.name)
# 使用类名（）创建对象时，会自动执行__init__初始化方法
tom = Cat("Tom")
tom.eat()
lazy_cat = Cat("大懒猫")
lazy_cat.eat()