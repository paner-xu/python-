class Gun:
    def __init__(self, model):
        self.model = model
        self.bullet_count = 0
    def add_bullet(self, count):
        self.bullet_count += count
    def shoot(self):
        # 1、判断子弹数量
        if self.bullet_count <= 0:
            print("[%s]没有子弹了..." % self.model)
            return

       # 2、发射子弹
        self.bullet_count -= 1
        # 3、发射信号
        print("%s突突突...[%d]" % (self.model, self.bullet_count))
class Sodier:
    def __init__(self, name):
        self.name = name
        self.gun = None
    def fire(self):
        # 1、判断是否有抢
        # if self.gun == None:
        # ==用于判断引用变量的值是否相等
        # is用于判断两个变量引用的对象是否是同一个
        if self.gun is None:
            print("[%s]还没有枪" % self.name)
            return
        # 2、装填子弹
        self.gun.add_bullet(50)
        # 3、高喊口号
        print("冲鸭...[%s]" % self.name)
        # 4、发射子弹
        self.gun.shoot()


ak47 = Gun("AK47")
xusanduo = Sodier("许三多")
xusanduo.gun = ak47
xusanduo.fire()



