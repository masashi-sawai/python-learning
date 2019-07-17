def func(data):
    print('長さ:' + str(len(data)))
    print('最大:' + str(max(data)))
    print('最小:' + str(min(data)))
    print('合計:' + str(sum(data)))
    data.sort()
    return data

a = [4, 8, 3, 4, 1]
res = func(a)
print(res)
