dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
dd = [2, 3, 0, 1]
n, m = map(int, input().split())
sx, sy, sd = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(n)]
v = [[0] * m for _ in range(n)]
v[sx][sy] = 1

cnt = 1

while True:
    flag = 0
    nd = sd
    for _ in range(4):
        nd -= 1
        if nd == -1:
            nd = 3
        nx = sx + dx[nd]
        ny = sy + dy[nd]
        print(nx, ny, nd)
        if 0 <= nx < n and 0 <= ny < n and v[nx][ny] == 0 and arr[nx][ny] == 0:
            v[nx][ny] = 1
            cnt += 1
            flag = 1
            print(nx, ny)
            break
    if flag == 0:
        nx += dx[dd[nd]]
        ny += dy[dd[nd]]
        if 0 <= nx < n and 0 <= ny < n and v[nx][ny] == 0 and arr[nx][ny] == 0:
            print(nx, ny)
            v[nx][ny] = 1
            cnt += 1
        else:
            break
    sx, sy, sd, = nx, ny, nd

print(cnt)