def check(stones, k, mid):
    cnt = 0
    for stone in stones:
        if stone < mid:
            cnt += 1
            if cnt >= k:
                return False
        else:
            cnt = 0
    return True

def solution(stones, k):
    left, right = 1, max(stones) + 1
    
    while left < right:
        mid = (left + right) // 2
        if check(stones, k, mid):
            left = mid + 1
        else:
            right = mid
            
    return left - 1
