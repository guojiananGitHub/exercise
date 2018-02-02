L = [x*x for x in range(10)]
print(L)

# 要创建一个generator，有很多种方法。第一种方法很简单，只要把一个列表生成式的[]改成()，就创建了一个generator：
g = (x*x for x in range(10))
for n in g:
    print(n)

# 斐波拉契数列（Fibonacci），除第一个和第二个数外，任意一个数都可由前两个数相加得到：1, 1, 2, 3, 5, 8, 13, 21, 34, ...
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        # print(b)
        yield b  # 如果一个函数定义中包含yield关键字，那么这个函数就不再是一个普通函数，而是一个generator：
        a, b = b, a+b
        n = n+1
    return 'done'
# for n in fib(6):
#     print(n)

# 用for循环调用generator时，发现拿不到generator的return语句的返回值。如果想要拿到返回值，必须捕获StopIteration错误，返回值包含在StopIteration的value中：
g = fib(6)
while True:
    try:
        x = next(g)
        print('g:', x)
    except StopIteration as e:
        print('Generator return value:', e.value)
        break

# def odd():
#     print('Step 1')
#     yield 1
#     print('Step 2')
#     yield(3)
#     print('Step 3')
#     yield(5)