import os

print(os.name)
print(os.environ)
print(os.environ.get('PATH'))

print(os.path.abspath('.'))

# 把两个路径合成一个时，不要直接拼字符串，而要通过os.path.join()函数，这样可以正确处理不同操作系统的路径分隔符。在Linux/Unix/Mac下，os.path.join()返回这样的字符串：
print(os.path.join('E:\exercise', 'testdir'))

# os.mkdir('E:\exercise/testdir')
# os.rmdir('E:\exercise/testdir')

# 要拆分路径时，也不要直接去拆字符串，而要通过os.path.split()函数，这样可以把一个路径拆分为两部分，后一部分总是最后级别的目录或文件名：
print(os.path.split('E:\exercise/test2/test2.txt'))

# os.path.splitext()可以直接让你得到文件扩展名
print(os.path.splitext('E:\exercise/test2/test2.txt'))

# 对文件重命名:
# os.rename('test.txt', 'test.py')

# 删掉文件:
# os.remove('test.py')

# 利用Python的特性来过滤文件。比如我们要列出当前目录下的所有目录
print([x for x in os.listdir('.') if os.path.isdir(x)])

# 列出所有的.py文件
print([x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1] == '.py'])