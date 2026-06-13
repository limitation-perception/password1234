n = int(input())
errors = []
for i in range(n):
    errors.append(input())
seen = {}
for error in errors:
    if error in seen:
        seen[error] += 1
    else:
        seen[error] = 1
max_elem = 0
max_keys = []
for key in seen:
    if seen[key] >= max_elem:
        max_elem = seen[key]
        max_keys.append(key)
max_keys = sorted(max_keys)
print(max_keys[0])





