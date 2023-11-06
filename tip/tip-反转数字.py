#a[1:2:3] 1：默认0，2:len,3:步长
def reverse_number_digits(num):
    # 在此处编写你的代码
    a = list(str(num))
    b = list(a[::-1])
    c = list()
    for i in b:
        c.append(int(i))
    return c
# 获取用户输入
num = int(input())

# 调用函数
print(reverse_number_digits(num))