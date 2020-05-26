# 定义布尔型变量has_tichet表示是否有车票
has_ticket = True
# 定义整型变量knife_length表示刀的长度
knife_length = 30
# 首先检查是否有车票，如果有，才允许进入安检
if has_ticket:
    print("车票检查通过，准备开始安检")
# 安检时需要检查刀的长度，判断是否超过20厘米
    if knife_length > 20:
        # 如果超过20厘米，提示刀的长度，不允许上车
        print("您携带的刀长%d, 不允许上车" % knife_length)
    # 如果没有超过20厘米，提示通过安检
    else:
        print("安检成功")
#如果没票，提示先购票
else:
    print("请先购买车票")



# 如果没有车票，提示不允许上车
