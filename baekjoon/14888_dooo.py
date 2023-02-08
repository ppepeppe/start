n = int(input())

number = list(map(int, input().split()))
lst = list(map(int, input().split()))

max_val = -1e9
min_val = 1e9

val = number[0]
def dfs(val, p, m, t, d, k):
    global max_val, min_val


    if p > lst[0] or m > lst[1] or t > lst[2] or d > lst[3]:
        return

    if k == n:

        if max_val < val:
            max_val = val
        if min_val > val:
            min_val = val
        return


    dfs(val+number[k], p+1, m, t, d, k+1)
    dfs(val-number[k], p, m+1, t, d, k+1)
    dfs(val*number[k], p, m, t+1, d, k+1)
    if val <= 0:

        dfs((abs(val)//number[k])*-1, p, m, t, d+1, k+1)
    else:
        dfs(val//number[k], p, m ,t ,d+1, k+1)

dfs(val, 0, 0, 0, 0, 1)
print(max_val)
print(min_val)


# # 백트래킹 (Python3 통과, PyPy3도 통과)
# import sys
#
# input = sys.stdin.readline
# N = int(input())
# num = list(map(int, input().split()))
# op = list(map(int, input().split()))  # +, -, *, //
#
# maximum = -1e9
# minimum = 1e9
#
#
# def dfs(depth, total, plus, minus, multiply, divide):
#     global maximum, minimum
#     if depth == N:
#         maximum = max(total, maximum)
#         minimum = min(total, minimum)
#         return
#
#     if plus:
#         dfs(depth + 1, total + num[depth], plus - 1, minus, multiply, divide)
#     if minus:
#         dfs(depth + 1, total - num[depth], plus, minus - 1, multiply, divide)
#     if multiply:
#         dfs(depth + 1, total * num[depth], plus, minus, multiply - 1, divide)
#     if divide:
#         dfs(depth + 1, int(total / num[depth]), plus, minus, multiply, divide - 1)
#
#
# dfs(1, num[0], op[0], op[1], op[2], op[3])
# print(maximum)
# print(minimum)