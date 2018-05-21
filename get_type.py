# 判断基本数据类型可以直接写int，str等，但如果要判断一个对象是否是函数怎么办？可以使用types模块中定义的常量：
import types
import animals


def fn():
    pass

print(type(fn) == types.FunctionType)
print(type(abs) == types.BuiltinFunctionType)
print(type(lambda x: x) == types.LambdaType)
print(type((x for x in range(10))) == types.GeneratorType)

# 对于class的继承关系来说，使用type()就很不方便。我们要判断class的类型，可以使用isinstance()函数。
# 总是优先使用isinstance()判断类型，可以将指定类型及其子类“一网打尽”。

a = animals.Animal()
d = animals.Dog()
print(isinstance(a, animals.Dog))
print(isinstance(d, animals.Animal))

# 如果要获得一个对象的所有属性和方法，可以使用dir()函数，它返回一个包含字符串的list，比如，获得一个str对象的所有属性和方法：
print(dir('ABC'))

# 类似__xxx__的属性和方法在Python中都是有特殊用途的，比如__len__方法返回长度。在Python中，如果你调用len()函数试图获取一个对象的
# 长度，实际上，在len()函数内部，它自动去调用该对象的__len__()方法，所以，下面的代码是等价的：

print(len('abc'))
print('abc'.__len__())

# 仅仅把属性和方法列出来是不够的，配合getattr()、setattr()以及hasattr()，我们可以直接操作一个对象的状态：


class MyObject(object):
    def __init__(self):
        self.x = 9

    def power(self):
        return self.x * self.x

obj = MyObject()

print(hasattr(obj, 'x'))  # 有‘X’吗？
print(obj.x)
print(hasattr(obj, 'y'))   # 有 ‘Y’吗？
setattr(obj, 'y', 19)  # 设置一个属性‘y'
print(hasattr(obj, 'y'))  # 有 ‘Y’吗？
print(getattr(obj, 'y'))  # 获取属性’y‘
print(obj.y)  # 获取属性’y‘

# 如果试图获取不存在的属性，会抛出AttributeError的错误：

# print(getattr(obj, 'z')) # 获取属性'z'

# 可以传入一个default参数，如果属性不存在，就返回默认值：

print(getattr(obj, 'z', 404))  # 获取属性'z'，如果不存在，返回默认值404

# 也可以获得对象的方法：

print(hasattr(obj, 'power'))  # 有属性'power'吗？
print(getattr(obj, 'power'))  # 获取属性'power'
fn = getattr(obj, 'power')  # 获取属性'power'并赋值到变量fn
print(fn)  # fn指向obj.power
print(fn())  # 调用fn()与调用obj.power()是一样的
