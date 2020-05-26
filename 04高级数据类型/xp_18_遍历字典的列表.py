students = [
    {"name":"小美"},
    {"name":"阿土"}
]
# 在学员列表中找到指定的姓名
find_name = "张三"
for stu_dict in students:
    print(stu_dict)
    if stu_dict["name"]==find_name:
        print("找到了 %s" % find_name)
        # 如果已经找到，应该退出循环，而不用遍历后续的元素
        break
else:
    print("没有找到 %s" % find_name)
print("循环结束")
