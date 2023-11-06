def find_nth_smallest(numbers_list, n):
    # 此处编写你的代码
    if n > len(numbers_list):
        return
    a = sorted(numbers_list)
    return a[n-1]
# 将输入的整数转换为列表
numbers_list = list(map(int, input().split()))
# 获取n的输入
n = int(input())
# 调用函数
print(find_nth_smallest(numbers_list, n))