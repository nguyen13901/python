# Bài 1: Viết chương trình kiểm tra 1 số có phải là lũy thừa của 2 hay không
# VD: Input 4 8 là lũy thừa của 2, 6 12 không phải là lũy thừa của 2
import math

def isExponential(n, base):
    if n < 0:
        return False
    while n > 1:
        if n % base != 0:
            return False
        n /= base
    return True

# using library Math
def isExponentialLibrary(n, base):
    if n < 0:
        return False
    return math.log(n, base).is_integer()

if __name__ == '__main__':
    print('4 la luy thua cua 2: ', isExponential(4, 2))
    print('8 la luy thua cua 2: ', isExponential(8, 2))
    print('6 la luy thua cua 2: ', isExponential(6, 2))
    print('12 la luy thua cua 2: ', isExponential(12, 2))

    #using library
    print("==========================")
    print('4 la luy thua cua 2: ', isExponentialLibrary(4, 2))
    print('8 la luy thua cua 2: ', isExponentialLibrary(8, 2))
    print('6 la luy thua cua 2: ', isExponentialLibrary(6, 2))
    print('12 la luy thua cua 2: ', isExponentialLibrary(12, 2))