name = "小明"
print("我的名字叫%s" % name)
student_no = 82
print("我的学号是%06d" % student_no)
price = 7.3
weight = 8.4
money = price * weight
print('苹果的单价为%.2f元,苹果的重量为%.1f斤,需支付%.2f元' % (price, weight, money))
#注意括号的完整性
scale = 0.25
print("数据比例为%.02f%%" % (scale * 100) )
scale = 0.25 * 100
print("数据比例为%.02f%%" % scale)