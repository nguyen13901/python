# collections: Counter, namedtuple, OrderedDict, defaultdict, deque

# from collections import Counter
#
# a = "aabbbbaassccbbaa"
# my_counter = Counter(a)
# print(my_counter)
# print(type(my_counter.items()))
# print(my_counter.most_common(2))
#
# # convert counter to list
# print(list(my_counter.elements()))

# from collections import namedtuple
#
# Point = namedtuple('Point', 'x, y')
# pt = Point(1, -4)
# print(type(pt))

# from collections import OrderedDict
#
# print("This is a Dict:\n")
# d = {}
# d['a'] = 1
# d['b'] = 2
# d['c'] = 3
# d['d'] = 4
#
# for key, value in d.items():
#     print(key, value)

# Starting from Python 3.7, insertion order of Python dictionaries is guaranteed.
# print("\nThis is an Ordered Dict:\n")
# od = OrderedDict()
# od['a'] = 1
# od['b'] = 2
# od['c'] = 3
# od['d'] = 4
#
# for key, value in od.items():
#     print(key, value)
#
# from collections import defaultdict
# d = defaultdict(float)
# d['a'] = 2
# d['a'] = 1
# d[2] = 3
# print(d)

from collections import deque
d = deque()

d.append(1)
d.append(2)
print(d.pop())


a = "hello"

d.appendleft(3)
d.append(4)
print(d)