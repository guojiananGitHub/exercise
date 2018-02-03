from collections import Iterator

def is_odd(n):
    return n % 2 == 1

print(list(filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15])))


def no_empty(s):
    return s and s.strip()

print(list(filter(no_empty, ['A', '', 'B', None, 'C', '  '])))

print(isinstance(filter(is_odd, [1, 2]), Iterator)) # 判斷filter()是否是Iterator对象
