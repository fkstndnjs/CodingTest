import sys
input_file_path = "/Users/ysh/Documents/Git Repository/CodingTest/lv2/input.txt"
sys.stdin=open(input_file_path, "rt")
n, m = map(int, input().split())
li = [int(input()) for _ in range(n)]
# 입력값
# -----------------------------------------------------------------

li.sort()
lt, rt = 0, li[-1]

while lt<=rt:
    mid=(lt+rt)//2
    total=sum([l//mid for l in li])
    if total>=m:
        ans=mid
        lt=mid+1
    else:
        rt=mid-1

print(ans)