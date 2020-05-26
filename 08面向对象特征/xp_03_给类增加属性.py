class Cat:
    def eat(self):
        # 哪一个对象调用的方法，self就是哪一个对象的引用
        print("%s爱吃鱼" % self.name)
    def drink(self):
        print("%s爱喝水" % self.name)
tom = Cat()
tom.name = "Tom"
tom.eat()
tom.drink()

lazy_cat = Cat()
lazy_cat.name = "大懒猫"
lazy_cat.eat()
lazy_cat.drink()
