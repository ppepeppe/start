n = int(input())
lst = list(map(int, input().split()))

lst.reverse()
dp = [1] * n

for i in range(1, n):
    for j in range(i+1):
        if lst[j] < lst[i]:
            dp[i] = max(dp[i], dp[j] + 1)
print(n - max(dp))