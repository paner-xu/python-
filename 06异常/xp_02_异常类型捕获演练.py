try:
    num = int(input("请输入有一个整数: "))
    result = 8 / num
    print(result)
except ValueError:
    print("请输入正确的整数：")
except ZeroDivisionError:
    print("除零错误")