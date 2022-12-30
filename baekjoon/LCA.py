import sys
input = sys.stdin.readline
sys.setrecursionlimit(int(1e5))

n = int(input())

G = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b = map(int, input().split())
    G[a].append(b)
    G[b].append(a)
p = [0] * (n+1)
c = [0] * (n+1)
d = [0] * (n+1)
d[1] = 1
def dfs(m, k):
    c[m] = 1
    d[m] = k
    for j in G[m]:
        if c[j] != 0:
            continue
        p[j] = m
        dfs(j, k+1)

def LCA(a, b):
    while d[a] != d[b]:
        if d[a] > d[b]:
            a = p[a]
        else:
            b = p[b]
    while a!= b:
        a = p[a]
        b = p[b]
    return a
dfs(1, 0)

m = int(input())
for _ in range(m):
    a, b = map(int, input().split())
    print(LCA(a, b))