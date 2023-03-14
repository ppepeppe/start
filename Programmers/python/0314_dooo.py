from itertools import combinations


def solution(orders, course):
    answer = []
    menu = []
    # for order in orders:
    #     for mu in order:
    #         if mu not in menu:
    #             menu.append(mu)
    # menu.sort()
    for c in course:
        ans = []
        for order in orders:
            for s in combinations(sorted(order), c):
                val = ''
                cnt = 0

                for k in s:
                    val += k
                for odr in orders:
                    n = len(val)
                    ncnt = 0
                    for i in val:
                        if i in odr:
                            ncnt += 1
                    if ncnt == n:
                        cnt += 1
                if cnt >= 2:
                    ans.append((val, cnt))
            ans.sort(key=lambda x: x[1], reverse=True)

        if ans:
            max_val = ans[0][1]
            for z in ans:
                if z[1] == max_val:
                    if z[0] not in answer:
                        answer.append(z[0])
    answer.sort()
    return answer