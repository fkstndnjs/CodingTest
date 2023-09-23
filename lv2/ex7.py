def solution(s):
    answer = []
    zeroCount = 0
    count = 0
    
    while s!='1':
        zeroCount+=s.count('0')
        s=s.replace('0', '')
        s=bin(len(s))[2:]
        count+=1
    
    return [count, zeroCount]