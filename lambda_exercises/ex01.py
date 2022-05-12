# 1. Write a Python program to create a lambda function that adds 15 to a given number passed in as an argument,
# also create a lambda function that multiplies argument x with argument y and print the result.

# Sample Output:
# 25
# 48

a = 25
sum_lambda = lambda x, y: x + y

print(sum_lambda(25, 13))

# create a lambda function that multiplies argument x with argument y and print the result.
mul_lambda = lambda x, y : x * y
print(mul_lambda(3, 5))

# Write a Python program to create a function that takes one argument, and that argument will be multiplied with
# an unknown given number.

def my_lambda(n):
    return lambda x: x * n

print("Double the number of 15 =", (my_lambda(2))(15))

print("Triple the number of 15 =", (my_lambda(3))(15))

print("Quadruple the number of 15 =", (my_lambda(4))(15))

print("Quintuple the number 15 =", (my_lambda(5))(15))
