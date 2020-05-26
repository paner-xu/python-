num_str = '0123456789'
# 截取从2-5位置的字符串
num_str2 = num_str[2:6]
# 截取从2-末尾的字符串
num_str2 = num_str[2:]
# 截取从开始-5位置的字符串
num_str2 = num_str[:6]
# 截取完整的字符串
num_str2 = num_str[::]
# 从开始位置，每隔一个字符截取字符串
num_str2 = num_str[::2]
# 从索引1开始，每隔一个取一个
num_str2 = num_str[1::2]
# 截取从2到末尾-1的字符串
num_str2 = num_str[2:-1]
# 截取字符串末尾两个字符
num_str2 = num_str[-2:]
# 字符串的逆序（面试题）
num_str2 = num_str[-1::-1]
num_str2 = num_str[::-1]
print(num_str2)


