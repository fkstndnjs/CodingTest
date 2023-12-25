def solution(progresses, speeds):
    answer=[]
    
    for i, p in enumerate(progresses):
        for j in range(i, len(progresses)):
            progresses[j]+=max(0, (100-p))*speeds[j]
        
        cnt=1
        
        print(progresses)
        
        for k in range(i+1, len(progresses)):
            if progresses[k]>=100 and progresses[k-1]>100:
                cnt+=1
        
        print(cnt)
        
        answer.append(cnt)

    return answer
