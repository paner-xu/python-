price = int(input("苹果的单价:"))   #不能转化成浮点型
weight = int(input("苹果的重量："))
money = price * weight
print("苹果的单价:%d,苹果的重量：%d,需要支付：%d" % (price, weight, money))