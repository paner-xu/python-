xiaoming_dict = {"name": "小明"}
# 1.取值
# 在取值时，如果指定的key不存在，程序会报错！
# print(xiaoming_dict["name123"])
print(xiaoming_dict["name"])
# 2.增加/修改
# 如果key不存在，会增加键值对
# 如果key存在，会修改已经存在的键值对
xiaoming_dict["age"] = 18
xiaoming_dict["name"] = "小小明"
# 3.删除
xiaoming_dict.pop("name")
#在删除指定的键值对时，如果key不存在，程序会报错!
print(xiaoming_dict)