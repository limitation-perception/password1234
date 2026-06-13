N, T = map(int, input().split())
grades = list(map(int, input().split()))
average = sum(grades) // len(grades)

print(average)
if int(average) >= T:
    print("PASS")
else:
<<<<<<< HEAD
    print("FAIL")
=======
    print("FAIL")
>>>>>>> 2207d4bb462497716731058b4df168a5b4602ca8
