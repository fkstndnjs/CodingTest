def solution(id_list, report, k):
    li = list(set(report))
    
    userCount = dict(zip(id_list, [0]*len(id_list)))
    reportCount = dict(zip(id_list, [0]*len(id_list)))
    reportList=[]
    
    for i in li:
        reportCount[i.split(' ')[1]]+=1
        
    for i, j in reportCount.items():
        if j>=k:
            reportList.append(i)
    
    for i in li:
        if i.split(' ')[1] in reportList:
            userCount[i.split(' ')[0]]+=1
    
    return list(userCount.values())