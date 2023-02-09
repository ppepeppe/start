from collections import deque

dx = [0, -1, 0, 1, 0]
dy = [0, 0, 1, 0, -1]

def bbfs(sy, sx, k, d):
    q = deque()
    q.append((sx, sy))
    v[sx][sy][0] = 1
    v[sx][sy][1].append(k)
    while q:
        cx, cy = q.popleft()

        if v[cx][cy][0] == d:
            return

        for i in range(1, 5):
            nx = cx + dx[i]
            ny = cy + dy[i]

            if 0 <= nx < 10 and 0 <= ny < 10 and v[nx][ny][0] == 0:
                q.append((nx, ny))
                v[nx][ny][1].append(k)
                v[nx][ny][0] = v[cx][cy][0] + 1



TC = int(input())
for tc in range(1, TC+1):
    t, m = map(int, input().split())

    a_move = list(map(int, input().split()))
    b_move = list(map(int, input().split()))
    a_move = [0] + a_move
    b_move = [0] + b_move
    battery = []
    for _ in range(m):
        battery.append(list(map(int, input().split())))
    v = [[[0, []] for _ in range(10)] for _ in range(10)]

    for i in range(len(battery)):
        bbfs(battery[i][0]-1, battery[i][1]-1, i+1, battery[i][2]+1)
        for i in v:
            for j in range(len(i)):
                i[j][0] = 0

    ax = 0
    ay = 0
    bx = 9
    by = 9
    assum = 0
    bssum = 0
    for i in range(t+1):
        ax += dx[a_move[i]]
        ay += dy[a_move[i]]
        bx += dx[b_move[i]]
        by += dy[b_move[i]]
        flag = 0
        if v[ax][ay][1] and v[bx][by][1]:
            for x in v[ax][ay][1]:
                if x in v[bx][by][1]:
                    flag= 1
                    break
        asum = 0
        bsum = 0
        max_asum = 0

        max_bsum = 0
        asum_lst = []
        bsum_lst = []
        if flag == 1:
            # print(ax, ay, bx, by)
            # for x in v[ax][ay][1]:
            #     asum_lst.append(battery[x-1][3])
            # for x in v[bx][by][1]:
            #     bsum_lst.append(battery[x-1][3])
            both = 0
            for i in range(len(v[ax][ay][1])):
                for j in range(len(v[bx][by][1])):

                    if v[ax][ay][1][i] == v[bx][by][1][j]:
                        asum = battery[v[ax][ay][1][i]-1][3]//2
                        bsum = battery[v[bx][by][1][j]-1][3]//2

                    else:
                        asum = battery[v[ax][ay][1][i] - 1][3]
                        bsum = battery[v[bx][by][1][j] - 1][3]
                    if max_asum + max_bsum < asum + bsum:
                        max_asum = asum
                        max_bsum = bsum

        else:

            for i in range(len(v[ax][ay][1])):
                if max_asum < battery[v[ax][ay][1][i]-1][3]:
                    max_asum = battery[v[ax][ay][1][i]-1][3]
            for j in range(len(v[bx][by][1])):
                if max_bsum < battery[v[bx][by][1][j] - 1][3]:
                    max_bsum = battery[v[bx][by][1][j] - 1][3]

        assum += max_asum
        bssum += max_bsum

    print('#{} {}'.format(tc, assum+bssum))

