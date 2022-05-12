# 10. Write a Python program to create Fibonacci series up to n using Lambda. Go to the editor
# Fibonacci series upto 2:
# [0, 1]
# Fibonacci series upto 5:
# [0, 1, 1, 2, 3]
# Fibonacci series upto 6:
# [0, 1, 1, 2, 3, 5]
# Fibonacci series upto 9:
# [0, 1, 1, 2, 3, 5, 8, 13, 21]

from functools import reduce

fib_series = lambda n: reduce(lambda x,_: x + [x[-1] + x[-2]], range(n - 2), [0, 1])

print("Fibonacci series upto 2:")
print(fib_series(2))
print("\nFibonacci series upto 5:")
print(fib_series(4))
print("\nFibonacci series upto 6:")
print(fib_series(6))
print("\nFibonacci series upto 9:")
print(fib_series(9))

x = [0, 1]
x = x + [2, 3]
print(x)

# Write a Python program to find intersection of two given arrays using Lambda
# Original arrays:
# [1, 2, 3, 5, 7, 8, 9, 10]
# [1, 2, 4, 8, 9]
# Intersection of the said arrays: [1, 2, 8, 9]

a = [1, 2, 3, 5, 7, 8, 9, 10]
b = [1, 2, 4, 8, 9]

c = list(filter(lambda x: x in a, b))
print(c)