import sys
sys.setrecursionlimit(10**6)
n, m = map(int, input().split())
start_G = [[] for _ in range(n+1)]
end_G = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    start_G[a].append(b)
    end_G[b].append(a)
s, e = map(int, input().split())


def dfs(s, G, v):
    if v[s] == 1:
        return
    v[s] = 1
    for c in G[s]:
        dfs(c, G, v)
    return
start_s = [0] * (n+1)
start_s[e] = 1
dfs(s, start_G, start_s)

end_s = [0] * (n+1)
dfs(s, end_G, end_s)

start_e = [0] * (n+1)
start_e[s] = 1
dfs(e, start_G, start_e)

end_e = [0] * (n+1)
dfs(e, end_G, end_e)

cnt = 0
for i in range(1, n+1):
    if start_s[i] and start_e[i] and end_s[i] and end_e[i]:
        cnt += 1
print(cnt-2)