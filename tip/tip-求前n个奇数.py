def find_first_n_odds(n):
    # 此处写你的代码
    count = 0
    i = 0
    a = list()
    while count < n:
        if i % 2 == 1:
            a.append(i)
            count += 1
        i += 1
    return a
# 获取输入n
n = int(input())
# 调用函数
print(find_first_n_odds(n))