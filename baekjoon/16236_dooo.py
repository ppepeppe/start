from  collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(sx, sy):
    q = deque()
    q.append((sx, sy))
    d = [[-1] * n for _ in range(n)]
    d[sx][sy] = 0
    while q:
        cx, cy = q.popleft()
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if 0 <= nx < n and 0 <= ny < n and d[nx][ny] == -1 and arr[nx][ny] <= ns:
                q.append((nx, ny))
                d[nx][ny] = d[cx][cy] + 1
    return d

def find(dist):
    global min_val, ns
    ssx = -1
    ssy = -1
    for i in range(n):
        for j in range(n):
            if dist[i][j] > 0 and arr[i][j] != 0 and arr[i][j] < ns:
                if dist[i][j] < min_val:
                    min_val = dist[i][j]
                    ssx = i
                    ssy = j
    return ssx, ssy, min_val

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]


flag = 0
for i in range(n):
    for j in range(n):
        if arr[i][j] == 9:
            sx = i
            sy = j
            flag = 1
            arr[i][j] = 0
            break
    if flag == 1:
        break

ns = 2

ate = 0
sol = 0

while True:
    v = bfs(sx, sy)
    min_val = 1e9
    ssx, ssy, ans = find(v)
    arr[ssx][ssy] = 0
    if ans == 1e9:
        print(sol)
        break
    else:
        sol += ans
    ate+= 1
    if ate == ns:
        ns += 1
        ate = 0
    sx = ssx
    sy = ssy
else:
    print(sol)