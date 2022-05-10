# Viết chương trình tính tổng S = 4! +7! + 12! + 18!\
import math
def factorial(n):
    if n < 0:
        raise ArithmeticError("Illegal number! Number must be greater than or equals 0")
    return 1 if (n == 0 or n == 1) else n * factorial(n-1)


if __name__ == '__main__':
    print('4! +7! + 12! + 18! = ', factorial(4) + factorial(7)
                                     + factorial(7) + factorial(12))

    # using library
    print('===========================')
    print('4! +7! + 12! + 18! = ', math.factorial(4) + math.factorial(7)
          + math.factorial(7) + math.factorial(12))