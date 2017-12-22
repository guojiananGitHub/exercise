classmates = ['Michael', 'Bob', 'Tracy']

#   len()函數可以獲得list元素個數
print(len(classmates))

#   append()追加元素到末尾
classmates.append('Adam')
print(classmates)

#   insert()把指定的元素插入到指定的位置
classmates.insert(1, 'Jack')
print(classmates)

#   pop()方法刪除末尾元素
classmates.pop()
print(classmates)

#   pop(i)刪除指定元素
classmates.pop(1)
print(classmates)

#   list裏數據類型可以不同
L = ['Apple', 123, True]
print(L)

#   list元素可以包含list
s = ['python', 'java', ['asp', 'php'], 'scheme']
print(len(s))

#   打印list中的list元素
print(s[2][-1])

#   元組只有1個元素時必須加一個逗號,
t = (1,)
print(t)
