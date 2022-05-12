fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
# count number of element 'apple' in list fruit
print(fruits.count("apple"))
# add element 'kiwi' end of the list
fruits.append('kiwi')
print(fruits)
# get index of 'banana'
print(fruits.index('banana'))
# get index of 'banana' from index 4
print(fruits.index('banana', 4))
# reverse list
fruits.reverse()
print(fruits)
# sort list
fruits.sort()
print(fruits)

# using for create list
squares = []
for i in range(5):
    squares.append(i ** 2)
print(squares)
#or
squares = [x**2 for x in range(10)]

# using lamda create list
squares = list(map(lambda x: x**2, range(5)))


#==============================================

# List Comprehensions

# Let's learn about list comprehensions! You are given three integers X, Y and Z representing the dimensions of a cuboid along with an
# integer N. You have to print a list of all possible coordinates given by (i, j, k) on a 3D grid where the sum of i + j + k  is not
# equal to N. Here, 0 <= i <= X; 0 <= j <= Y; 0 <= k <= Z

# Input Format
# Four integers X, Y, Z and N each on four separate lines, respectively.

# Constraints
# Print the list in lexicographic increasing order.

# Sample Input
# 1
# 1
# 1
# 2

# Sample Output
# [[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]


# Enter your code here. Read input from STDIN. Print output to STDOUT

X = int(input())
Y = int(input())
Z = int(input())
N = int(input())

ans = [[i, j, k] for i in range(X+1) for j in range(Y+1) for k in range(Z+1) if i + j + k != N]
print(ans)