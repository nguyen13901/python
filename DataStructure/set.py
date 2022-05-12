# Sets: unordered, mutable, no duplicate

#my_set = set("Hello")
#my_set = {1, 2, 3, 1, 2, 45, 45, 12}
#my_set = set([1, 2, 3, 1,2 , 4, 60])
my_set = set()

my_set.add(1)
my_set.add(4)
my_set.add(19)
my_set.add(2)
my_set.add(-10)

#my_set.remove(4)
my_set.discard(4)
#my_set.remove(10) --> if set has no member that is element-> it's cause error
#my_set.discard(10) --> if set has not member that is element --> do nothing

# print(my_set)
#
# odds = {1, 3, 5, 7, 9}
# evens = {2, 4, 6, 8, 10}
# primes = {2, 3, 5, 7}
#
# print(odds.union(evens))
# print(odds.intersection(primes))
#
setA = {1, 2, 3, 4, 5, 6, 7, 8, 9}
setB = {1, 2, 3, 10, 11, 12}
#
# diff = setA.difference(setB) # list elements in setA that different elements in setB
# print(diff)
#
# diff2 = setA.symmetric_difference(setB) # list all different in elements in setA and setB
# print(diff2)
#
# setA.symmetric_difference_update(setB)
# print(setA)
#
# setA.difference_update(setB)
# print(setA)
#
# setA.update(setB)
# print(setA)

# print(setA.issubset(setB))
# setC = {1, 2, 3, 4}
# print(setC.issubset(setA))
#
# setB = setC.copy()
# print(setB)
# setC.add(10)
# print(setB)

#a = frozenset([1, 2, 3 ,4])

