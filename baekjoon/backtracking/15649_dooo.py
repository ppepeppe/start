N, k = map(int, input().split())

lst = []

def dfs(n, llst):
    if n == k:
        lst.append(llst)
        return

    for i in range(1, N+1):
        if v[i] == 0:
            v[i] = 1
            dfs(n+1, llst + [i])
            v[i] = 0
v = [0] * (N+1)
dfs(0, [])
for i in lst:
    print(*i)