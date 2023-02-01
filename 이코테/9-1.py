n, m = map(int, input().split())
inf = 1e9
G = [[inf] * (n+1) for _ in range(n+1)]

for i in range(1, n+1):
    G[i][i] = 0
for _ in range(m):
    a, b = map(int, input().split())
    G[a][b] = 1
    G[b][a] = 1
x, k =map(int, input().split())
for i in range(1, n+1):
    for j in range(1, n+1):
        for k in range(1, n+1):
            G[j][k] = min(G[j][k], G[j][i] + G[i][k])

dis = G[1][k] + G[k][x]

if dis >= inf:
    print(-1)
else:
    print(dis)