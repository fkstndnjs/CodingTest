n=25
k=5
count=0

while n!=1:
    n = n//5 if n%k==0 else 1
    count+=1

print(count)