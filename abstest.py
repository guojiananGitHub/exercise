import math


#   絕對值
def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x
# print(abs(-99))


#   空函數
def nop():
    pass


#   返回多個值
def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y + step * math.sin(angle)
    return nx, ny

x, y = move(100, 100, 60, math.pi/6)
print(x, y)


#   一元二次方程
# 请定义一个函数quadratic(a, b, c)，接收3个参数，返回一元二次方程：
# ax2 + bx + c = 0
# 的两个解。
# 提示：计算平方根可以调用math.sqrt()函数：
def quadratic(a, b, c):
    if not isinstance(a, (int, float)):
        raise TypeError('a is not a number')
    if not isinstance(b, (int, float)):
        raise TypeError('b is not a number')
    if not isinstance(c, (int, float)):
        raise TypeError('b is not a number')
    d = b*b - 4*a*c
    if a == 0:
        if b == 0:
            if c == 0:
                return '方程根為全體實數'
            else:
                return '方程無根'
        else:
            x1 = -c/b
            x2 = x1
            return x1, x2
    else:
        if d < 0:
            return '方程無根'
        else:
            x1 = (-b + math.sqrt(d)/2/a)
            x2 = (-b - math.sqrt(d)/2/a)
            return x1, x2
print(quadratic(0, 0, 0))
print(quadratic(1, 3, -4))
print('Hello')