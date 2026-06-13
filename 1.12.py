calc_count = int(input())
lst = []
for i in range(calc_count):
    lst.append(input().split())


for i in range(calc_count):
    if lst[i][0] == "2":
        dec = int(lst[i][2], 2)
        if lst[i][1] == "10":
            print(dec)
        elif lst[i][1] == "8":
            ei = oct(dec)
            print(ei)
        elif lst[i][1] == "2":
            bi = bin(dec)
            print(bi)
        elif lst[i][1] == "16":
            he = hex(dec)
            print(he)
    elif lst[i][0] == "8":
        dec = int(lst[i][2], 8)
        if lst[i][1] == "10":
            print(dec)
        elif lst[i][1] == "8":
            ei = oct(dec)
            print(ei)
        elif lst[i][1] == "2":
            bi = bin(dec)
            print(bi)
        elif lst[i][1] == "16":
            he = hex(dec)
            print(he)
    elif lst[i][0] == "10":
        dec = int(lst[i][2], 10)
        if lst[i][1] == "10":
            print(dec)
        elif lst[i][1] == "8":
            ei = oct(dec)
            print(ei)
        elif lst[i][1] == "2":
            bi = bin(dec)
            print(bi)
        elif lst[i][1] == "16":
            he = hex(dec)
            print(he)
    elif lst[i][0] == "16":
        dec = int(lst[i][2], 16)
        if lst[i][1] == "10":
            print(dec)
        elif lst[i][1] == "8":
            ei = oct(dec)
            print(ei)
        elif lst[i][1] == "2":
            bi = bin(dec)
            print(bi)
        elif lst[i][1] == "16":
            he = hex(dec)
            print(he)
