class Women:
    def __init__(self, name):
        self.name = name
        # self.age = 18
        self.__age = 18
    # def secret(self):
    def __secret(self):
        print("[%s]的年龄是%d" % (self.name, self.__age))
xiaofang = Women("小芳")

# 私有属性，不能直接外部访问
# 可以在两条下划线前加上一条下划线和类名，
# 就能访问私有属性和方法
print(xiaofang._Women__age)

# 私有方法不能外部调用
xiaofang._Women__secret()