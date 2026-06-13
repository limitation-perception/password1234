log_count = int(input())
lst = []
for i in range(log_count):
    lst.append(input())

uni = []
count = 0
for i in lst:
    if i not in uni:
        count += 1
        uni.append(i)

print(count)
if count > 1000:
    print("ALERT")
else:
    print("OK")
