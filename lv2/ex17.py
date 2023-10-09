import sys
input_file_path = "/Users/ysh/Documents/Git Repository/CodingTest/lv2/input.txt"
sys.stdin=open(input_file_path, "rt")

n=int(input())
li = [list(map(int, input().split())) for _ in range(n)]

res=0
s=e=n//2

for i in range(n):
    for j in range(s, e+1):
        res+=li[i][j]

    if i<n//2:
        s-=1
        e+=1
    else:
        s+=1
        e-=1

print(res)