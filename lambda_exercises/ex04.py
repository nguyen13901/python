# Write a Python program to find if a given string starts with a given character using Lambda. Go to the editor
# Sample Output:
# True
# False
import datetime


def start_w(s, a):
    return s.startswith(a)


sentences = "Hello world!"
character = "a"
#my_lambda = lambda s, c: s[0] == c
def my_lambda(s, c): return s[0] == c
print(start_w(sentences, character))
print(start_w(sentences, 'H'))

print(my_lambda(sentences, character))
print(my_lambda(sentences, 'H'))

# Write a Python program to extract year, month, date and time using Lambda. Go to the editor
# Sample Output:
# 2020-01-15 09:03:32.744178
# 2020
# 1
# 15
# 09:03:32.744178


now = datetime.datetime.now()
print(now)
def year(date_time): return date_time.year
def month(date_time): return date_time.month
def day(date_time): return date_time.day
def time(date_time): return date_time.time()


print(year(now))
print(month(now))
print(day(now))
print(time(now))