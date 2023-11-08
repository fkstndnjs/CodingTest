from itertools import permutations

def isSo(n):
    count=0
    
    if n==1:
        return False
    
    for i in range(2, n+1):
        if n%i==0:
            count+=1
        if count>1:
            return False

    return True if count<2 else False

def solution(numbers):
    answer = 0
    
    for i in range(1, len(numbers)+1):
        for j in [i for i in set(list(permutations(numbers, i))) if i[0]!='0']:
            tmp=""
            for k in j:
                tmp+=k
            if isSo(int(tmp)):
                answer+=1
        
    return answer