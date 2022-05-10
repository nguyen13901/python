# Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score.
# You are given n scores. Store them in a list and find the score of the runner-up.

# Sample input :
# 5
# 2 3 6 6 5
# Output: 5

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    l_arr = list(set(arr))
    print(sorted(l_arr)[-2])

