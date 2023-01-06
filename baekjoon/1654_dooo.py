n, k = map(int, input().split())
lst = []
for _ in range(n):
    lst.append(int(input()))

start = 0
end = max(lst)
while start <= end:
    middle = (start+end)//2
    if middle == 0:
        break
    cnt = 0
    for i in lst:
        cnt += i//middle
    if cnt >= k:
        start = middle+1
    else:
        end = middle - 1
print(end)
