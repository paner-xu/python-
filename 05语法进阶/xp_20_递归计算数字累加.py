# 定义一个函数
# 能够接收一个num的整数参数
# 计算1+2+...+num的结果
def sum_numbers(num):
    # 1.出口
    if num == 1:
        return num
    # 2.数字的累加 num+(1...num - 1)
    # 假设sum_numbers能正确处理1...num-1
    temp = sum_numbers(num - 1)
    # 两个数字的相加
    return num + temp
result = sum_numbers(100)
print(result)