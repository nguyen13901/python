# 17. Write a Python program to find numbers divisible by nineteen or thirteen from a list of numbers using Lambda. Go to the editor
# Orginal list:
# [19, 65, 57, 39, 152, 639, 121, 44, 90, 190]
# Numbers of the above list divisible by nineteen or thirteen:
# [19, 65, 57, 39, 152, 190]

orignal = [19, 65, 57, 39, 152, 639, 121, 44, 90, 190]

numbers = list(filter(lambda x: x % 19 == 0 or x % 13 == 0, orignal))

print(numbers)

# Write a Python program to find all anagrams of a string in a given list of strings using lambda. Go to the editor
# Orginal list of strings:
# ['bcda', 'abce', 'cbda', 'cbea', 'adcb']
# Anagrams of 'abcd' in the above string:
# ['bcda', 'cbda', 'adcb']

from collections import Counter

orignal = ['bcda', 'abce', 'cbda', 'cbea', 'adcb']
str = 'abcd'
anagrams = list(filter(lambda x: sorted(str) == sorted(x), orignal))
print(anagrams)

anagrams2 = list(filter(lambda x: (Counter(str) == Counter(x)), orignal))
print(anagrams2)