def input_passward():
    # 1.提示用户输入密码
    pwd = input("输入密码: ")
    # 2.判断输入密码的长度>=8，返回输入的密码
    if len(pwd) >= 8:
        return pwd
    # 3.密码长度<8，主动抛出异常
    print("主动抛出异常")
    # 1.创建异常对象
    ex = Exception("密码长度不够")
    # 2.主动抛出异常
    raise ex
# 提示用户输入密码
try:
    print(input_passward())
except Exception as result:
    print("未知错误%s" % result)
