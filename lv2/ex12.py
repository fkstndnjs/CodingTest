def solution(want, number, discount):
    answer=0
    
    dic = dict(zip(want, number))
    
    numLen = sum(number)
    
    i = 0
    
    while i < len(discount)-numLen+1:
        tmp = dic.copy()
        for r in range(i, i+numLen):
            if discount[r] in list(dic.keys()) and tmp[discount[r]]>0:
                tmp[discount[r]]-=1
        
        if not sum(list(tmp.values())):
            answer+=1
            
        i+=1
            
    return answer