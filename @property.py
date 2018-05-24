class Student(object):

    # def get_score(self):
    #     return self.get_score
    #
    # def set_score(self, value):
    #     if not isinstance(value, int):
    #         raise ValueError('score must be an integer!')
    #     if value < 0 or value > 100:
    #         raise ValueError('score must between 0~100!')
    #     self._score = value

    # 装饰器（decorator）可以给函数动态加上功能,对于类的方法，装饰器一样起作用。Python内置的 @ property装饰器就是负责把一个方法
    # 变成属性调用的：
    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value

    # @property的实现比较复杂，我们先考察如何使用。把一个getter方法变成属性，只需要加上@property就可以了，此时，@property本身又
    # 创建了另一个装饰器@score.setter，负责把一个setter方法变成属性赋值，于是，我们就拥有一个可控的属性操作：
s = Student()
s.score = 60
print('s.score =', s.score)
# ValueError: score must between 0 ~ 100!
s.score = 9999

# 还可以定义只读属性，只定义getter方法，不定义setter方法就是一个只读属性：

    # @property
    # def birth(self):
    #     return self._birth
    #
    # @birth.setter
    # def birth(self, value):
    #     self.__birth__ = value
    #
    # @property
    # def age(self):
    #     return 2015 - self._birth

# 上面的birth是可读写属性，而age就是一个只读属性，因为age可以根据birth和当前时间计算出来。

s = Student()
s.birth(1993)
print(s.age)
