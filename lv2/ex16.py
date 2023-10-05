def solution(n):
    answer = 0
    binN=bin(n)[2:]
    temp=n+1
    binTemp=bin(temp)[2:]
    
    while binTemp.count('1')!=binN.count('1'):
        temp+=1
        binTemp=bin(temp)[2:]

    return temp