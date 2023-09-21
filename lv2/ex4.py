def solution(A,B):
    answer = 0

    A.sort()
    B.sort(reverse=True)    
    
    print(A, B)
    
    for i, a in enumerate(A):
        answer+=a*B[i]

    return answer