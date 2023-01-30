n, m, k = map(int, input().split())

lst = list(map(int, input().split()))

lst.sort()

first = lst[n-1]
second = lst[n-2]
cnt = 0
total = 0
while True:
    for _ in range(k):
        if cnt == m:
            break
        total += first
        cnt += 1
    if cnt == m:
        break
    total += second
    cnt += 1
print(total)