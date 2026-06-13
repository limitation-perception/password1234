# Підмасив із максимальною сумою
import sys


def max_subarray(array):
    max_so_far = max_ending_here = array[0]
    start_index = 0
    end_index = 0
    for i in range(1, len(array) - 1):
        temp_start_index = None
        if array[i] > (max_ending_here + array[i]):
            temp_start_index = i
            max_ending_here = array[i]
        else:
            max_ending_here = max_ending_here + array[i]
        if max_so_far < max_ending_here:
            max_so_far = max_ending_here
            if temp_start_index != None:
                start_index = temp_start_index
            end_index = i
    print(max_so_far, start_index, end_index)


n = int(input())
ar = list(map(int, sys.stdin.readline().strip().split()))
max_subarray(ar)
