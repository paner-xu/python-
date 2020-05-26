# del关键字本质上是将一个变量从内存中删除
# 如果使用del关键字将变量从内存中删除，
# 后续代码就不能使用这个变量了
name_list = ["张三", "李四", "王五"]
del name_list[0]
print(name_list)