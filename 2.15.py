from platform import python_revision

from pyasn1_modules.rfc2985 import counterSignature


def hasCycle(num1,linked):
    arr1 = list(map(int, linked.split()))
    prev = []
    cop = 0
    for i in range (num1 ** 2):
        cop = arr1[i]
        if arr1[i] in prev:
            return print(f"CYCLE AT {prev[cop]}")
        prev.append(arr1[i-1])
    return print("NO CYCLE")

hasCycle(7, "1 2 3 4 5 6 7 5 -1")