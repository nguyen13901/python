#Viết chương trình random 5 số nguyên ngẫu nhiên từ 20 – 30.
#Yêu cầu: 5 số ngẫu nhiên không được trùng nhau

import random
import sys
if __name__ == '__main__':
    arr = set()
    while True:
        arr.add(random.randint(20, 30))
        if len(arr) == 5:
            break
    print(arr)