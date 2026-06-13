# Рюкзак першокурсника
import sys


def knapsack_tabulation(capacity, values, weights):
    n = len(values)
    tab = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i-1] <= w:
                include_item = values[i-1] + tab[i-1][w - weights[i-1]]
                exclude_item = tab[i-1][w]
                tab[i][w] = max(include_item, exclude_item)
            else:
                tab[i][w] = tab[i-1][w]

    items_included = []
    w = capacity
    for i in range(n, 0, -1):
        if tab[i][w] != tab[i-1][w]:
            items_included.append(i-1)
            w -= weights[i-1]

    print(tab[n][capacity])
    items_included.sort()
    print(' '.join(list(map(lambda el: str(el+1), items_included))))

    return tab[n][capacity]


n, w = tuple(map(int, input().strip().split(' ')))
val = []
wt = []
for i in range(n):
    inp = list(map(int, sys.stdin.readline().strip().split(' ')))
    val.append(inp[0])
    wt.append(inp[1])
knapsack_tabulation(w, val, wt)
