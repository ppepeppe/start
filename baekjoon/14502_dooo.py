dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
    global max_cnt
    q = []
    ccnt = 0
    v = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            v[i][j] = arr[i][j]
            if arr[i][j] == 2:
                q.append((i, j))
    while q:
        cx, cy = q.pop(0)
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if 0<= nx < n and 0 <= ny <m and v[nx][ny] == 0:
                q.append((nx, ny))
                v[nx][ny] = 2
    for r in range(n):
        for c in range(m):
            if v[r][c] == 0:
                ccnt += 1
    if max_cnt < ccnt:
        max_cnt = ccnt
def dfs(cnt):

    if cnt == 3:
        bfs()

        return

    for i in range(n):
        for j in range(m):
            if arr[i][j] == 0:
                arr[i][j] = 1
                dfs(cnt+1)
                arr[i][j] = 0
n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
max_cnt = -1
u = [[0] * m for _ in range(n)]
dfs(0)

print(max_cnt)
