from collections import deque
from collections import defaultdict

v, e, s, t = map(int, input().split())
adj = defaultdict(list)

for _ in range(e):
    u, to = map(int, input().split())
    adj[u].append(to)

q = deque([s])
parent = {s: None}
found = False

while q:
    curr = q.popleft()
    if curr == t:
        found = True
        break
    for nxt in adj[curr]:
        if nxt not in parent:
            parent[nxt] = curr
            q.append(nxt)

if not found:
    print("UNREACHABLE")
else:
    path = []
    curr = t
    while curr is not None:
        path.append(curr)
        curr = parent[curr]
    path.reverse()
    print(len(path))
    print(" ".join(map(str, path)))
