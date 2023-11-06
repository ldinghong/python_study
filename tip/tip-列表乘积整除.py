def is_product_divisible_by_sum(numbers_list):
    # 此处编写代码
    s = 1
    c = 0
    for i in numbers_list:
        s *= i
    for j in numbers_list:
        c += j
    if s % c == 0:
        return True
    return False
# 获取整数输入并将其转换为列表
numbers_list = list(map(int, input().split()))
# 调用函数打印结果
print(is_product_divisible_by_sum(numbers_list))