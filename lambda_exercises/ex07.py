# Write a Python program to find the values of length six in a given list using Lambda.
# Sample Output:
# Monday
# Friday
# Sunday

weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
days = list(filter(lambda x: len(x) == 6, weekdays))
print(days)

# Write a Python program to add two given lists using map and lambda. Go to the editor
# Original list:
# [1, 2, 3]
# [4, 5, 6]
# Result: after adding two list
# [5, 7, 9]

num1 = [1, 2, 3]
num2 = [4, 5, 6]

result = list(map(lambda x, y: x + y, num1 ,num2))
print(result)

result2 = [num1[i] + num2[i] for i in range(3)]
print(result2)
