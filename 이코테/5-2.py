from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

n, m = map(int, input().split())

arr = [list(map(int, input())) for _ in range(n)]
v = [[0] * m for _ in range(n)]

def bfs(sx, sy):
    q = deque()
    q.append((sx, sy))
    v[sx][sy] = 1
    while q:
        cx, cy = q.popleft()
        if cx == n-1 and cy == m-1:
            return
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] == 1 and v[nx][ny] == 0:
                q.append((nx, ny))
                v[nx][ny] = v[cx][cy] + 1

bfs(0, 0)
print(v[n-1][m-1])