from collections import deque

visited=[False]*9

def bfs(graph, start, visited):
    queue = deque([start])

    while queue:
        v = queue.popleft()

        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i]=True