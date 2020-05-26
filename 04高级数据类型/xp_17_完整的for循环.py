for num in [1,2,3,4]:
    print(num)
    if num == 3:
        break

else:
    # 如果循环体内部使用了break
    # else下方的代码就不会被执行
    print("会执行吗")
print("循环结束")