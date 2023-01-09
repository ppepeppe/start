n, k = map(int, input().split())
lst = []
for _ in range(n):
    lst.append(int(input()))

lst.sort()
start = 1
end = lst[n-1] - lst[0]
ans = 0
while start <= end:
    mid = (start + end) // 2
    cnt = 1
    stand = lst[0]
    for i in range(1, n):
        if lst[i] >= stand + mid:
            cnt += 1
            stand = lst[i]

    if cnt >= k:
        start = mid + 1
        ans = mid
    else:
        end = mid - 1
print(ans)