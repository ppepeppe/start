dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

n = int(input())
arr =[list(input()) for _ in range(n)]

def find_heart(sx, sy):
    cnt = 0
    for i in range(4):
        nx = sx + dx[i]
        ny = sy + dy[i]
        if 0 <= nx < n and 0 <= ny < n and arr[nx][ny] == '*':
            cnt += 1
    if cnt != 4:
        return False
    else:
        return sx, sy

flag = 0
for i in range(n):
    for j in range(n):
        if find_heart(i, j):
            hx, hy = find_heart(i, j)
            flag = 1
            break
    if flag == 1:
        break
arm_cnt = 0
for i in range(n):
    if i == hy:
        l_arm = arm_cnt
        arm_cnt = 0
    elif arr[hx][i] == '*':
        arm_cnt += 1
r_arm = arm_cnt

middel = 0
for i in range(hx+1, n):
    if arr[i][hy] == '*':
        middel += 1
        middel_end_x = i
        middel_end_y =hy


l_foot = 0
r_foot = 0
for i in range(middel_end_x+1, n):
    if arr[i][middel_end_y-1] == '*':
        l_foot += 1
    if arr[i][middel_end_y+1] == '*':
        r_foot += 1
print(hx+1, hy+1)
print(l_arm, r_arm, middel, l_foot, r_foot)