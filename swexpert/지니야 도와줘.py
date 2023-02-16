dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

n, m = map(int, input().split())
arr = [list(input()) for _ in range(n)]

rain = []
for i in range(n):
    for j in range(m):
        if arr[i][j] == 'H':
            ex = i
            ey= j
        elif arr[i][j] == 'W':
            sx = i
            sy = j
        elif arr[i][j] == '*':
            rain.append((i, j))
v = [[[0]*2 for _ in range(m)] for _ in range(n)]
def bfs(sx, sy):
    q = [(sx, sy)]
    q += rain

    v[sx][sy][0] = 1
    for i in range(1, len(q)):
        v[q[i][0]][q[i][1]][1] = 1
    while q:
        cx, cy = q.pop(0)
        if cx == ex and cy == ey:
            return v[cx][cy][0] - 1
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if arr[cx][cy] == 'W' and (arr[nx][ny] == '.' or arr[nx][ny] == 'H') and v[nx][ny][0] == 0 and v[cx][cy][0] > 0:
                        q.append((nx, ny))
                        v[nx][ny][0] = v[cx][cy][0] + 1
                        if nx != ex or ny != ey:
                            arr[nx][ny] = 'W'
                if arr[cx][cy] == '*' and arr[nx][ny] != 'X' and arr[nx][ny] != 'H' and v[nx][ny][1] == 0:
                    if v[nx][ny][0] != 0:
                        v[nx][ny][0] = -1
                    q.append((nx, ny))
                    v[nx][ny][1] = 1
                    arr[nx][ny] = '*'
ans = bfs(sx, sy)
if ans:
    print(ans)
else:
    print("FAIL")