def solution(n):
    answer = [i for i in list(range(1, n+1)) if i%2 != 0]
    return answer