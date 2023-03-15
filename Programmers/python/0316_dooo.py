def solution(record):
    answer = []
    dic = dict()
    for i in record:
        lst = i.split(' ')
        if lst[0] == 'Enter':
            dic[lst[1]] = lst[2]
            answer.append((lst[1], 0))
        elif lst[0] == 'Change':
            dic[lst[1]] = lst[2]
        else:
            answer.append((lst[1], 1))
    result = []
    for lst in answer:
        val = dic[lst[0]]
        if lst[1] == 0:
            val += '님이 들어왔습니다.'
            result.append(val)
        else:
            val += '님이 나갔습니다.'
            result.append(val)
    return result