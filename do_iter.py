from collections import Iterable
# 如何判断一个对象是可迭代对象呢？方法是通过collections模块的Iterable类型判断
print(isinstance('ABC', Iterable))  # str是否可迭代
print(isinstance([1, 2, 3], Iterable))  # list是否可迭代
print(isinstance(123, Iterable))  # 整数是否可迭代

# 如果要对list实现类似Java那样的下标循环怎么办？Python内置的enumerate函数可以把一个list变成索引-元素对
for i, value in enumerate(['A', 'B', 'C']):
    print(i, value)

# 同时引用了两个变量
for x, y in [(1, 1), (2, 4), (3, 9)]:
    print(x, y)
