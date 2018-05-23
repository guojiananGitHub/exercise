from types import MethodType


class Student(object):
    __slots__ = ('name', 'age')  # 为了达到限制的目的，Python允许在定义class的时候，定义一个特殊的__slots__变量，
    # 来限制该class实例能添加的属性：
    # pass

# # 给实例绑定一个属性
# s = Student()
# s.name = 'Michael'  # 动态给实例绑定一个属性

# 给实例绑定一个方法


# def set_age(self, age):  # 定义一个函数作为实例方法
#     self.age = age
#
# s.set_age = MethodType(set_age, s)  # 给实例绑定一个方法
# s.set_age(25)
# print(s.age)  # 测试结果

# 给一个实例绑定的方法，对另一个实例不起作用


# s2 = Student()  # 创建新的实例
# print(s2.set_age(25))  # 尝试调用方法

# 给所有实例都绑定方法，可以给class绑定方法


# def set_score(self, score):
#     self.score = score

# Student.set_score = set_score
# s.set_score(100)
# print(s.score)
# s2.set_score(99)
# print(s2.score)

# 限制class实例添加属性测试
s = Student()  # 创建新的实例
s.name = 'Michael'  # 绑定属性‘name’
s.age = 25  # 绑定属性‘age’
# s.score = 99  # 绑定属性‘score’

# 使用__slots__要注意，__slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的：


class GraduateStudent(Student):
    pass

g = GraduateStudent()
g.score = 9999