from random import randint
import sys
n = int(input())
ar = []
for i in range(n):
    ar.append(list(sys.stdin.readline().strip().split(' ')))
def part(array, low, high):
    rand_idx = randint(low, high)
    array[low], array[rand_idx] = array[rand_idx], array[low]
    k = array[low]
    i = low + 1
    j = high
    while i <= j:
        while i <= high and three_compare(array[i], k):
            i += 1
        while j >= low and not three_compare(array[j], k) and array[j] != k:
            j -= 1
        if i <= j:
            array[i], array[j] = array[j], array[i]
            i += 1
            j -= 1
    array[low], array[j] = array[j], array[low]
    return j
def quick_sort(array, low, high):
    if low < high:
        pi = part(array, low, high)
        quick_sort(array, low, pi - 1)
        quick_sort(array, pi + 1, high)

def three_compare(arr1, arr2):
    if arr1[1] != arr2[1]:
        return arr1[1] > arr2[1]
    if arr1[2] != arr2[2]:
        return arr1[2] > arr2[2]
    return arr1[0] < arr2[0]

quick_sort(ar, 0, n - 1)
for student in ar:
    print(student[0])