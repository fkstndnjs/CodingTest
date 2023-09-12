def solution(lottos, win_nums):
    winTable = {6: 1, 5: 2, 4: 3, 3: 4, 2: 5, 1: 6, 0: 6}
    answer = []
    sortedLottos = sorted(lottos)
    zeroCount=lottos.count(0)
    
    li = list(set(lottos)&set(win_nums))
    
    answer = [winTable[len(li)+zeroCount],winTable[len(li)]]
    
    return answer