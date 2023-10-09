import sys
input_file_path = "/Users/ysh/Documents/Git Repository/CodingTest/lv2/input.txt"
sys.stdin=open(input_file_path, "rt")

n = int(input())
a=list(map(int, input().split()))

sum=0
cnt=0

for x in a:
    if x==1:
        cnt+=1
        sum+=cnt
    else:
        cnt=0

print(sum)