def dfs(m, money):
    global min_val
    if m >= 13:
        if min_val > money:
            min_val = money
        return

    dfs(m+1, money + price[0] * month[m])
    dfs(m+1, money + price[1])
    dfs(m+3, money + price[2])

TC = int(input())
for tc in range(1, TC+1):
    price = list(map(int, input().split()))
    month = [0] + list(map(int, input().split()))
    min_val = price[3]
    dfs(1, 0)
    print('#{} {}'.format(tc, min_val))