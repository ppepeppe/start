from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

n, m = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(n)]


def bfs(sx, sy):
    v = [[0] * m for _ in range(n)]
    q = deque()
    q.append((sx, sy))
    v[sx][sy] = 1
    arr[sx][sy] = -1
    while q:
        cx, cy = q.popleft()
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if 0 <= nx < n and 0 <= ny < m and v[nx][ny] == 0 and (arr[nx][ny] == 0 or arr[nx][ny] == -1):
                q.append((nx, ny))
                v[nx][ny] = 1
                arr[nx][ny] = -1

snow_cnt = 0
c = 1
for i in range(n):
    for j in range(m):
        if arr[i][j] == 1:
            snow_cnt += 1


snow_ccnt = 0
time = 0
snow = []
while snow_ccnt < snow_cnt:
    bfs(0, 0)

    for i in range(n):
        for j in range(m):
            if arr[i][j] == 1:
                cnt = 0
                new = []
                for k in range(4):
                    nx = i + dx[k]
                    ny = j + dy[k]
                    if arr[nx][ny] == -1:
                        cnt += 1
                if cnt >= 2:

                    snow.append((i,j))

    for x, y in snow:
        arr[x][y] = 0
        snow_ccnt += 1

    snow = []
    time += 1
print(time)