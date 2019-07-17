def func_a(data):
    data.pop(0)
    return data


def func_b(data):
    data.pop(-2)
    return data


def func_c(data):
    data.append(100)
    return data

a = [4, 8, 3, 4, 1]
res = func_a(a)
print(res)
a = [4, 8, 3, 4, 1]
res = func_b(a)
print(res)
a = [4, 8, 3, 4, 1]
res = func_c(a)
print(res)
