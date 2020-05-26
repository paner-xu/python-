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


ak47 = Gun("AK47")
ak47.add_bullet(50)
ak47.shoot()
xusanduo = Sodier("许三多")
xusanduo.gun = ak47
print(xusanduo.gun)


