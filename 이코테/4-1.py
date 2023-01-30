dx = [-1 , 1, 0, 0]
dy = [0, 0, -1, 1]
move = ['U', 'D', 'L', 'R']

n = int(input())
lst = list(input().split())

x, y = 0, 0

for mv in lst:
    for i in range(4):
        if mv == move[i]:
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                x = nx
                y = ny

print(x+1, y+1)