import sys
input_file_path = "/Users/ysh/Documents/Git Repository/CodingTest/lv2/input.txt"
sys.stdin=open(input_file_path, "rt")
sys.setrecursionlimit(10**8)
input=sys.stdin.readline

dx=[-1, 1, 0,0]
dy=[0,0,-1,1]
MAX=1000+10
M, N = map(int, input().split())

def dfs(x, y):
    global answer, M
    visited[x][y]=True

    if x==M:
        answer="YES"
        return

    for i in range(4):
        newX = x+dx[i]
        newY = y+dy[i]

        if map_[newX][newY] and not visited[newX][newY]:
            dfs(newX, newY)


map_ = [[False]*MAX for _ in range(MAX)]
visited = [[False]*MAX for _ in range(MAX)]
answer="NO"

for i in range(1, M+1):
    p = input().strip()
    for j in range(1, N+1):
        map_[i][j] = p[j-1]=='0'


for k in range(1, N+1):
    if map_[1][k]:
        dfs(1, k)

print(answer)