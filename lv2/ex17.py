import sys
from collections import deque
input_file_path = "/Users/ysh/Documents/Git Repository/CodingTest/lv2/input.txt"
sys.setrecursionlimit(10**5)
sys.stdin=open(input_file_path, "rt")
input=sys.stdin.readline

N, M, R = map(int, input().split())

def dfs(idx):
    global count
    visited[idx]=True
    print(idx, end=" ")

    graph[idx].sort()
    for i in graph[idx]:
        if not visited[i]:
            dfs(i)

def bfs(idx):
    queue=deque([idx])
    visited2[idx]=True

    while queue:
        v=queue.popleft()
        print(v, end=" ")

        for i in graph[v]:
            if not visited2[i]:
                queue.append(i)
                visited2[i]=True

graph=[[] for _ in range(N+1)]
visited=[False]*(N+1)
visited2=[False]*(N+1)

for _ in range(M):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)


dfs(R)
print()
bfs(R)