from collections import Counter

def solution(k, tangerine):
    answer = 0
    
    count = dict(Counter(tangerine))
    
    sortedCount = sorted(count.items(), key=lambda x:x[1])
    count=1
    
    while k>0:
        k-=sortedCount[count*-1][1]
        count+=1
        answer+=1
        
    return answer