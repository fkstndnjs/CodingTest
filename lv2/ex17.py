import sys
input_file_path = "/Users/ysh/Documents/Git Repository/CodingTest/lv2/input.txt"
sys.stdin=open(input_file_path, "rt")

n = int(input())
a = list(map(int, input().split()))

def digit_sum(x):
    sum=0

    while x>0:
        sum+=x%10
        x=x//10
    
    return sum

max=-2147000000

for x in a:
    tot=digit_sum(x)
    if tot>max:
        max=tot
        res=x

print(res)