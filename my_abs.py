import math


#   絕對值
def abs(x):
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
def quadratic(a, b, c):
