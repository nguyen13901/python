# collections.OrderedDict
# An OrderedDict is a dictionary that remembers the order of the keys that were inserted first.
# If a new entry overwrites an existing entry, the original insertion position is left unchanged.

# Task
# You are the manager of a supermarket.
# You have a list of n items together with their prices that consumers bought on a particular day.
# Your task is to print each item_name and net_price in order of its first occurrence.

# Sample Input
# 9
# BANANA FRIES 12
# POTATO CHIPS 30
# APPLE JUICE 10
# CANDY 5
# APPLE JUICE 10
# CANDY 5
# CANDY 5
# CANDY 5
# POTATO CHIPS 30
# =========================
# Sample Output
# BANANA FRIES 12
# POTATO CHIPS 60
# APPLE JUICE 20
# CANDY 20

from collections import OrderedDict

n = int(input())
menus = OrderedDict()
for i in range(n):
    items = input().split()
    price = int(items[-1])
    name = " ".join(items[:-1])
    if menus.get(name):
        menus[name] += price
    else:
        menus[name] = price
for key in menus.keys():
    print(key, menus[key])