import sys
input_file_path = "/Users/ysh/Documents/Git Repository/CodingTest/lv2/input.txt"
sys.stdin=open(input_file_path, "rt")
n, m = map(int, input().split())
a=list(map(int, input().split()))
# 입력값
# -----------------------------------------------------------------

a.sort()
lt=0
rt=n-1
while lt<=rt:
    mid = (lt+rt)//2
    if a[mid]==m:
        print(mid+1)
        break
    elif a[mid]>m:
        rt=mid-1
    else:
        lt=mid+1