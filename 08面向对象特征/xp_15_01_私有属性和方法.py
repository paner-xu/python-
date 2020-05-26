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
# print(xiaofang.__age)

# 私有方法不能外部调用
# xiaofang.__secret()