def f(x):
    return x*x

# map()函数接收两个参数，一个是函数，一个是Iterable，map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回
# map()函数用法，map(函数，可迭代对象)
r = map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])
print(list(r))

print(list(map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9])))