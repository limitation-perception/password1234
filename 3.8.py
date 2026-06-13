v, e = map(int, input().split())
adj = {i: [] for i in range(1, v + 1)}
for i in range(e):
    u, vv = map(int, input().split())
    adj[u].append(vv)
    adj[vv].append(u)

visited = set()
comps = []

for i in range(1, v + 1):
    if i not in visited:
        comp = []
        q = [i]
        visited.add(i)
        while q:
            curr = q.pop(0)
            comp.append(curr)
            for nxt in adj[curr]:
                if nxt not in visited:
                    visited.add(nxt); q.append(nxt)
        comps.append(sorted(comp))

print(len(comps))
largest = comps[0]
for x in comps:
    if len(x) > len(largest) or (len(x) == len(largest) and x[0] < largest[0]):
        largest = x
print(len(largest))
print(" ".join(map(str, largest)))