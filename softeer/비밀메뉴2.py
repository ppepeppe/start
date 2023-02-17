n, m, k = map(int, input().split())

key = list(map(int, input().split()))
menu = list(map(int, input().split()))
#
# max_cnt = 0
# for i in range(m):
#     menu_idx = i
#     key_idx = 0
#     cnt = 0
#     while key_idx < n and menu_idx < m:
#         print(menu_idx, key_idx)
#         if menu[menu_idx] == key[key_idx]:
#             menu_idx += 1
#             key_idx += 1
#             cnt += 1
#         else:
#             if max_cnt < cnt:
#                 max_cnt = cnt
#             key_idx += 1
#             cnt = 0
#     if max_cnt < cnt:
#         max_cnt = cnt
# print(max_cnt)

max_cnt = 0
dp = [[0] * m for _ in range(n)]

for i in range(n):
    for j in range(m):
        if key[i] == menu[j]:
            if i == 0 or j == 0:
                dp[i][j] = 1
            else:
                dp[i][j] = dp[i-1][j-1] + 1

    if max_cnt < max(dp[i]):
        max_cnt = max(dp[i])
print(max_cnt)