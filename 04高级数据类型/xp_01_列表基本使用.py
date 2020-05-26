name_list = ["zhangsan", "lisi", "wangwu"]
# 1.取值和取索引
print(name_list[0])

# 知道数据内容，想知道数据在列表中的位置
# 使用index需要注意，如果传递的数据不在列表内，程序会报错！
print(name_list.index("zhangsan"))
# 2.修改
name_list[1] = "李四"
# list assignment index out of range
# 列表指定的索引超出范围，程序会报错！
# name_list[3] = "李四"

# 3.增加
# append用于在列表末尾追加数据
name_list.append("王小二")
temp_list = ["孙悟空", "猪二哥", "沙师弟"]
# extend可以将其他列表中的完整内容，追加到当前列表的末尾
name_list.extend(temp_list)
# insert可以在指定索引位置插入数据
name_list.insert(1, "小美眉")
# 4.删除
# remove可以将列表中的指定元素删除
name_list.remove("猪二哥")
# pop方法可以删除指定位置的索引
name_list.pop(0)
# pop方法默认可以删除列表最后一个元素
name_list.pop()
# clear可以将列表元素清空
name_list.clear()
print(name_list)