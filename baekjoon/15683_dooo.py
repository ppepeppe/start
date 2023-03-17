import copy


dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

cctv = []
mode = [[],
        [[0], [1], [2], [3]],
        [[0, 2], [1, 3]],
        [[0, 1], [1, 2], [2, 3], [0, 3]],
        [[0, 1, 2], [0, 1, 3], [1, 2, 3], [0, 2, 3]],
        [[0, 1, 2, 3]]]

n, m = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    for j in range(m):
        if 1 <= arr[i][j] <= 5:
            cctv.append((arr[i][j], i, j))

def check(board, lst, x, y):
    for i in lst:
        nx = x
        ny = y
        while True:
            nx += dx[i]
            ny += dy[i]

            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                break
            if board[nx][ny] == 6:
                break
            elif board[nx][ny] == 0:
                board[nx][ny] = 7

def dfs(depth, board):
    global min_val
    if depth == len(cctv):
        cnt = 0
        for i in range(n):
            for j in range(m):
                if board[i][j] == 0:
                    cnt += 1

        min_val = min(min_val, cnt)
        return
    n_arr = copy.deepcopy(board)
    num, x, y = cctv[depth]
    for k in mode[num]:
        check(n_arr, k, x, y)
        dfs(depth + 1, n_arr)
        n_arr = copy.deepcopy(board)

min_val = 1e9

dfs(0, arr)
print(min_val)