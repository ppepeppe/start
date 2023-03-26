N, k = map(int, input().split())

def dfs(n, lst):
    if n == N+1:
        if len(lst) == k:
            print(*lst)
        return

    dfs(n+1, lst + [n])
    dfs(n+1, lst)

dfs(1, [])