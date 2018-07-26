import re

# s = 'ABC\\-001'  # Python的字符串
# 對應的正則表達式字符串變成：
# 'ABC\-001'

# s = r'ABC\-001'  # Python的字符串
# 對應的正則表達式字符串不變：
# 'ABC\-001'

# match()方法判断是否匹配，如果匹配成功，返回一个Match对象，否则返回None
# print(re.match(r'^\d{3}\-\d{3,8}$', '010-12345'))
# print(re.match(r'^\d{3}\-\d{3,8}$', '010 12345'))

# 常见的判断方法就是：
# test = '用戶輸入的字符串'
# if re.match(r'正則表達式', test):
#     print('ok')
# else:
#     print('fail')

# 切分字符串
# print('a b   c'.split(' '))
# print(re.split(r'\s+', 'a b   c'))
# print(re.split(r'[\s\,]+', 'a,b, c  d'))
# print(re.split(r'[\s\,\;]+', 'a,b;; c  d'))


# 分組
# 用()表示的就是要提取的分组（Group）。比如：^(\d{3})-(\d{3,8})$分别定义了两个组，可以直接从匹配的字符串中提取出区号和本地号码：
# m = re.match(r'^(\d{3})-(\d{3,8})$', '010-12345')
# print(m)
# print(m.group(0))
# print(m.group(1))
# print(m.group(2))


# 贪婪匹配
# print(re.match(r'^(\d+)(0*)$', '102300').groups())  # 由于\d+采用贪婪匹配，直接把后面的0全部匹配了，结果0*只能匹配空字符串了
# print(re.match(r'^(\d+?)(0*)$', '102300').groups())  # 必须让\d+采用非贪婪匹配（也就是尽可能少匹配），才能把后面的0匹配出来，加个?就可以让\d+采用非贪婪匹配

# 編譯
re_telephone = re.compile(r'^(\d{3})-(\d{3,8})$')
# 使用
print(re_telephone.match('010-12345').groups())
print(re_telephone.match('010-8086').groups())