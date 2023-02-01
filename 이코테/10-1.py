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
p = [0] * (n+1)
for i in range(1, n+1):
    p[i] = i

for _ in range(m):
    h, a, b = map(int, input().split())
    if h == 0:
        union(a, b, p)
    else:
        a = find(p, a)
        b = find(p, b)
        if a==b:
            print('YES')
        else:
            print("NO")