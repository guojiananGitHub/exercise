# try:
#     f = open('E:\exercise/test.txt', 'r')
#     read()會一次性讀取文件的全部內容
#     print(f.read())
#     调用readline()可以每次读取一行内容，调用readlines()一次读取所有内容并按行返回list。
#     for line in f.readline():
#         print(line.strip())
#
# finally:
#     if f:
#         f.close()

# with open('E:\exercise/test.txt', 'r') as f:
#     print(f.read())


# 要读取二进制文件，比如图片、视频等等，用'rb'模式打开文件即可：
# f = open('E:\exercise/641.jpg', 'rb')
# print(f.read())


# 要读取非UTF-8编码的文本文件，需要给open()函数传入encoding参数，例如，读取GBK编码的文件：
# f = open('E:\exercise/test.txt', 'r', encoding='gbk')
# print(f.read())

# 寫文件
# f = open('E:\exercise/test.txt', 'w')
# f.write('Hi')
# f.close()

with open('E:\exercise/test.txt','w') as f:
    f.write('Hello')