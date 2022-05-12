# Tuple: ordered, immutable, allows duplicate elements
import sys

#my_tuple = "Max", 28, "Boston"
#my_tuple = tuple(["Max", 28, "Botton"])

#my_tuple2 = "a", "b", "c", "d", "e"
#print(my_tuple)

#if "a" in my_tuple2:
#    print("YES")
#else:
#   print("NO")

# if_tuple = "Peter", 28, "Manchester United"
#
# name, age, city = if_tuple
# print("Name: {}, age: {}, city: {}".format(name, age, city))
#
# my_tuple = (0, 1, 2, 3, 4, 5)
#
# i1, *i2, i3 = my_tuple
# print(i1)
# print(i2)
# print(i3)

#convert list to tuple
# arr = [1, 2, 3, 4, 5]
# arr_tuple = tuple(arr)
# print(arr_tuple)
# # convert tuple to list
#arr2 = list(arr_tuple)
#print(arr2)

# Compare size of list vs size of tuple
my_list = [0, 1, 2, "hello", True]
my_tuple1 = (0, 1, 2, "hello", True)
my_tuple2 = tuple(my_list)
print(sys.getsizeof(my_list), "bytes") # 96 bytes
print(sys.getsizeof(my_tuple1), "bytes") # 80 bytes
print(sys.getsizeof(my_tuple2), "bytes") # 80 bytes