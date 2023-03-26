N, k = map(int, input().split())

def dfs(n, s, lst):
    if n == k:
        print(*lst)
        return

    for i in range(s, N+1):
        dfs(n+1, i, lst + [i])

dfs(0, 1, [])