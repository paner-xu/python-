def demo(num_list):
    print("函数内部的代码")
    # 如果传递的参数是可变类型，在函数内部，
    # 通过方法修改数据的内容，同样会影响到外部的参数
    num_list.append(9)
    print(num_list)
    print("函数执行结束")
gl_num_list = [1, 2, 3]
demo(gl_num_list)
print(gl_num_list)