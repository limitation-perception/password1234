def solve(m,n):
    for i in range(n):
        arr = []
        for j in range(m):
            if i % 2:
                if (j + 1) % 2:
                    arr.append(".")
                else:
                    arr.append("#")
            if not i % 2:
                if j % 2:
                    arr.append(".")
                else:
                    arr.append("#")

        print(''.join(arr))

solve(n=4, m=6)