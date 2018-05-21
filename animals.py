# 当我们定义一个class的时候，可以从某个现有的class继承，新的class称为子类（Subclass），
# 而被继承的class称为基类、父类或超类（Base class、Super class）。


class Animal(object):
    def run(self):
        print('Animal is running...')


# 当我们需要编写Dog和Cat类时，就可以直接从Animal类继承：

class Dog(Animal):
    pass


class Cat(Animal):
    pass