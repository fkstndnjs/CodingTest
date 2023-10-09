import sys
input_file_path = "/Users/ysh/Documents/Git Repository/CodingTest/lv2/input.txt"
sys.stdin=open(input_file_path, "rt")

n=int(input())
li = [list(map(int, input().split())) for _ in range(n)]

largest=0

for i in range(n):
    sum1=sum2=sum3=sum4=0

    for j in range(n):
        sum1+=li[i][j]
        sum2+=li[j][i]
        
    sum3+=li[i][i]
    sum4+=li[i][n-i-1]

    largest = max(largest, sum1, sum2, sum3, sum4)

print(largest)