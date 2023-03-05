import sys
from collections import deque
import heapq
input = sys.stdin.readline
n = int(input())

G = [[] for _ in range(n+1)]


for _ in range(n):
    lst = list(map(int, input().split()))
    for k in range(1, len(lst)-1, 2):
        G[lst[0]].append((lst[k], lst[k+1]))

def bfs(s):
    v = [-1] * (n+1)
    v[s] = 0
    q = deque()
    q.append(s)
    while q:
        c = q.popleft()
        for k in G[c]:
            if v[k[0]] == -1:
                v[k[0]] = v[c] + k[1]
                q.append(k[0])
    return v

dis = bfs(1)
max_idx = dis.index(max(dis))
print(max(bfs(max_idx)))