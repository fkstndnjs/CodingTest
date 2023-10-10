import sys
input_file_path = "/Users/ysh/Documents/Git Repository/CodingTest/lv2/input.txt"
sys.stdin=open(input_file_path, "rt")

def dfs(idx):
    global visited, graph, answer
    visited[idx]=True
    answer+=1

    for i in range(1, n+1):
        if not visited[i] and graph[idx][i]:
            dfs(i)

n = int(input())  # 노드의 개수
m = int(input())  # 간선의 개수

graph = [[False]*(n+1) for _ in range(n+1)]
visited = [False]*(n+1)
answer=0

for _ in range(m):
    i, j = map(int, input().split())
    graph[i][j] = True
    graph[j][i] = True

dfs(1)

print(answer-1)