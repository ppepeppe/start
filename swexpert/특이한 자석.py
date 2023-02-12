TC = int(input())
for tc in range(1, TC+1):

    k = int(input())

    arr = [list(map(int, input().split())) for _ in range(4)]
    arr = [[0]] + arr

    for _ in range(k):
        a, b = map(int, input().split())
        lst= [(a, b)]
        s = b
        for i in range(a, 1,-1):
            if arr[i][6] != arr[i-1][2]:
                lst.append((i-1, s*(-1)))
                s *= -1
            else:
                break
        s = b

        for i in range(a,4):
            if arr[i][2] != arr[i+1][6]:
                lst.append((i+1,s*(-1)))
                s*=-1
            else:
                break
        for i in lst:
            if i[1] == 1:
                new_arr = [arr[i[0]][-1]]
                for k in range(7):
                    new_arr.append(arr[i[0]][k])
            else:
                new_arr = []
                for k in range(1,8):
                    new_arr.append(arr[i[0]][k])
                new_arr.append(arr[i[0]][0])
            arr[i[0]] = new_arr
    ans = 0
    for i in range(1, 5):
        if arr[i][0] == 1:
            ans += 2**(i-1)
    print('#{} {}'.format(tc, ans))


