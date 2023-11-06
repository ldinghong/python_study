def list_between(start, end):
    # 此处写你的代码
    a = []
    for i in range(start+1,end):
        a.append(i)
    return a
# 获取输入的start 及 end
start = int(input())
end = int(input())

# 调用函数
print(list_between(start, end))