# Viết chương trình nhập vào một dãy các số nguyên từ bàn phím. Tìm số lẻ
# lớn nhất trong dãy số và in ra.

# VD: 5 1 9 11 20 19 17 21 30
# => Kết quả : 21


if __name__ == '__main__':
    a = [5, 1, 9, 11, 20, 19, 17, 21, 30]
    maxOdd = None

    for i in sorted(a)[::-1]:
        if i % 2 != 0:
            maxOdd = i
            break

    if maxOdd is None:
        raise ValueError('There were no odd integers in {}'.format(a))
    print('max odd: ', maxOdd)