from collections import deque
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
n = int(input())

arr = [list(map(int, input())) for _ in range(n)]

v = [[0] * n for _ in range(n)]
lst = []
def bfs(sx, sy):
    q = deque()
    q.append((sx, sy))
    v[sx][sy] =1
    cnt = 1
    while q:
        cx, cy = q.popleft()
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if 0 <= nx < n and 0 <= ny < n and arr[nx][ny] == 1 and v[nx][ny] == 0:
                q.append((nx, ny))
                v[nx][ny] = 1
                cnt += 1
    lst.append(cnt)

for i in range(n):
    for j in range(n):

        if arr[i][j] == 1 and v[i][j] == 0:
            bfs(i, j)
lst.sort()
print(len(lst))
for i in lst:
    print(i)