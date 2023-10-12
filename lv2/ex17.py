import sys
input_file_path = "/Users/ysh/Documents/Git Repository/CodingTest/lv2/input.txt"
sys.stdin=open(input_file_path, "rt")

N, M, R = map(int, sys.stdin.readline().split())

def dfs(idx):
    global count
    visited[idx]=True
    answer[idx]=count
    count+=1

    graph[idx].sort(reverse=True)
    for i in graph[idx]:
        if not visited[i]:
            dfs(i)


graph=[[] for _ in range(N+1)]
visited=[False]*(N+1)
answer=[0]*(N+1)
count=1

for _ in range(M):
    x, y = map(int, sys.stdin.readline().split())
    graph[x].append(y)
    graph[y].append(x)


dfs(R)

for i in range(1, N+1):
    print(answer[i])