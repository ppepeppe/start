n, k = map(int, input().split())

a_lst = list(map(int, input().split()))
b_lst = list(map(int, input().split()))

a_lst.sort()
b_lst.sort(reverse=True)
cnt = 0

for i in range(n):
    if a_lst[i] < b_lst[i]:
        a_lst[i], b_lst[i] = b_lst[i], a_lst[i]
        cnt += 1
    else:
        break
    if cnt == k:
        break
print(sum(a_lst))