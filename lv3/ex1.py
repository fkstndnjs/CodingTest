def solution(n, computers):
    count=0
    def dfs(idx):
        visited[idx]=True
        
        for i in range(n):
            if not visited[i] and computers[idx][i]:
                dfs(i)
                
    visited=[False]*n
    
    for i in range(n):
        if not visited[i]:
            dfs(i)
            count+=1
    
    return count