def compare_length(str1, str2):
    # 此处编写你的代码
    if len(str1) == len(str2):
        return True
    return False
# 获取输入
input_str1 = input()
input_str2 = input()

# 调用函数
print(compare_length(input_str1, input_str2))