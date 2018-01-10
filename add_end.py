# 默認參數n=2
# def power(x, n=2):
#     s = 1
#     while n > 0:
#         n = n - 1
#         s = s * x
#     return s
# print(power(5))

# 定义默认参数要牢记一点：默认参数必须指向不变对象！None為不變對象
# def add_end(L = None):
#     if L is None:
#         L = []
#     L.append('END')
#     return L

# 可變參數
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n*n
    return sum
print(calc())

# 關鍵字參數
def person(name, age, *, city, job):
    print(name, age, city, job)