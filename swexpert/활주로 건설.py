TC = int(input())

for tc in range(1, TC+1):

    n, k = map(int, input().split())

    arr = [list(map(int, input().split())) for _ in range(n)]


    no = 0
    for j in range(n):
        std = arr[0][j]
        flag = 0
        cnt = 1
        for i in range(1, n):
            if abs(arr[i][j] - std) > 1:
                no += 1
                break
            if std == arr[i][j]:
                cnt += 1
                if flag == 1:
                    if cnt == k:
                        flag = 0
                        cnt = 0
            elif std > arr[i][j]:
                if flag == 0:
                    cnt = 1
                    flag = 1
                    std =arr[i][j]
                else:
                    if cnt < k:
                        no += 1


                        break
            else:
                if flag == 0:
                    if cnt < k :
                        no+=1


                        break
                else:
                    if cnt< k:
                        no+= 1
                        break
                cnt = 1
                std = arr[i][j]
        else:
            if flag == 1 and cnt < k:
                no+=1

    for i in range(n):
        std = arr[i][0]
        flag = 0
        cnt = 1
        for j in range(1, n):
            if abs(arr[i][j] - std) > 1:
                no += 1


                break
            if std == arr[i][j]:
                cnt += 1
                if flag == 1:
                    if cnt == k:
                        flag = 0
                        cnt = 0
            elif std > arr[i][j]:
                if flag == 0:
                    cnt = 1
                    flag = 1
                    std = arr[i][j]
                else:
                    if cnt < k:
                        no += 1


                        break
            else:
                if flag == 0:
                    if cnt < k:
                        no += 1


                        break
                else:
                    if cnt < k:
                        no += 1
                        break
                cnt = 1
                std = arr[i][j]
        else:
            if flag == 1 and cnt < k:
                no += 1


    print('#{} {}'.format(tc, 2*n - no))