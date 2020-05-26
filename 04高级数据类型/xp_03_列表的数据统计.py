name_list = ["张三", "李四", "王五","王小二","张三"]
# len（length，长度）可以统计列表中元素的总数
len_list = len(name_list)
print(len_list)
count = name_list.count("张三")
print(count)
# remove从列表中删除第一次出现的数据，如果数据不存在，程序会报错！
name_list.remove("张三")
print(name_list)