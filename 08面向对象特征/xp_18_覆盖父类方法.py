class Animal:
    def eat(self):
        print("吃---")
    def drink(self):
        print("喝---")
    def run(self):
        print("跑---")
    def sleep(self):
        print("睡---")
class Dog(Animal):
    # Dog类是Animal类的子类（派生类），
    # Animal类是Dog类的父类（基类），
    # Dog类从Animal类继承（派生）
    # def eat(self):
    #     print("吃")
    # def drink(self):
    #     print("喝")
    # def run(self):
    #     print("跑")
    # def sleep(self):
    #     print("睡")
    def dark(self):
        print("汪汪叫")
class XiaoTianQuan(Dog):
    def fly(self):
        print("我会飞")
    def dark(self):
        print("叫的跟神一样")
xtq = XiaoTianQuan()
xtq.dark()