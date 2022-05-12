# 12. Write a Python program to rearrange positive and negative numbers in a given array using Lambda. Go to the editor
# Original arrays:
# [-1, 2, -3, 5, 7, 8, 9, -10]
# Rearrange positive and negative numbers of the said array:
# [2, 5, 7, 8, 9, -10, -3, -1]

original = [-1, 2, -3, 5, 7, 8, 9, -10]

sorting = sorted(original, key = lambda i : 0 if i == 0 else -1 / i)
print("Rearrange positive and negative numbers of the said array: ")
print(sorting)

# Write a Python program to count the even, odd numbers in a given array of integers using Lambda. Go to the editor
# Original arrays:
# [1, 2, 3, 5, 7, 8, 9, 10]
# Number of even numbers in the above array: 3
# Number of odd numbers in the above array: 5

original_arr = [1, 2, 3, 5, 7, 8, 9, 10]
odds = list(filter(lambda x: x % 2 == 1, original_arr))
evens = list(filter(lambda x: x % 2 == 0, original_arr))
print("Number of even numbers in the above array: ", len(odds))
print("Number of odd numbers in the above array: ", len(evens))