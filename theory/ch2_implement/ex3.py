def solution(start="c2"):
    newStart=[ord(start[0])-ord('a'), int(start[1])-1]
    print(newStart)
    answer=0

    for i in [-2,2]:
        for j in [-1,1]:
            if 0 <= newStart[0]+i < 8 and 0 <= newStart[1]+j < 8:
                answer+=1

    for i in [-2,2]:
        for j in [-1,1]:
            if 0 <= newStart[1]+i < 8 and 0 <= newStart[0]+j < 8:
                answer+=1

    return answer

print(solution())