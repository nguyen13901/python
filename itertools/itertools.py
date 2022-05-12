# itertools: product, permutations, combinations, accumulate, groupby, and infinite iterators
from itertools import product
# a = [1, 2]
# b = [3, 4]
# prod = product(a, b)
# print(list(prod))

# from itertools import groupby
#
# persons = [{'name': 'Tim', 'age': 25}, {'name': 'Viet', 'age': 27}
#            ,{'name': 'Nguyen', 'age': 27}, {'name': 'Bao', 'age': 30}]
#
# arr = groupby(persons, key = lambda x: x['age'])
# for key, value in arr:
#     print(key, list(value))
# print(type(arr))

# A Python program to print all
# permutations using library function
# from itertools import permutations
#
# # Get all permutations of [1, 2, 3]
# perm = permutations([1, 2, 3])
#
# # Print the obtained permutations
# for i in list(perm):
#     print(i)

# A Python program to print all
# combinations of given length
# from itertools import combinations
#
#
# # Get all combinations of [1, 2, 3]
# # and length 2
# comb = combinations([1, 2, 3], 2)
#
#
# # Print the obtained combinations
# for i in list(comb):
#     print(i)

# from itertools import accumulate
# import operator
# a = [1, 2, 5, 3, 4]
# acc = accumulate(a, func=max)
# print(a)
# print(list(acc))