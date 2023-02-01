import heapq

inf = 1e9

n, m, s = map(int, input().split())

G = [[] for _ in range(n+1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    G[a].append((b, c))

d = [inf] * (n+1)

def dijk(s):
    q = []
    d[s] = 0
    heapq.heappush(q, (0, s))
    while q:
        dist, now = heapq.heappop(q)
        if d[now] < dist:
            continue
        for i in G[now]:
            cost = dist + i[1]
            if d[i[0]] > cost:
                d[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
dijk(s)

cnt = 0
max_dis = -1

for k in d:
    if k != inf:
        cnt += 1
        if max_dis < k:
            max_dis = k
print(cnt-1, max_dis)