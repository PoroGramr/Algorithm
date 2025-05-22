def solution(citations):
    citations.sort()
    print(citations)
    answer = 0
    
    for h in range(max(citations)):
        currentCount = 0
        for i in range(len(citations)):
            if citations[i] >= h:
                currentCount += 1
        
        if currentCount >= h:
            answer = h
            
    return answer