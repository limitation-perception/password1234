# Бінарний пошук сесії
import sys


def bin_s(arr, x):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = low + (high - low) // 2
        if arr[mid] < x:
            low = mid + 1
        elif arr[mid] > x:
            high = mid - 1
        else:
            while arr[mid] == x:
                mid -= 1
            return mid + 1
    return -1


n = int(input())
arr = list(map(int, sys.stdin.readline().split(' ')))
q = int(input())
while q > 0:
    print(bin_s(arr, int(input())))
    q -= 1
