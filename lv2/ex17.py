import sys
input_file_path = "/Users/ysh/Documents/Git Repository/CodingTest/lv2/input.txt"
sys.stdin=open(input_file_path, "rt")

n = int(input())
arr=list(map(int, input().split()))

avg=round(sum(arr)/n)
min=2147000000

for i, a in enumerate(arr):
    tmp=abs(a-avg)

    if tmp<min:
        min=tmp
        score=a
        idx=i+1
        
    elif tmp==min:
        if a>score:
            score=a
            idx=i+1

print(avg, idx)