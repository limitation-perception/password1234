lst = input()
left = 0
right = 0

for i in lst:
    if i == "(":
        left += 1
    elif i == ")":
        right += 1

if left == right:
    print("YES")
elif left != right:
    print("NO")