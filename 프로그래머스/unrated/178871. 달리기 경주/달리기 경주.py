def solution(players, callings):
    dic = dict(zip(players, [i for i in range(len(players))]))
    
    for now in callings:
        now_idx: int = dic[now]
        front: str = players[now_idx-1]
        # 순서 switch
        players[now_idx-1] = now
        players[now_idx] = front
        # dic에서 인덱스 갱신
        dic[now] -= 1
        dic[front] += 1
    return players