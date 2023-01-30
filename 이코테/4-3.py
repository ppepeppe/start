dx = [-2, -1, 1, 2, 1, 2, -2, -1]
dy = [1, 2, 2, 1, -2, -1, -1, -2]

s = input()
x = int(s[1]) -1
y = int(ord(s[0])) - int(ord('a'))

cnt = 0
for i in range(8):
    nx = x + dx[i]
    ny = y + dy[i]
    if 0 <= nx < 8 and 0 <= ny < 8:
        cnt += 1
print(cnt)
