import sys
input_file_path = "/Users/ysh/Documents/Git Repository/CodingTest/lv2/input.txt"
sys.setrecursionlimit(10**5)
sys.stdin=open(input_file_path, "rt")
input=sys.stdin.readline

N = int(input())
X, Y = map(int, input().split())
M = int(input())

def dfs(idx, count):
    global answer
    visited[idx]=True

    if idx==Y:
        answer=count
        return
    
    for i in graph[idx]:
        if not visited[i]:
            dfs(i, count+1)

graph=[[] for _ in range(N+1)]
visited=[False]*(N+1)
answer=-1

for _ in range(M):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

dfs(X, 0)

print(answer)