import heapq

def solution(n, works):
    answer = 0
    
    # 최대 힙으로 변환
    works = [-work for work in works]
    heapq.heapify(works)
    
    # N시간 동안 야근을 하면서 작업량을 최소화
    for _ in range(n):
        if works:
            max_work = -heapq.heappop(works)  # 가장 많은 작업량을 가진 작업을 꺼냄
            if max_work > 1:
                heapq.heappush(works, -(max_work - 1))  # 작업량을 1 줄인 후 다시 힙에 추가
    
    # 야근 피로도 계산
    for work in works:
        answer += work ** 2
    
    return answer