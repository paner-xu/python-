class A:
    def test(self):
        print("A---test方法")
    def demo(self):
        print("A---demo方法")
class B:
    def test(self):
        print("B---test方法")
    def demo(self):
        print("B---demo方法")
# 子类对父类的继承顺序对输出结果产生影响
class C(B, A):
    pass
c = C()
c.test()
c.demo()

# 查看C类调用父类方法的顺序
print(C.__mro__)