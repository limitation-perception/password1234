

def solve():
    num1 = int(input())
    arr1 = list(map(int, input().split()))
    num2 = int(input())
    arr2 = list(map(int, input().split()))
    result = []
    i = 0
    j = 0

    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]:
            result.append(arr1[i])
            i += 1
        else:
            result.append(arr2[j])
            j += 1
    result.extend(arr1[i:])
    result.extend((arr2[j:]))
    print(' '.join(list(map(str, result))))


solve()