from bisect import insort_right


def solev(num,labs):
    labs_list = labs.split()
    labs_list =list(map (int,labs_list))
    is_labs_okay = True
    for i in range (num):
        if (i + 1) % 2:
            if labs_list[i] < labs_list[i-1] or labs_list[i] < labs_list[i+1]:
                is_labs_okay =True
            else:
                return print("No")
        if (i) % 2:
            if labs_list[i] > labs_list[i - 1] or labs_list[i] > labs_list[i + 1]:
                is_labs_okay = True
            else:
                return print("No")

    if is_labs_okay:
        return print("Yes")




solev(5,"4 7 2 9 1")