# Злиття відсортованих потоків

import heapq
import sys


def merge_k(arr, k):
    res = []
    h = []
    for i in range(len(arr)):
        heapq.heappush(h, (arr[i][0], i, 0))
    while h:
        val, ap, vp = heapq.heappop(h)
        res.append(val)
        if vp + 1 < len(arr[ap]):
            heapq.heappush(h, (arr[ap][vp + 1], ap, vp + 1))
    return res


k = int(input())
arr = []
for i in range(k):
    n = int(input())
    arr.append(list(map(int, sys.stdin.readline().strip().split())))
print(' '.join(list(map(str, merge_k(arr, k)))))