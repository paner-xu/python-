# 假设一下内容是从网上抓取
# 要求：将字符串中的空白字符去除
# 再使用“”作为分隔符，拼成一个整齐的字符串
poem_str = "\t\n登鹳雀楼,  王焕之,  白日依山尽\t\n,  黄河入海流,欲穷千里目, 更上一层楼"
print(poem_str)
# 拆分字符串
poem_list = poem_str.split()
print(poem_list)

# 合并字符串
result = "".join(poem_list)
print(result)