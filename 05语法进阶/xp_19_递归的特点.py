def sum_num(num):
    print(num)
    # 递归的出口很重要，否则会陷入死循环
    if num == 1:
        return
    # 自己调用自己
    sum_num(num - 1)
sum_num(3)