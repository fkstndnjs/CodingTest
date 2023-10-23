def solution(clothes):
    dic = {}
    
    for _, category in clothes:
        if category in dic:
            dic[category] += 1
        else:
            dic[category] = 1
    
    answer = 1
    for count in dic.values():
        answer *= (count + 1)  # 해당 종류의 의상을 입지 않는 경우도 고려 (+1)
    
    # 아무 의상도 입지 않는 경우를 빼줌
    return answer - 1