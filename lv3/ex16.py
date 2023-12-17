from collections import deque

def solution(n, roads, sources, destination):
    # 지도 정보를 그래프로 변환
    graph = {i: [] for i in range(1, n + 1)}
    for a, b in roads:
        graph[a].append(b)
        graph[b].append(a)
    
    # 목적지에서 시작하는 BFS로 최단 경로 계산
    def bfs(graph, destination):
        queue = deque([destination])
        visited = [-1] * (n + 1)
        visited[destination] = 0

        while queue:
            current = queue.popleft()
            for neighbor in graph[current]:
                if visited[neighbor] == -1:
                    visited[neighbor] = visited[current] + 1
                    queue.append(neighbor)

        return visited

    distances = bfs(graph, destination)
    return [distances[source] for source in sources]
