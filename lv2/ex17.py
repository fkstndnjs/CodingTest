import sys
input_file_path = "/Users/ysh/Documents/Git Repository/CodingTest/lv2/input.txt"
sys.stdin=open(input_file_path, "rt")
n=int(input())
li = [list(map(int, input().split())) for _ in range(n)]
# 입력값
# -----------------------------------------------------------------

cnt=0

for i in range(3):
    for j in range(7):
        tmp=li[j][i:i+5]
        if tmp==tmp[::-1]:
            print(tmp)
            cnt+=1

print(cnt)