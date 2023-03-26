# N, s = map(int, input().split())
# arr = list(map(int, input().split()))
# def sub(n, lst):
#     global cnt
#     if n == N:
#         if sum(lst) == s and len(lst) != 0:
#             cnt += 1
#         return
#     sub(n+1, lst + [arr[n]])
#     sub(n+1, lst)
#
#
# cnt = 0
# sub(0, [])
# print(cnt)


N, s = map(int, input().split())
arr = list(map(int, input().split()))

def sub(n, ssum, cnt):
    global ans
    if n == N:
        if cnt > 0 and ssum == s:
            ans += 1
        return

    sub(n+1, ssum + arr[n], cnt + 1)
    sub(n+1, ssum, cnt)
ans = 0
sub(0, 0, 0)
print(ans)