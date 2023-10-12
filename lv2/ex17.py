import sys
input_file_path = "/Users/ysh/Documents/Git Repository/CodingTest/lv2/input.txt"
sys.stdin=open(input_file_path, "rt")

N, M, R = map(int, input().split())

def dfs(idx):
    global visited, graph, answer, order
    visited[idx] = True
    answer[idx] = order
    order += 1

    for i in graph[idx]:  # 인접한 노드들을 순회합니다.
        if not visited[i]:  # 방문하지 않은 노드인 경우에만 재귀 호출합니다.
            dfs(i)

graph = [[] for _ in range(N+1)]
visited = [False]*(N+1)
answer = [0]*(N+1)
order=1

for _ in range(M):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

for i in range(1, N+1):
    graph[i] = sorted(graph[i])

dfs(R)

for i in range(1, N+1):
    print(answer[i])