def solution(name, yearning, photo):
    dic = dict(zip(name, yearning))
    answer = []
    # max : 100 x 100 = 10000
    for p in photo: # p: List[str]
        score = 0
        for person in p:
            if person in dic.keys():
                score += dic[person]
            else:
                continue
        answer.append(score)
    return answer
            
        