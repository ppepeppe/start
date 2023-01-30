n, m = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(n)]

max_val  = -1
for lst in arr:
    min_val = min(lst)
    if max_val < min_val:
        max_val = min_val
print(max_val)