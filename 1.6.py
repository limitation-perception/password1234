lst = str(input().lower())
sorted_list = []
for i in lst:
    if i.isalpha():
        sorted_list.append(i)


def palindrom(lst):
    if len(sorted_list) % 2 == 0:
        for i in range(len(sorted_list)):
            if i == 0:
                if sorted_list[0] != sorted_list[-1]:
                    return "NO"
            elif sorted_list[i] != sorted_list[-i + 1]:
                return "NO"
        return "YES"
    elif len(sorted_list) % 2 == 1:
        sorted_list_upd = []
        for i in sorted_list:
            if i != sorted_list[len(sorted_list)//2 + 1]:
                sorted_list_upd.append(i)
        for i in range(len(sorted_list_upd)):
            if i == 0:
                if sorted_list_upd[0] != sorted_list_upd[-1]:
                    return "NO"
            elif sorted_list_upd[i] != sorted_list_upd[-i + 1]:
                return "NO"
        return "YES"


print(palindrom(sorted_list))
