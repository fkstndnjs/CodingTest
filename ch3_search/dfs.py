def dfs(graph, n, visited):
    visited[n] = True

    for i in graph[n]:
        if not visited[i]:
            dfs(graph, i, visited)