N, T = map(int, input().split())
grades = list(map(int, input().split()))
average = sum(grades) // len(grades)

print(average)
if int(average) >= T:
    print("PASS")
else:
    print("FAIL")