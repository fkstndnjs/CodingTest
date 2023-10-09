import sys
input_file_path = "/Users/ysh/Documents/Git Repository/CodingTest/lv2/input.txt"
sys.stdin=open(input_file_path, "rt")

n, m = map(int, input().split())

list = [i for i in range(2, n+m+1)]

dic = dict(zip(list, [0]*len(list)))

for i in range(1, n+1):
    for j in range(1, m+1):
        dic[i+j]+=1

newLi = [k for k, v in dic.items() if v==max(dic.values())]

print(newLi)