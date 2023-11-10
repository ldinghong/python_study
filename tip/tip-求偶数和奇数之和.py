def calculate_sum(numbers_list):
    # 此处编写代码
    even_sum = 0
    odd_sum = 0
    for i in numbers_list:
        if i % 2 == 0:
            even_sum += i
        else:
            odd_sum += i
    r = list()
    r.append(even_sum)
    r.append(odd_sum)
    return r
# 获取输入转为列表
numbers_list = list(map(int,input().split()))

# 打印偶数和奇数的和
print(calculate_sum(numbers_list))