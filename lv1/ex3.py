def getYaksuCount(n):
    count = 0
    
    i = 1
    while i * i <= n:
        if n % i == 0:
            if i == n // i:
                count += 1
            else:
                count += 2
        i += 1
        
    return count

def solution(number, limit, power):
    answer = 0
    
    for i in range(1, number + 1):
        yaksu_count = getYaksuCount(i)
        if yaksu_count > limit:
            answer += power
        else:
            answer += yaksu_count
            
    return answer
