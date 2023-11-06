def is_string_identical(text_string):
    # 此处编写代码
    for i in text_string:
        if i != text_string[0]:
            return False
    return True
# 获取输入
text_string = input()
# 调用函数
print(is_string_identical(text_string))