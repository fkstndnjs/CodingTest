def solution(graph, n, visited):
    answer=""

    def dfs(graph, n, visited):
        if visited[n] == False:
            visited[n] = True
        answer+=str(visited(n))
        for i in graph[n]:
            dfs(graph, i, visited)