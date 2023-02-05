import sys
from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

n, m = map(int, input().split())
arr = [list(input()) for _ in range(n)]

cnt = 0
for i in range(n):
    for j in range(m):
        if arr[i][j] == '#':
            cnt += 1

def check(x, y):
    ccnt = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] == '#':
            ccnt += 1
            sx = nx
            sy = ny
            sd = i
    if ccnt > 1:
        return False
    return x, y, sd

def bfs(sx, sy, sd):
    q = deque()
    q.append((sx, sy, sd))
    v = [[[0] * 2 for _ in range(m)] for _ in range(n)]

    v[sx][sy][0] = sd
    v[sx][sy][1] = 1
    path = []
    total = 1
    while q:
        cx, cy, cd = q.popleft()
        flag = 0
        while True:
            if cd == 4:
                cd = 0
            elif cd == 5:
                cd = 1
            elif cd == -1:
                cd = 3
            elif cd == -2:
                cd = 2
            nx = cx + dx[cd] * 2
            ny = cy + dy[cd] * 2
            print(cx, cy, nx, ny, cd, path)
            if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] == '#' and arr[nx-dx[cd]][ny-dy[cd]] == '#' and v[nx][ny][1] == 0 and v[nx-dx[cd]][ny-dy[cd]][0] == 0:

                v[nx][ny][0] = cd
                v[nx - dx[cd]][ny - dy[cd]][1] = 1
                v[nx - dx[cd]][ny - dy[cd]][0] = cd
                v[nx][ny][1] = 1
                q.append((nx, ny, cd))
                total += 2
                if flag == 0:
                    path.append('A')
                elif flag == 1:
                    path.append('L')
                    path.append('A')
                else:
                    path.append('R')
                    path.append('A')

                break
            elif flag != 2:
                if flag == 0:
                    cd -= 1
                    flag = 1
                elif flag == 1:
                    cd += 2
                    flag = 2
            else:
                break
    if total == cnt:
        return path
    else:
        return False

min_len = 1e9
ans = 0

for i in range(n):
    for j in range(m):
        if arr[i][j] == '#' and check(i, j):

            sx, sy, sd = check(i,j)
            ppath = bfs(sx, sy, sd)
            if ppath:

                # if min_len > len(ppath):
                #     min_len = len(ppath)
                #     sol = ppath
                #     ans_x = sx
                #     ans_y = sy
                #     ans = sd
                #     sys.exit()
                dicr = ['^', '>', 'v', '<']
                print(sx + 1, sy + 1)
                print(dicr[sd])
                print(''.join(ppath))
                sys.exit()
