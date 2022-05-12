# Write a Python program to sort each sublist of strings in a given list of lists using lambda.
# Original list:
# [['green', 'orange'], ['black', 'white'], ['white', 'black', 'orange']]
# After sorting each sublist of the said list of lists:
# [['green', 'orange'], ['black', 'white'], ['black', 'orange', 'white']]

original = [['green', 'orange'], ['black', 'white'], ['white', 'black', 'orange']]

sorting = list(map(lambda x: sorted(x), original))

print(sorting)

# Write a Python program to sort a given list of lists by length and value using lambda. Go to the editor
# Original list:
# [[2], [0], [1, 3], [0, 7], [9, 11], [13, 15, 17]]
# Sort the list of lists by length and value:
# [[0], [2], [0, 7], [1, 3], [9, 11], [13, 15, 17]]

original = [[2], [0], [1, 3], [0, 7], [9, 11], [13, 15, 17]]

sorting = sorted(original, key = lambda x: (len(x), x))

print(sorting)