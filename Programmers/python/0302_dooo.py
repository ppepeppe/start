from collections import deque


def solution(n, wires):
    answer = 100
    G = [[] for _ in range(n + 1)]
    for i in wires:
        G[i[0]].append(i[1])
        G[i[1]].append(i[0])

    def bfs(s):
        q = deque()
        q.append(s)
        cnt = 1
        v = [0] * (n + 1)
        v[s] = 1
        while q:
            c = q.popleft()
            for e in G[c]:
                if v[e] == 0:
                    q.append(e)
                    v[e] = 1
                    cnt += 1
        return cnt

    for i in wires:
        a = i[0]
        b = i[1]
        G[a].remove(b)
        G[b].remove(a)
        a_cnt = bfs(a)
        b_cnt = bfs(b)
        answer = min(abs(a_cnt - b_cnt), answer)
        G[a].append(b)
        G[b].append(a)

    return answer