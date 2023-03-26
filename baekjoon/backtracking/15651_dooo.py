N, k = map(int, input().split())

def dfs(n, lst):
    if n == k:
        print(*lst)
        return
    for i in range(1, N + 1):
        dfs(n+1, lst + [i])

dfs(0, [])