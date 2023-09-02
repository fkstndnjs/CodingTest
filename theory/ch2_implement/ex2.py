def solution(n=5):
    clockStr=""
    answer=0

    for i in range(n+1):
        answer+=clockStr.count('3')
        for j in range(60):
            answer+=clockStr.count('3')
            for k in range(60):
                answer+= 1 if '3' in str(i)+str(j)+str(k) else 0

    return answer

print(solution())