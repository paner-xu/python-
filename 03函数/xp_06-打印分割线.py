def print_line():
    print("-" * 50)
print_line()

# 改进版
def print_line(char):
    print(char * 50)
print_line("$")

# 改进版
def print_line(char, times):
    print(char * times)
print_line("*", 40)