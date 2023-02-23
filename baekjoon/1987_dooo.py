
import sys
input = sys.stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

R, C = map(int, input().split())
arr = [list(input().strip()) for _ in range(R)]
answer = 1
def bfs(x, y):
    global answer
    q = set([(x, y, arr[x][y])])
    while q:
        x, y, ans = q.pop()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if ((0 <= nx < R) and (0 <= ny < C)) and (arr[nx][ny] not in ans):
                q.add((nx,ny,ans + arr[nx][ny]))
                answer = max(answer, len(ans)+1)

bfs(0, 0)
print(answer)