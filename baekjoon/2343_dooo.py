n,m = map(int,input().split())
lst = list(map(int,input().split()))


num = sum(lst)

start = 0
end = 10000000000
ans = num

while start<=end:

    mid = (start+end) // 2
    if mid < max(lst):
        start = mid + 1
        continue
    cnt = 1
    tmp = 0

    for i in range(len(lst)):
        if tmp + lst[i] <= mid:
            tmp += lst[i]
        else:
            tmp = lst[i]
            cnt += 1
    if cnt <= m:
        end = mid - 1
        ans = min(ans,mid)
    else:
        start = mid + 1
print(ans)
