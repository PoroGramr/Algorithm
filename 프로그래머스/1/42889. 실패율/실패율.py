def solution(N, stages):
    # 실패율
    dic = {}
    allPlayers = len(stages)
    for i in range(1, N + 1):
        notClearPlayer = stages.count(i)
        if allPlayers == 0 :
            failRate = 0
        else:
            failRate = notClearPlayer / allPlayers
        dic[i] = failRate
        
        allPlayers -= notClearPlayer
        
    # 실패율을 정렬
    dicSort = sorted(dic.items(), key = lambda x : x[1], reverse = True)
    
    #정렬된 실패율 반환
    result = []
    for i in range(len(dicSort)):
        result.append(dicSort[i][0])
    
    return result