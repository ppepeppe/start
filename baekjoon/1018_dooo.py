import copy

n, m = map(int, input().split())

arr = [list(input()) for _ in range(n)]
min_cnt = 1e9
for i in range(n-8+1):
    for j in range(m-8+1):

        new_arr_lst = [[] for _ in range(8)]
        for k in range(8):
            new_arr_lst[k] = arr[i+k][j:j+8]

        for time in range(2):
            new_arr = copy.deepcopy(new_arr_lst)
            if time == 0:
                cnt = 0
            else:
                if new_arr[0][0] == 'B':
                    new_arr[0][0] = 'W'
                else:
                    new_arr[0][0] = 'B'
                cnt = 1

            for r in range(8):
                for c in range(8):

                    if r == 0 and c == 0:
                        continue
                    elif c != 0:
                        if new_arr[r][c-1] == new_arr[r][c]:
                            cnt += 1
                            if new_arr[r][c] == 'B':
                                new_arr[r][c] = 'W'
                            else:
                                new_arr[r][c] = 'B'
                    elif r != 0 and c== 0:
                        if new_arr[r-1][c] == new_arr[r][c]:
                            cnt += 1
                            if new_arr[r][c] == 'B':
                                new_arr[r][c] = 'W'
                            else:
                                new_arr[r][c] = 'B'


            if min_cnt > cnt:
                min_cnt = cnt

print(min_cnt)