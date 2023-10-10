import sys
input_file_path = "/Users/ysh/Documents/Git Repository/CodingTest/lv2/input.txt"
sys.stdin=open(input_file_path, "rt")
n, e = map(int, input().split())

def dfs(idx):
    global graph, visited
    visited[idx]=True

    for i in range(1, n+1):
        if not visited[i] and graph[idx][i]:
            dfs(i)

graph=[[False]*(n+1) for _ in range(n+1)]
visited=[False]*(n+1)
cnt=0

for _ in range(e):
    x, y = map(int, input().split())
    graph[x][y]=True
    graph[y][x]=True

for i in range(1, n+1):
    if not visited[i]:
        dfs(i)
        cnt+=1

print(cnt)