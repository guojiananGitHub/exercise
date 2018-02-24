# try:
#     f = open('E:\exercise/test.txt', 'r')
#     print(f.read())
# finally:
#     if f:
#         f.close()

with open('E:\exercise/test.txt', 'r') as f:
    # print(f.read())
    for line in f.readlines():
        print(line.strip())

# 要读取二进制文件，比如图片、视频等等，用'rb'模式打开文件即可：
# f = open('E:\exercise\\641.jpg', 'rb')
# print(f.read())

# f = open('E:\exercise\\test.txt', 'r', encoding='gbk', errors='ignore')
# print(f.read())

# f = open('E:\exercise/test.txt', 'w')
# f.write('Hello,world!')
# f.close()

with open('E:\exercise/test.txt', 'a') as f:
    f.write('\nHello,world!')