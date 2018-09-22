from collections import namedtuple
from collections import deque
from collections import defaultdict
from collections import OrderedDict
# namedtuple是一个函数，它用来创建一个自定义的tuple对象，并且规定了tuple元素的个数，并可以用属性而不是索引来引用tuple的某个元素。
# 这样一来，我们用namedtuple可以很方便地定义一种数据类型，它具备tuple的不变性，又可以根据属性来引用，使用十分方便。
Point = namedtuple('Point', ['x', 'y'])
p = Point(1, 2)
print(p.x)
print(p.y)
# namedtuple('名稱', [屬性list]):
Circle = namedtuple('Circle', ['x', 'y', 'r'])  # 用座標和半徑表示一個圓

q = deque(['a', 'b', 'c'])
q.append('x')
q.appendleft('y')
print(q)

# 使用dict时，如果引用的Key不存在，就会抛出KeyError。如果希望key不存在时，返回一个默认值，就可以用defaultdict：
dd = defaultdict(lambda: 'N/A')
dd['key1'] = 'abc'
print(dd['key1'])
print(dd['key2'])


