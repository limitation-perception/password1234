from statistics import median


def solve(students,numbers):

    arr1 = list(map(int, numbers.split()))
    arr1 = sorted(arr1)

    arr2 = []

    print("Output:")
    print(f"Min: {min(arr1)}")
    print(f"Max: {max(arr1)}")
    print(f"Median: {median(arr1)}")
    for i in arr1:
        if i > median(arr1):
            arr2.append(i)
    print(f"Above average: {len(arr2)}")


solve(5,"70 90 60 80 100")
