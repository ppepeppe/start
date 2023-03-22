def solution(N, stages):
    answer = []
    cnt = [0] * (N + 2)
    for stage in stages:
        cnt[stage] += 1

    for i in range(1, N + 1):
        total = 0
        for j in range(i, N + 2):
            total += cnt[j]
        if total == 0:
            answer.append((i, 0))
        else:
            answer.append((i, cnt[i] / total))
    answer.sort()

    answer.sort(key=lambda x: x[1], reverse=True)
    ans = []
    for i in answer:
        ans.append(i[0])
    return ans