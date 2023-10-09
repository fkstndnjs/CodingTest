import sys
input_file_path = "/Users/ysh/Documents/Git Repository/CodingTest/lv2/input.txt"
sys.stdin=open(input_file_path, "rt")

s = input()
res=0

for x in s:
    if x.isdigit():
        res=res*10+int(x)

cnt=0

for i in range(1, res+1):
    if res%i==0:
        cnt+=1

print(res, cnt)