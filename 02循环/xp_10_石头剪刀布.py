#导入工具包
#注意：在导入工具包时，应将该工具包放在文件顶部，
# 这样可以方便下面的代码在任何时候都能使用工具包
import random
# 1.从控制台输入要出的拳 石头（1）/剪刀（2）/布（3）
player = int(input("请输入要出的拳 石头（1）/剪刀（2）/布（3）"))

# 2.电脑随机出拳——先假设电脑只会出石头，完成整体代码功能
computer = random.randint(1, 3)

# 3.比较胜负
print("玩家选择的拳头 %d - 电脑出的拳头 %d" %(player, computer))
#英文状态下输入
if ((player == 1 and  computer == 2)
        or (player == 2 and computer == 3)
        or (player == 3 and computer == 1)):
    print("欧耶，电脑弱爆了！")
elif player == computer:
    print("心有灵犀，再来一局")
else:
    print("不服气，我们决战到天明！")

