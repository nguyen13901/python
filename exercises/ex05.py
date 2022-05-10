#Viết chương trình chuyển đổi một số tự nhiên ở hệ cơ số 10 thành số ở hệ
# cơ số 2

def toBinary(n):
    rs = ''
    while n != 0:
        rs += str(n % 2)
        n //= 2
    return rs[::-1]

if __name__ == '__main__':
    print('10 to binary: ', toBinary(10))
    print('24 to binary: ', toBinary(24))
    print('18 to binary: ', toBinary(18))
    print('7 to binary: ', toBinary(7))