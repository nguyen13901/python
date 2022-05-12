# Write a Python program that multiply each number of given list with a given number using lambda function. Print the result. Go to the editor
# Original list: [2, 4, 6, 9, 11]
# Given number: 2
# Result:
# 4 8 12 18 22

original = [2, 4, 6, 9, 11]
n = 2

result = list(map(lambda x: x * 2, original))
print(result)

# Write a Python program to calculate the sum of the positive and negative numbers of a given list of numbers using lambda function
# Original list: [2, 4, -6, -9, 11, -12, 14, -5, 17]
# Sum of the positive numbers: 48
# Sum of the negative numbers: -32

from functools import reduce

original = [2, 4, -6, -9, 11, -12, 14, -5, 17]
sum1 = reduce(lambda x, y: x if y < 0 else x + y, original, 0)
sum2 = reduce(lambda x, y: x if y > 0 else x + y, original, 0)
print("Sum of the positive numbers: ", sum1)
print("Sum of the negative numbers: ", sum2)

#original = [2, 4, -6, -9, 11, -12, 14, -5, 17]

list1 = list(filter(lambda x: x > 0, original))
list2 = list(filter(lambda x: x < 0, original))

print("Sum of the positive numbers: ", sum(list1))
print("Sum of the negative numbers: ", sum(list2))