print(sorted([36, 5, -12, 9, -21]))

print(sorted([36, 5, -12, 9, -21], key = abs))

print(sorted(['bob', 'about', 'Zoo', 'Credit']))

print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower)) # 排序忽略大小写，按照字母序排序

print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True)) # 反向排序