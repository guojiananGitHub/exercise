from collections import Iterator

# filter()把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素。
def is_odd(n):
    return n % 2 == 1

print(list(filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15])))


def no_empty(s):
    return s and s.strip()

print(list(filter(no_empty, ['A', '', 'B', None, 'C', '  '])))

print(isinstance(filter(is_odd, [1, 2]), Iterator)) # 判斷filter()是否是Iterator对象
