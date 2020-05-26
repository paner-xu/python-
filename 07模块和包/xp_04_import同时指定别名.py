# 别名的命名规则要满足大驼峰命名法
import xp_01_测试模块1 as DogModule
import xp_02_测试模块2 as CatModule
DogModule.say_hello()
CatModule.say_hello()

dog = DogModule.Dog()
print(dog)
cat = CatModule.Cat()
print(cat)