def solution(n, left, right):
    newLi=[]
    
    for i in range(left, right+1):
        x, y = divmod(i, n)
        newLi.append((x, y))
    
    answer = []
    for i in newLi:
        answer.append(max(i)+1)
    
    return answer