def read_graph():
    first_line = []
    first_line.extend(input().split())

    V = int(first_line[0])
    E = int(first_line[1])

    adj = [[] for _ in range(V + 1)]

    for _ in range(E):
        edge = []
        edge.extend(input().split())
        u = int(edge[0])
        v = int(edge[1])
        adj[u].append(v)
        adj[v].append(u)

    return V, adj


def bfs_color(start_node, adj, color):
    q = [start_node]
    head = 0
    color[start_node] = 0

    while head < len(q):
        u = q[head]
        head += 1

        for v in adj[u]:
            if color[v] == -1:
                color[v] = 1 - color[u]
                q.append(v)
            elif color[v] == color[u]:
                return False
    return True


def check(V, adj):
    color = [-1] * (V + 1)

    for i in range(1, V + 1):
        if color[i] == -1:
            if not bfs_color(i, adj, color):
                return False, []

    return True, color


def print_result(is_bi, color, V):
    if not is_bi:
        print("NO")
        return

    print("YES")
    part1 = []
    part2 = []

    for i in range(1, V + 1):
        if color[i] == 0:
            part1.append(str(i))
        elif color[i] == 1:
            part2.append(str(i))

    print(" ".join(part1))
    print(" ".join(part2))


if __name__ == "__main__":
    V, adj = read_graph()
    is_bip, color = check(V, adj)
    print_result(is_bip, color, V)