def solution(n, results):
    answer = 0
    G = [[0] * n for _ in range(n)]
    for lst in results:
        G[lst[0]-1][lst[1]-1] = 1
    for k in range(n):
        for a in range(n):
            for b in range(n):
                if G[a][b] == 0 and G[a][k] and G[k][b]:
                    G[a][b] = 1
    for i in range(n):
        total = 0
        for j in range(n):
            total += G[i][j] + G[j][i]
        if total == n-1:
            answer += 1
    return answer