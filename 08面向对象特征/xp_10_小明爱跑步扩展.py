# 小明体重75.0公斤，小美体重40.0公斤
# 小明和小美都爱跑步
# 每次跑步会减肥0.5公斤
# 每次吃东西会增肥1公斤
class Person:
    def __init__(self, name, weigh):
        # self.属性=形参
        self.name = name
        self.weight = weigh
    def __str__(self):
        return "我的名字是%s, 我的体重是%.2f" % (self.name, self.weight)
    def run(self):
        print("%s爱跑步，跑步可以减肥" % self.name)
        self.weight -= 0.5
    def eat(self):
        print("%s是吃货，吃完再减肥" % self.name)
        self.weight += 1
xiaoming = Person("小明", 75.0)
xiaoming.eat()
xiaoming.run()
xiaomei = Person("小美", 40.0)
xiaomei.eat()
xiaomei.run()
print(xiaoming)
print(xiaomei)
# 同一个类创建的多个对象之间，属性互不干扰


