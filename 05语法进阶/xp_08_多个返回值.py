def measure():
    """测量温度和湿度"""
    print("开始检测...")
    temp = 25
    wetness = 50
    print("检测结束...")
    # 元组可以包含多个数据，因此可以使用元组一次返回多个值
    # 如果函数返回的是元组，小括号可以省略
    # return (temp, wetness)
    return temp, wetness
result = measure()
print(result)
# 需要单独处理温度和湿度---不方便
print(result[0])
print(result[1])

# 如果函数返回的是元组，同时需要单独处理元组中的元素
# 可以定义多个变量，一次接收函数的返回结果
# 注意使用多个变量接收结果时，变量的个数应该与元组中元素的个数保持一致
gl_temp, gl_wetness = measure()
print(gl_temp)
print(gl_wetness)
