import functools


def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator


# 函数也是一个对象
@log('execute')
def now():
    print('2015-3-25')


# 函数对象可以被赋值给变量
# f = now
# # print(f()) # 调用函数对象
# print(now.__name__)  # __name__属性可以拿到函数的名字
# print(f.__name__)

print(now())
