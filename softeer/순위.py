n, m = map(int, input().split())
lst = list(map(int, input().split()))
lst = [0] + lst
cnt = [1] * (n+1)

for _ in range(m):
    a, b = map(int, input().split())
    if lst[a] > lst[b]:
        cnt[b] = 0
    elif lst[a] < lst[b]:
        cnt[a] = 0
    else:
        cnt[a] = 0
        cnt[b] = 0
ans = 0
for i in range(1, n+1):
    if cnt[i] == 1:
        ans += 1
print(ans)
