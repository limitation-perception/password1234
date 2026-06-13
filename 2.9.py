def lcs_algo(s1, s2, m, n):
    L = [[0 for x in range(n + 1)] for x in range(m + 1)]

    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                L[i][j] = 0
            elif s1[i - 1] == s2[j - 1]:
                L[i][j] = L[i - 1][j - 1] + 1
            else:
                L[i][j] = max(L[i - 1][j], L[i][j - 1])

    index = L[m][n]

    lcs_algo = [""] * (index + 1)
    lcs_algo[index] = ""

    i = m
    j = n
    while i > 0 and j > 0:

        if s1[i - 1] == s2[j - 1]:
            lcs_algo[index - 1] = s1[i - 1]
            i -= 1
            j -= 1
            index -= 1

        elif L[i - 1][j] > L[i][j - 1]:
            i -= 1
        else:
            j -= 1

    print(len("".join(lcs_algo)))
    print("".join(lcs_algo))


s1 = input()
s2 = input()

lcs_algo(s1, s2, len(s1), len(s2))
