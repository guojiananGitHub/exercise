# 在Class内部，可以有属性和方法，而外部代码可以通过直接调用实例变量的方法来操作数据，这样，就隐藏了内部的复杂逻辑。
# 但是，从前面Student类的定义来看，外部代码还是可以自由地修改一个实例的name、score属性：
# 如果要让内部属性不被外部访问，可以把属性的名称前加上两个下划线__，在Python中，实例的变量名如果以__开头，就变成了一个私有
# 变量（private），只有内部可以访问，外部不能访问，所以，我们把Student类改一改：


class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score

    # 如果要让内部属性不被外部访问，可以把属性的名称前加上两个下划线__，在Python中，实例的变量名如果以__开头，就变成了一个
    # 私有变量（private），只有内部可以访问，外部不能访问
    def print_score(self):
        print('%s: %s' % (self._name, self._score))

    # 如果外部代码要获取name和score怎么办？可以给Student类增加get_name和get_score这样的方法：
    def get_name(self):
        return self.get_name

    def get_score(self):
        return self.get_score

    # 如果又要允许外部代码修改score怎么办？可以再给Student类增加set_score方法：
    def set_score(self, score):
        self._score = score
        return self._score

a = Student('haro', 80)
a.set_score(90)
print(a.name, a._score)

# 练习
# 请把下面的Student对象的gender字段对外隐藏起来，用get_gender()和set_gender()代替，并检查参数有效性：
#
# # -*- coding: utf-8 -*-
#
# class Student(object):
#     def __init__(self, name, gender):
#         self._name = name
#         self._gender = gender
#
#     def get_gender(self):
#         return self._gender
#
#     def set_gender(self,gender):
#         if gender in ['male','female']:
#             self._gender = gender
#         else:
#             print('...')
# # 测试:
# bart = Student('Bart', 'male')
# if bart.get_gender() != 'male':
#     print('测试失败!')
# else:
#     bart.set_gender('female')
#     if bart.get_gender() != 'female':
#         print('测试失败!')
#     else:
#         print('测试成功!')