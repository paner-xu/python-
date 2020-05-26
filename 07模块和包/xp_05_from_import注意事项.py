# 当从两个不同的模块中导入两个同名的函数时，
# 后倒入的模块中的函数会覆盖掉先导入的函数
from xp_01_测试模块1 import say_hello
from xp_02_测试模块2 import say_hello
# 可以用as修改别名
from xp_01_测试模块1 import say_hello as Module_say_hello
say_hello()
Module_say_hello()