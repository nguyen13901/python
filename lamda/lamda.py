# lamda arguments: expression

# add10 = lambda x: x + 10
# print(add10(5))
#
# def add10_func(x):
#     return x + 10
#
# print(add10_func(5))
#
# mult = lambda x, y: x*y
# print(mult(2, 7))

# def sort_point(points):
#     return points[1]
#
# points2D = [(1, 2), (15, 1), (5, -1), (10, 4)]
# #points2D_sorted = sorted(points2D)
#
#
# #points2D_sorted = sorted(points2D, key = lambda point: point[1])\
# #points2D_sorted = sorted(points2D, key = sort_point)
# points2D_sorted = sorted(points2D, key = lambda point: point[0] + point[1])
# print(points2D_sorted)

# map (func, seq)
# a = [1, 2, 3, 4, 5]
# b = map(lambda x : x * 2, a)
# print(a)
# print(list(b))
#
# # filter(func, seq)
# a = [1, 2, 3, 4, 5, 6]
# b = filter(lambda x: x % 2 == 0, a)
# print(a)
# print(list(b))
#
# # reduce(func, seq)
from functools import reduce
a = [1, 2, 3, 4, 5, 6]
# b = reduce(lambda x,_ : x + [x[-1] + x[-2]], range(2),  [0, 1])
b = range(0, 2)
# print(a)
print(type(b))