# 后导入的模块的同名函数会覆盖先导入的函数，
# 容易产生混淆，不推荐使用
from xp_01_测试模块1 import *
from xp_02_测试模块2 import *
print(title)
say_hello()
dog = Dog()
print(dog)