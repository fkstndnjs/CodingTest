def solution(n=5, li=['R','R','R','U','D','D']):
    direction = {'R':[0,1],'L':[0,-1],'D':[1,0],'U':[-1,0]}
    answer=[0,0]

    for i in li:
        if 0 <= answer[0]+direction[i][0] < n and answer[1]+direction[i][1] >= 0 and answer[1]+direction[i][1] < n:
            answer[0]+=direction[i][0]
            answer[1]+=direction[i][1]

    return [i+1 for i in answer]

print(solution())
