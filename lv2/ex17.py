import sys
input_file_path = "/Users/ysh/Documents/Git Repository/CodingTest/lv2/input.txt"
sys.stdin=open(input_file_path, "rt")
sys.setrecursionlimit(10**8)
input=sys.stdin.readline
dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]

def dfs(x, y):
    map_[x][y]=False

    for i in range(8):
        nx, ny = x+dx[i], y+dy[i]

        if map_[nx][ny]:
            dfs(nx, ny)

while True:
    cnt=0
    m, n = map(int, input().split())

    if m==0 and n==0:
        break

    map_ = [[False]*(m+10) for _ in range(n+10)]

    for i in range(1, n+1):
        tmp = list(map(int, input().split()))
        for j in range(1, m+1):
            map_[i][j] = tmp[j-1]==1

    for i in range(1, n+1):
        for j in range(1, m+1):
            if map_[i][j]:
                dfs(i,j)
                cnt+=1

    print(cnt)