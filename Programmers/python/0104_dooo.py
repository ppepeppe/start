def solution(phone_book):
    answer = True
    dic = dict()
    for i in phone_book:
        dic[i] = 0
    for j in phone_book:
        se = ''
        for k in j:
            se += k
            if se in dic and se != j:
                answer= False
    return answer