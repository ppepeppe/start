def find(p, x):
    if p[x] != x:
        p[x] = find(p, p[x])
    return p[x]

def union(a, b, p):
    a = find(p, a)
    b = find(p, b)
    if a < b:
        p[b] = a
    else:
        p[a] = b

n, m = map(int, input().split())

G = []
for _ in range(m):
    a, b, c = map(int, input().split())
    G.append((c, a, b))

p = [0] * (n+1)
for i in range(1, n+1):
    p[i] = i

G.sort()
last = 0
total = 0
for e in G:
    cost, a, b = e
    if find(p, a) != find(p, b):
        union(a, b, p)
        total += cost
        last = cost
print(total, last)
