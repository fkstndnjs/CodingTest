import sys
input_file_path = "/Users/ysh/Documents/Git Repository/CodingTest/lv2/input.txt"
sys.stdin=open(input_file_path, "rt")
T=int(input())

for t in range(T):
    n,s,e,k=map(int, input().split())
    a=list(map(int, input().split()))
    newA = a[s-1:e]
    newA.sort()
    print("#%d %d" %(t+1, newA[k-1]))
