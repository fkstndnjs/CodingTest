def solution(genres, plays):
    answer = []        
    dic = dict()
    dic2 = dict()
    
    for i in range(len(genres)):
        if genres[i] not in dic:
            dic[genres[i]] = [(i, plays[i])]
            dic2[genres[i]] = plays[i]
        else:
            dic[genres[i]].append((i, plays[i]))
            dic2[genres[i]] += plays[i]
    
    for k, v in dic.items():
        v.sort(key = lambda x: (-x[1], x[0]))
        
    dic2 = sorted(list(dic2.items()), key=lambda x: -x[1])
    
    for d, _ in dic2:
        for i in range(min(2, len(dic[d]))):
            answer.append(dic[d][i][0])

    return answer
