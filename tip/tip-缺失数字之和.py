def sum_missing_numbers(nums):
    # 此处编写代码
    sum = (min(nums) + max(nums)) * (max(nums) - min(nums) + 1) // 2
    for i in nums:
        sum -= i
    return sum
# 获取输入转为数字列表
nums = list(map(int, input().split()))

# 调用函数
print(sum_missing_numbers(nums))