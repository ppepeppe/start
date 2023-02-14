dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

TC = int(input())
for tc in range(1, TC+1):
    n = int(input())
    arr = []
    for _ in range(n):
        a, b, c, d = map(int, input().split())
        a*=2
        b*=2
        arr.append([b,a,c,d])
    ans = 0
    for _ in range(4002):
        mv_lst = []
        del_lst = []
        for lst in arr:
            lst[0] += dx[lst[2]]
            lst[1] += dy[lst[2]]
        dic = dict()


        ddel, v = set(), set()
        for i in range(len(arr)):
            cj, ci = arr[i][0], arr[i][1]
            if (cj, ci) in v:
                ddel.add((cj, ci))
            v.add((cj, ci))

        for i in range(len(arr)-1, -1, -1):
            if (arr[i][0], arr[i][1]) in ddel:
                ans += arr[i][3]
                arr.pop(i)
    print('#{} {}'.format(tc, ans))