import sys

dic = [[1, 1, 1, 0, 1, 1, 1], [0, 0, 1, 0, 0, 0, 1], [0, 1, 1, 1, 1, 1, 0], [0, 1, 1, 1, 0, 1, 1],
       [1, 0, 1, 1, 0, 0, 1], [1, 1, 0, 1, 0, 1, 1], [1, 1, 0, 1, 1, 1, 1], [1, 1, 1, 0, 0, 0, 1],
       [1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 0, 1, 1]]

TC = int(input())
for _ in range(TC):
    a, b = input().split()
    total = 0
    if len(a) == len(b):
        for i in range(len(a)):
            cnt = 0
            if a[i] != b[i]:

                for j in range(7):
                    if dic[int(a[i])][j] != dic[int(b[i])][j]:
                        cnt += 1
            total += cnt
    elif len(a) > len(b):
        minus = len(a) - len(b)
        for i in range(minus):
            for j in range(7):
                if dic[int(a[i])][j] == 1:
                    total += 1
        for i in range(len(b)):
            cnt = 0
            if a[minus + i] != b[i]:
                for j in range(7):
                    if dic[int(a[minus + i])][j] != dic[int(b[i])][j]:
                        cnt += 1
            total += cnt
    else:
        minus = len(b) - len(a)
        for i in range(minus):
            for j in range(7):
                if dic[int(b[i])][j] == 1:
                    total += 1
        for i in range(len(a)):
            cnt = 0
            if b[minus + i] != a[i]:
                pass
                for j in range(7):
                    if dic[int(b[minus + i])][j] != dic[int(a[i])][j]:
                        cnt += 1

            total += cnt
    print(total)