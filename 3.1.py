def input_data():
    data = input().strip()
    matrix = []
    for i in range(int(data[0])):
        row = input()
        row = [int(char) for char in row]
        matrix.append(row)
    return matrix


class UndirectedGraph:
    def __init__(self):
        self.graph = {}
        self.visited = []

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []
        self.graph[u].append(v)
        self.graph[v].append(u)


    def build_graph(self, matrix):
        rows = len(matrix)
        cols = len(matrix[0])

        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 1:
                    if rows > i > 0 and matrix[i - 1][j] == 1:
                        self.add_edge(tuple([i, j]), tuple([i - 1, j]))
                    if cols > j > 0 and matrix[i][j - 1] == 1:
                        self.add_edge(tuple([i, j]), tuple([i, j - 1]))
                    if (i, j) not in self.graph:
                        self.graph[(i,j)] = []


    def dfs(self, node):
        if node not in self.visited:
            self.visited.append(node)
            for neighbour in self.graph[node]:
                self.dfs(neighbour)

def count_islands(matrix):
    undirected_graph = UndirectedGraph()
    undirected_graph.build_graph(matrix)
    islands = 0
    for node in undirected_graph.graph.keys():
        if node not in undirected_graph.visited:
            undirected_graph.dfs(node)
            islands += 1
    return islands


if __name__ == "__main__":
    print("Input:")
    matrix = input_data()
    print("Output:")
    islands = count_islands(matrix)
    print(islands)