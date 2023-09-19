def solution(n):
    answer = 0
    for i in range(1, n + 1):
        temp_sum = 0
        j = i
        while temp_sum < n:
            temp_sum += j
            j += 1
        if temp_sum == n:
            answer += 1
    return answer