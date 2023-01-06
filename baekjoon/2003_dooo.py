n, m = map(int, input().split())

lst = list(map(int, input().split()))

cnt = 0
for i in range(n):
    num = lst[i]
    if num == m:
        cnt += 1
    else:
        for j in range(i+1, n):
            num += lst[j]
            if num == m:
                cnt += 1
                break
print(cnt)
