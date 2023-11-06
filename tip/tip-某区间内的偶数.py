def find_even_numbers(num):
    # 此处写入代码
    a = list()
    for i in range(1,num+1):
        if i % 2 == 0:
            a.append(i)
    return a
# 获取整数输入
num = int(input())
# 调用函数
print(find_even_numbers(num))