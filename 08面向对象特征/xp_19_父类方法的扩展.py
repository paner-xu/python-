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
    # 1、根据子类特有的需求编写代码
    def dark(self):
        print("叫的跟神一样")
    # 使用super（）.调用父类中封装的方法
        super().dark()
    # 增加其他子类的代码
        print("@#$$%^&&*&*")
xtq = XiaoTianQuan()
xtq.dark()