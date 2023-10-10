import sys
input_file_path = "/Users/ysh/Documents/Git Repository/CodingTest/lv2/input.txt"
sys.stdin=open(input_file_path, "rt")
dx=[-1, 0, 1, 0]
dy=[0,1,0,-1]
n=int(input())
li = [list(map(int, input().split())) for _ in range(n)]
li.insert(0, [0]*n)
li.append([0]*n)
for l in li:
    l.insert(0, 0)
    l.append(0)

cnt=0

for i in range(1, n+1):
    for j in range(1, n+1):
        if all(li[i][j] > li[i+dx[k]][j+dy[k]] for k in range(4)):
            cnt+=1

print(cnt)