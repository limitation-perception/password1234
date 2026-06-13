import sys


def dfs(node, p=-1):
    global timer
    tin[node] = low[node] = timer
    timer += 1
    children = 0

    for to in adj[node]:
        if to == p:
            continue
        if tin[to] != -1:
            if tin[to] < low[node]:
                low[node] = tin[to]
        else:
            dfs(to, node)
            if low[to] < low[node]:
                low[node] = low[to]

            if low[to] >= tin[node] and p != -1:
                ap[node] = True
            children += 1

    if p == -1 and children > 1:
        ap[node] = True


v, e = sys.stdin.readline().strip().split()
v = int(v)
e = int(e)
adj = {}
for i in range(1, v + 1):
    adj[i] = []

for _ in range(int(e)):
    line = input().split()
    u = int(line[0])
    vv = int(line[1])
    adj[u].append(vv)
    adj[vv].append(u)

timer = 0
tin = [-1] * (v + 1)
low = [-1] * (v + 1)
ap = {}


for i in range(1, v + 1):
    if tin[i] == -1:
        dfs(i)

if len(ap) == 0:
    print("NONE")
else:
    print(len(ap))
    ap_list = []
    for node in ap:
        ap_list.append(node)
    ap_list.sort()

    ap_str = ""
    for node in ap_list:
        ap_str += str(node) + " "
    print(ap_str)
