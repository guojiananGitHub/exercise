d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
print(d['Bob'])
print(d.get('Thomas', -1))

#   set是一集組合，無序不重覆
s = set([1, 2, 2, 3, 3])
print(s)

#   通過add()添加元素
s.add(4)
print(s)

#   remove()可以刪除元素
s.remove(4)
print(s)

a = ['c', 'b', 'a']
a.sort()
print(a)

a = 'abc'
b = a.replace('a', 'A')
print(b)
print(a)