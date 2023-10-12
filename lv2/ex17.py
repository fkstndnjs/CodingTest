import sys
input_file_path = "/Users/ysh/Documents/Git Repository/CodingTest/lv2/input.txt"
sys.setrecursionlimit(10**5)
sys.stdin=open(input_file_path, "rt")
input=sys.stdin.readline

N = int(input())

def dfs(idx):
    global answer
    visited[idx]=True

    for i in graph[idx]:
        if not visited[i]:
            answer[i]=idx
            dfs(i)

graph=[[] for _ in range(N+1)]
visited=[False]*(N+1)
answer=[0]*(N+1)

for _ in range(N-1):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

dfs(1)

for i in range(2, N+1):
    print(answer[i])