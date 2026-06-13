tree = input().split()


def solve(tree, father):
    i = 0
    j = 0
    while i <= len(tree) or j <= len(tree):
        i = father * 2
        j = father * 2 + 1
        if tree[i] != tree[j]:
            return print("NO")
        else:
            father += 1
            solve(tree, father)
    return print("YES")


solve(tree, 1)
