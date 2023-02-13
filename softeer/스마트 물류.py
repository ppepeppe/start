n, k = map(int, input().split())

lst = list(input())

cnt = 0
for i in range(n):
    if lst[i] == 'P':
        flag = 0
        for s in range(i-k,i):
            if s < 0:
                continue
            if lst[s] == 'H':

                lst[s] = 'X'
                cnt += 1
                flag = 1
                break
        if flag == 0:
            for s in range(i+1, i+k+1):
                if s > n-1:
                    continue
                if lst[s] == 'H':
                    lst[s] = 'X'
                    cnt += 1
                    break
print(cnt)