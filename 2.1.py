def solve():
    n = int(input())
    lines = []
    for i in range(n):
        lines.append(input().split())
    children = {}
    names = {}
    root_id = None

    for i in range(n):
        node_id = int(lines[i][0])
        name = lines[i][1]
        parent_id = int(lines[i][2])

        names[node_id] = name

        if parent_id == 0:
            root_id = node_id
        else:
            if parent_id not in children:
                children[parent_id] = []
            children[parent_id].append(node_id)

    for p_id in children:
        children[p_id].sort()

    def print_tree(current_id, depth):
        indent = " " * (2 * depth)
        print(f"{indent}{names[current_id]}")

        if current_id in children:
            for child_id in children[current_id]:
                print_tree(child_id, depth + 1)

    if root_id is not None:
        print_tree(root_id, 0)


solve()