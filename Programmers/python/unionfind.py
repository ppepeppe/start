def find(p, x):
    if p[x] != x:
        p[x] = find(p, p[x])
    return p[x]


def union(p, a, b):
    a = find(p, a)
    b = find(p, b)
    if a < b:
        p[b] = a
    else:
        p[a] = b


def solution(n, costs):
    answer = 0
    costs.sort(key=lambda x: x[2])
    p = [0] * n
    for i in range(n):
        p[i] = i
    for e in costs:
        now, next, cost = e
        if find(p, now) != find(p, next):
            union(p, now, next)
            answer += cost

    return answer