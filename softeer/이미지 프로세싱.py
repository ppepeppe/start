from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(sx, sy, num):
    v = [[0] * m for _ in range(n)]
    std = arr[sx-1][sy-1]
    arr[sx-1][sy-1] = num
    q = deque()
    q.append((sx-1, sy-1))
    v[sx-1][sy-1] = 1
    while q:
        cx, cy = q.popleft()
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if 0 <= nx < n and 0 <= ny < m:

                if v[nx][ny] == 0 and arr[nx][ny] == std:

                    q.append((nx, ny))
                    v[nx][ny] = 1
                    arr[nx][ny] = num


n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
k = int(input())
for _ in range(k):
    a, b, c = map(int, input().split())
    bfs(a, b, c)
for i in arr:
    print(i)