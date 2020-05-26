try:
    num = int(input("请输入有一个整数: "))
    result = 8 / num
    print(result)
except ValueError:
    print("请输入正确的整数：")
except Exception as result:
    print("未知错误%s" % result)
# else 只有在没有异常时才会执行的代码
else:
    print("尝试成功")
# finally 无论是否有异常，都会执行的代码
finally:
    print("无论是否出现错误都会执行的代码")
print("-" * 50)