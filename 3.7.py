import sys


def activity_selection(start, finish, name):
    arr = list(zip(start, finish, name))
    res_n = [arr[0][2]]
    arr.sort(key=lambda x: x[1])

    count = 1

    j = 0

    for i in range(1, len(arr)):
        if arr[i][0] >= arr[j][1]:
            count += 1
            res_n.append(arr[i][2])
            j = i

    print(count)
    print('\n'.join(res_n))


n = int(input())
start = []
end = []
name = []
for _ in range(n):
    inp = sys.stdin.readline().strip().split(' ')
    start.append(int(inp[0]))
    end.append(int(inp[1]))
    name.append(inp[2])
activity_selection(start, end, name)

