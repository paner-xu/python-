class Cat:
    def __init__(self, new_name):
        self.name = new_name
        print("%s来了" % self.name)
    def __del__(self):
        print("%s去了" % self.name)
# tom是一个全局变量
tom = Cat("Tom")
print(tom.name)

del tom
print("*" * 50)

