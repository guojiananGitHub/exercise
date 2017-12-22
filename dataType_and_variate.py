#   科學記數法
print(1.23e9)
print(1.23e-9)

#   轉義字符
print('I\'m ok.')
print('\\\n\\')

#   r''表示''內部不轉義
print(r'\\\n\\')

#   r'''...'''表示多行內容
print(r'''line
line2
line3''')

#   變量經典案例
a = 'ABC'
b = a
a = 'XYZ'
print(b)