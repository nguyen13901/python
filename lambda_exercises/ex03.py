# 5. Write a Python program to filter a list of integers using Lambda. Go to the editor
# Original list of integers:
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Even numbers from the said list:
# [2, 4, 6, 8, 10]
# Odd numbers from the said list:
# [1, 3, 5, 7, 9]

original_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_list = list(filter(lambda x: x % 2 == 0,original_list))
odd_list = list(filter(lambda x: x % 2 == 1, original_list))

print(even_list)
print(odd_list)

# 6. Write a Python program to square and cube every number in a given list of integers using Lambda. Go to the editor
# Original list of integers:
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Square every number of the said list:
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# Cube every number of the said list:
# [1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]
original_list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
square_list = list(map(lambda x: x**2, original_list1))
cube_list = list(map(lambda x: pow(x, 3), original_list1))

print(square_list)
print(cube_list)