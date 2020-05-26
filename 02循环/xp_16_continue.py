i = 0
while i < 10:
    # continue 条件满足时，不执行后续重复的代码
    # i == 3
    if i == 3:
        # 注意：在循环体中，如果使用continue关键字，在使用之前，
        # 要确认循环的计数是否修改，否则可能会导致死循环
        i += 1
        continue
    print(i)
    i += 1