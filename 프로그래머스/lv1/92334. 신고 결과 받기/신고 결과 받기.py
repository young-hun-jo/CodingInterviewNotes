def solution(id_list, report, k):
    count = {}   
    history = {}  
    for user in id_list:
        count[user] = 0
        history[user] = set()
    
    for content in report:
        reporter, reportee = content.split(" ")
        if reportee in history[reporter]:
            continue
        else:
            count[reportee] += 1
            history[reporter].add(reportee)
    stop_users = set(name for name, cnt in count.items() if cnt >= k)
    answer = [0] * len(id_list)
    for i in range(len(id_list)):
        reportees: set = history[id_list[i]]
        temp = stop_users & reportees
        answer[i] = len(temp)
    return answer
        
                
    