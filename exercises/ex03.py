# Nhập vào một số bất kỳ. Kiểm tra số đó có phải là số đối xứng hay không
# 121 13331 là số đối xứng.

def isReverseNumber(n):
    return str(n)[::-1] == str(n)

def isReverseNumber2(n):
    a, b = n, 0
    while a > 0:
        b = b * 10 + a % 10
        a //= 10
    return n == b

if __name__ == '__main__':
    #n = int(input())
    print('121 la so doi xung: ', isReverseNumber(121))
    print('13331 la so doi xung: ', isReverseNumber(13331))
    print('789 la so doi xung: ', isReverseNumber(789))

    print('=======================')
    print('121 la so doi xung: ', isReverseNumber2(121))
    print('13331 la so doi xung: ', isReverseNumber2(13331))
    print('789 la so doi xung: ', isReverseNumber2(789))