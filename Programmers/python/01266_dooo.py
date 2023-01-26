def solution(genres, plays):
    answer = []
    dic = dict()
    for i in range(len(genres)):
        if genres[i] in dic.keys():
            dic[genres[i]][0] += plays[i]
            dic[genres[i]].append((plays[i],i))
        else:
            dic[genres[i]] = [plays[i], (plays[i], i)]
    lst = list(dic.values())
    lst.sort(reverse=True)
    for i in lst:
        music = i[1::]
        music.sort(key = lambda x:x[1])
        music.sort(reverse=True, key=lambda x: x[0])
        cnt = 0
        for k in music:
            cnt += 1
            if cnt == 3:
                break
            answer.append(k[1])
    return answer