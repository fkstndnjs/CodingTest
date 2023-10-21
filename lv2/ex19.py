def solution(tickets):
    answer = []
    tLen = len(tickets)

    def dfs(idx, visited, s):
        nonlocal answer
        visited[idx] = True
        s.append(tickets[idx][1])
        
        if all(visited):
            answer.append(s[:])
        
        for i in range(tLen):
            if not visited[i] and tickets[idx][1] == tickets[i][0]:
                dfs(i, visited[:], s[:])

    for i in range(tLen):
        if tickets[i][0] == "ICN":
            dfs(i, [False] * tLen, ["ICN"])

    answer.sort()
    return answer[0]
