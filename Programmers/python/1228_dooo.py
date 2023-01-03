def solution(operations):
    q = []
    for i in operations:
        if i[0] == 'I':
            q.append(int(i[2:len(i)+1]))
        else:
            if q:
                if '-' in i:
                    q.pop(q.index(min(q)))
                else:
                    q.pop(q.index(max(q)))
            else:
                continue
    if q:
        return [max(q), min(q)]
    else:
        return [0,0]