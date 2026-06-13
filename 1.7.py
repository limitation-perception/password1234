def input_data():
    input_dat = input().split()
    data = []
    for i in range(int(input_dat[0])):
        x = input().split()
        data.append([int(y) for y in x])

    return data , int(input_dat[1])

def best_student(st):
    best_st = []
    best_n = 0
    best_score = 0
    for i in st:
        best_st.append(sum(i))

    for i in range(len(best_st)):
        if best_st[i] > best_score:
            best_score = best_st[i]
            best_n = i
    return best_n + 1

def ghost_subject(st, n):
    ghost_sb = {}
    amount_of_ghosts = 0
    for i in range(len(st)):
        for j in range(n):
            ghost_sb[j] = ghost_sb.get(j, 0) + st[i][j]
    for x in ghost_sb.keys():
        if ghost_sb[x] == 0:
            amount_of_ghosts += 1
    return amount_of_ghosts


if __name__ == "__main__":
    print("Input:")
    students, amount_of_subjects = input_data()
    best_attendance = best_student(students)
    am_of_ghosts = ghost_subject(students, amount_of_subjects)
    print("\nOutput:")
    print(best_attendance)
    print(am_of_ghosts)


