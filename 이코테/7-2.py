n, k = map(int, input().split())
lst = list(map(int, input().split()))

s = 0
e = max(lst)
ans = 0
while s <= e:
    mid = (s+e)//2
    total = 0
    for i in range(n):
        if lst[i] - mid > 0:
            total += lst[i] - mid

    if total < k:
        e = mid - 1
    else:
        ans = mid
        s = mid + 1
print(ans)