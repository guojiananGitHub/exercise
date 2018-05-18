# 类与实例的学习
class Student(object):
    # 实例：__init__(self,参数,参数)
    def __init__(self, name, score):
        self.name = name
        self.score = score

    # 数据封装
    # Student实例本身就拥有这些数据，要访问这些数据，就没有必要从外面的函数去访问，可以直接在Student类的内部定义访问
    # 数据的函数，这样，就把“数据”给封装起来了。这些封装数据的函数是和Student类本身是关联起来的，我们称之为类的方法
    def print_score(self):
        print('%s: %s' % (self.name, self.score))

    # 封装的另一个好处是可以给Student类增加新的方法，比如get_grade：
    def get_grade(self):
        if self.score>90:
            return 'A'
        elif self.score>80:
            return 'B'
        else:
            return 'C'

a = Student('haro', 60)
b = Student('clear_love', 99)
# 同样的，get_grade方法可以直接在实例变量上调用，不需要知道内部实现细节：
print(a.name, a.get_grade())
print(b.name, b.get_grade())