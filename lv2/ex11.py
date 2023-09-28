def solution(citations):
    answer = 0
    listAnswer = []
    setCitations = sorted(list(set(citations)),reverse=True)
    maxSet = max(setCitations)
    citations.sort(reverse=True)
    dictCitations = {x:0 for x in range(maxSet,-1,-1)}
    for i in citations:
        for l in dictCitations.keys():
            if l <= i:
                dictCitations[l] += 1
    for x, y in dictCitations.items():
        if x <= y:
            return x
    return answer