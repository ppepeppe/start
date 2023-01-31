n, k = map(int, input().split())

lst = []
for _ in range(n):
    lst.append(int(input()))
lst.sort()
dp = [10001] * 10001

dp[0] = 0
for i in lst:
    for j in range(i, 10001):
        if dp[j-i] != 10001:
            dp[j] = min(dp[j], dp[j-i] + 1)
if dp[k] == 10001:
    print(-1)
else:
    print(dp[k])