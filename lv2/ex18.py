import heapq as hq

def solution(operations):
    answer = []
    minQ = []
    maxQ = []
    
    for op in operations:
        command, num = op.split()
        if command=="I":
            hq.heappush(minQ, int(num))
            hq.heappush(maxQ, -int(num))
        elif command=="D" and minQ:
            if num=="1":
                hq.heappop(maxQ)     
                minQ = [-i for i in maxQ]
                hq.heapify(minQ)
            else:
                hq.heappop(minQ)
                maxQ = [-i for i in minQ]
                hq.heapify(maxQ)

    if minQ:
        answer.append(-hq.heappop(maxQ))
        answer.append(hq.heappop(minQ))
    else:
        answer.extend([0,0])
        
    return answer