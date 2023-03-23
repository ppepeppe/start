from collections import deque
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

n, l, r = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(n)]



def bfs(sx, sy, idx):
    united = []
    united.append((sx, sy))
    q = deque()
    q.append((sx, sy))
    v[sx][sy] = idx
    total = arr[sx][sy]
    cnt = 1
    while q:
        cx, cy = q.popleft()
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if 0 <= nx < n and 0 <= ny < n and v[nx][ny] == 0:
                if l <= abs(arr[cx][cy] - arr[nx][ny]) <= r:
                    q.append((nx, ny))
                    united.append((nx, ny))
                    v[nx][ny] = idx
                    total += arr[nx][ny]
                    cnt += 1
    num = total//cnt
    for i in united:
        arr[i[0]][i[1]] = num
    return
time = 0
while True:
    v = [[0] * n for _ in range(n)]
    idx = 1
    for i in range(n):
        for j in range(n):
            if v[i][j] == 0:
                bfs(i, j, idx)
                idx += 1

    if idx == n * n + 1:
        break
    time += 1
print(time)