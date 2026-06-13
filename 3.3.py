import sys
from collections import defaultdict
sys.setrecursionlimit(10**6)


v, e = map(int, input().split())
adj = defaultdict(list)
for _ in range(e):
    u, to = map(int, input().split())
    adj[u].append(to)

color = {i: 0 for i in range(1, v + 1)}
parent = {}
cycle_start, cycle_end = -1, -1


def dfs(node):
    global cycle_start, cycle_end
    color[node] = 1
    for nxt in adj[node]:
        if color[nxt] == 0:
            parent[nxt] = node
            if dfs(nxt):
                return True
        elif color[nxt] == 1:
            cycle_start = nxt
            cycle_end = node
            return True
    color[node] = 2
    return False


for i in range(1, v + 1):
    if color[i] == 0:
        if dfs(i):
            break

if cycle_start == -1:
    print("NO CYCLE")
else:
    cycle = []
    curr = cycle_end
    while curr != cycle_start:
        cycle.append(curr)
        curr = parent[curr]
    cycle.append(cycle_start)
    cycle.reverse()
    print("CYCLE FOUND")
    print(" ".join(map(str, cycle)))
