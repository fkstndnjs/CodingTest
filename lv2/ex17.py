import sys
input_file_path = "/Users/ysh/Documents/Git Repository/CodingTest/lv2/input.txt"
sys.stdin=open(input_file_path, "rt")

n = int(input())

for i in range(n):
    s=input()
    s=s.upper()
    size=len(s)

    for j in range(size//2):
        if s[j]!=s[-1-j]:
            print("#%d NO" %(i+1))
            break

    else:
        print("#%d YES" %(i+1))