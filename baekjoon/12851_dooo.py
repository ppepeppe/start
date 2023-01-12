from collections import deque

s, e = map(int, input().split())

v = [0] * 100001
cnt = [0] * 100001
def bfs(s):
    q = deque()
    q.append(s)
    v[s] = 1
    while q:
        c = q.popleft()
        for i in (c-1, c+1, c*2):
            if 0 <= i < 100001:
                if v[i] == 0:
                    v[i] = v[c] + 1
                    q.append(i)
                    cnt[i] =1
                elif v[i] == v[c] + 1:
                    q.append(i)
                    cnt[i] += 1
bfs(s)

print(v[e]-1)
if v[e]-1 == 0:
    print(1)
else:
    print(cnt[e])