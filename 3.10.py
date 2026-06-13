import sys


class Graph:
    def __init__(self, size):
        self.adj_matrix = [[0] * size for _ in range(size)]
        self.size = size

    def add_edge(self, u, v, c):
        self.adj_matrix[u][v] = c

    def bfs(self, s, t, parent):
        visited = [False] * self.size
        queue = []
        queue.append(s)
        visited[s] = True

        while queue:
            u = queue.pop(0)

            for ind, val in enumerate(self.adj_matrix[u]):
                if not visited[ind] and val > 0:
                    queue.append(ind)
                    visited[ind] = True
                    parent[ind] = u

        return visited[t]

    def edmonds_karp(self, source, sink):
        parent = [-1] * self.size
        max_flow = 0

        while self.bfs(source, sink, parent):
            path_flow = float("Inf")
            s = sink
            while(s != source):
                path_flow = min(path_flow, self.adj_matrix[parent[s]][s])
                s = parent[s]

            max_flow += path_flow
            v = sink
            while(v != source):
                u = parent[v]
                self.adj_matrix[u][v] -= path_flow
                self.adj_matrix[v][u] += path_flow
                v = parent[v]

            path = []
            v = sink
            while(v != source):
                path.append(v)
                v = parent[v]
            path.append(source)
            path.reverse()

        return max_flow


v, e, s, t = sys.stdin.readline().strip().split(' ')

g = Graph(int(v) + 1)

for _ in range(int(e)):
    inp = list(map(int, sys.stdin.readline().strip().split(' ')))
    g.add_edge(inp[0], inp[1], inp[2])

print(g.edmonds_karp(int(s), int(t)))