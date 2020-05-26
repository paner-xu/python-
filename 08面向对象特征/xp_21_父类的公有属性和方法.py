class A:
    def __init__(self):
        self.num1 = 100
        self.__num2 = 200
    def __test(self):
        print("私有方法%d %d" % (self.num1, self.__num2))
    def test(self):
        # 1、访问私有属性
        print("公有方法%d %d" % (self.num1, self.__num2))
        # 2、调用公私有方法
        self.__test()
class B(A):
    def demo(self):
        # 1、子类的对象方法中不能访问父类的私有属性
        # print("访问父类的私有属性%d %d" % (self.num1, self.__num2))
        # 2、子类的对象方法中不能调用父类的私有方法
        # self.__test()
        self.test()
        pass
b = B()
b.demo()
print(b)
# 1、在外部不能访问父类的私有属性/私有方法
# print(b.__num2)
# b.__test()

