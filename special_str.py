class Student(object):
    def __init__(self, name):
        self.name = name
    # 只需定義好__str__()方法，返回一個好看的字符串
    def __str__(self):
        return 'Student object (name: %s)' % self.name

print(Student('Michael'))