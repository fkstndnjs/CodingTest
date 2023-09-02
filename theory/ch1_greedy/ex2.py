n=5
m=8
k=3

nLi = [2,4,5,4,6]
counter=""
answer=0

for i in range(m):
    newLi = nLi[0:]
    if counter.count(str(max(nLi))) < nLi.count(max(nLi))*k:
        answer+=max(nLi)
        counter+=str(max(nLi))
    else:
        newLi.remove(max(nLi))
        answer+=max(newLi)
        counter=""

print(answer)