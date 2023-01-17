from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(sx, sy, k):
    q = deque()
    v = [[0] * n for _ in range(n)]
    q.append((sx, sy))
    v[sx][sy] = 1
    if arr[sx][sy] == 1:
        cnt = 1
    else:
        cnt = 0
    while q:
        cx, cy = q.popleft()
        if v[cx][cy] == k:
            return cnt
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if 0 <= nx < n and 0 <= ny < n and v[nx][ny] == 0:
                if arr[nx][ny] == 1:
                    cnt += 1
                q.append((nx, ny))
                v[nx][ny] = v[cx][cy] + 1
    return cnt
def cost(x):
    return (x * x) + (x-1) * (x-1)
TC = int(input())
for tc in range(1, TC+ 1):
    n, k = map(int, input().split())

    arr = [list(map(int, input().split())) for _ in range(n)]
    max_val = -1
    result = 0
    for i in range(n):
        for j in range(n):
            for s in range(1,n+2):
                ans = bfs(i, j, s)
                sol = ans * k - cost(s)
                if sol >= 0:
                    if ans > max_val:
                        max_val = ans

    print('#{} {}'.format(tc, max_val))
