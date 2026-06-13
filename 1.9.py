task_count = int(input())
lst = []
for i in range(task_count):
    lst.append(input().split())

# task_count = 4
# lst = [
#     ["Lab2_OOP", "5"],
#     ["Essay_English", "3"],
#     ["Lab1_Discrete", "5"],
#     ["Project_DB", "1"]
# ]


tasks = []
for i in range(task_count):
    temp_wr = str(lst[i][1]) + str(lst[i][0])
    tasks.append(temp_wr)

tasks_sorted = sorted(tasks)

for i in range(task_count):
    tasks_sorted[i] = tasks_sorted[i][0:1] + " " + tasks_sorted[i][1:]
    print(tasks_sorted[i])

