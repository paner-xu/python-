# 小明体重75.0公斤
# 小明每次跑步会减肥0.5公斤
# 小明每次吃东西会增肥1公斤
class Person:
    def __init__(self, name, weigh):
        # self.属性=形参
        self.name = name
        self.weight = weigh
    def __str__(self):
        return "我的名字是%s, 我的体重是%.02f" % (self.name, self.weight)
    def run(self):
        print("%s爱跑步，跑步可以减肥" % self.name)
        self.weight -= 0.5
    def eat(self):
        print("%s是吃货，吃完再减肥" % self.name)
        self.weight += 1
xiaoming = Person("小明", 75.0)
xiaoming.eat()
xiaoming.run()
print(xiaoming)
# 封装
# 1、将属性和方法封装到一个抽象的类中
# 2、在外界使用类创建对象，然后用对象调用方法
# 3、对象方法的细节都被封装在类的内部
# 在对象的方法内部，可以直接访问对象的属性


