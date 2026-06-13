import sys


v, e = sys.stdin.readline().strip().split()
v = int(v)
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
bridges = []


def dfs(node, p=-1):
    global timer
    tin[node] = low[node] = timer
    timer += 1

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

            if low[to] > tin[node]:
                u_edge = node
                v_edge = to
                if u_edge > v_edge:
                    temp = u_edge
                    u_edge = v_edge
                    v_edge = temp
                bridges.append([u_edge, v_edge])


for i in range(1, v + 1):
    if tin[i] == -1:
        dfs(i)


bridges.sort(key=lambda ed: (ed[0], ed[1]))

print(len(bridges))
for edge in bridges:
    print(str(edge[0]) + " " + str(edge[1]))
