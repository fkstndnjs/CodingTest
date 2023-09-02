from collections import deque

def bfs(graph, start, visited):
    queue = deque([start])
    visited[next]=True

    while queue:
        next = queue.popleft()

        for i in graph[next]:
            if not visited[i]:
                queue.append(i)
                visited[next]=True