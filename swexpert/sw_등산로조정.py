dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

from collections import deque


def bfs(sx, sy):
    global max_val
    q = deque()
    q.append((sx, sy, arr[sx][sy], 0, [(sx, sy)]))
    v = [[[0] * 2 for _ in range(n)] for _ in range(n)]
    v[sx][sy][0] = 1
    while q:
        cx, cy, ch, ct, clst = q.popleft()

        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if ch > arr[nx][ny] and v[cx][cy][ct] + 1 >= v[nx][ny][ct]:
                    q.append((nx, ny, arr[nx][ny], ct, clst + [(nx, ny)]))
                    v[nx][ny][ct] = v[cx][cy][ct] + 1
                elif ch <= arr[nx][ny]:
                    if ct == 1:
                        continue
                    else:

                        if (nx, ny) not in clst and v[cx][cy][0] + 1 >= v[nx][ny][1]:
                            nh = arr[nx][ny]
                            for _ in range(k):
                                nh -= 1

                                if nh < ch:
                                    q.append((nx, ny, nh, 1, clst + [(nx, ny)]))
                                    v[nx][ny][1] = v[cx][cy][ct] + 1
                                    break

    for i in range(n):
        for j in range(n):
            vcnt = max(v[i][j])
            if vcnt > max_val:
                max_val = vcnt
    return v


TC = int(input())
for tc in range(1, TC + 1):
    n, k = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    max_val = 0
    max_idx = arr[0][0]
    idx_lst = [(0, 0)]
    for i in range(n):
        for j in range(n):
            if max_idx < arr[i][j]:
                max_idx = arr[i][j]
                idx_lst = [(i, j)]
            elif max_idx == arr[i][j]:
                idx_lst.append((i, j))
    for r, c in idx_lst:
        v = bfs(r, c)


    print('#{} {}'.format(tc, max_val))
