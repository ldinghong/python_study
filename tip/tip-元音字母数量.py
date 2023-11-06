def vowel_count(string):
    # 此处写你的代码
    count = 0
    for i in string:
        if (i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u'):
            count += 1
    return count
# 获取输入字符串
input_string = input()
# 调用函数
print(vowel_count(input_string))