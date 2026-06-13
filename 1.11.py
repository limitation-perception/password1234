students_count = int(input())
lst = []
biggest = None
for i in range(students_count):
    lst.append(input())

for i in range(students_count):
    lst[i] = lst[i].split()

for i in range(students_count):
    lst[i][1] = int(lst[i][1])
students_strick = []
for i in range(students_count):
    counter = 0
    max_count = 0
    for l in range(lst[i][1]):
        if l == 1:
            counter += 1
            if counter >= max_count:
                max_count = counter
                biggest = lst[i][0]
        elif l == 0:
            counter = 0
    # student_strick = list(int(max_count), str(lst[i][0]))
    # students_strick.append(student_strick)
    lst[i][1] = max_count
    print(biggest)

print("1")
