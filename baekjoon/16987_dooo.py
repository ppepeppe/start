N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

def dfs(n, cnt):
    global ans
    if n == N:
        ans = max(ans, cnt)
        return

    if arr[n][0] <= 0:
        dfs(n+1, cnt)
    else:
        flag = 0
        for j in range(N):
            if arr[j][0] <= 0 or n == j:
                continue
            break_egg = 0
            flag = 1
            arr[n][0] -= arr[j][1]
            arr[j][0] -= arr[n][1]
            if arr[n][0] <= 0:
                break_egg += 1
            if arr[j][0] <= 0:
                break_egg += 1

            dfs(n+1, cnt + break_egg)
            arr[n][0] += arr[j][1]
            arr[j][0] += arr[n][1]

        if flag == 0:
            dfs(n+1, cnt)
ans = 0
dfs(0, 0)
print(ans)
