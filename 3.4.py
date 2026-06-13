import heapq
import sys

v, e = sys.stdin.readline().strip().split()
v = int(v)
e = int(e)
courses = []
for _ in range(v):
    courses.append(input())

adj = {}
indegree = {}
for c in courses:
    adj[c] = []
    indegree[c] = 0

for _ in range(e):
    line = input().split()
    a = line[0]
    b = line[1]
    adj[a].append(b)
    indegree[b] += 1

q = []
for c in courses:
    if indegree[c] == 0:
        heapq.heappush(q, c)

res = []
while len(q) > 0:
    curr = heapq.heappop(q)
    res.append(curr)
    for nxt in adj[curr]:
        indegree[nxt] -= 1
        if indegree[nxt] == 0:
            heapq.heappush(q, nxt)

if len(res) != v:
    print("IMPOSSIBLE")
else:
    for c in res:
        print(c)
