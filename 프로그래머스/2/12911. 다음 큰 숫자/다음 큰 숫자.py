def solution(n):
    
    nxt = n + 1
    
    oriCount = bin(n)
    oriCount = str(oriCount[2:])
    
    oriCount = oriCount.count("1")
        
    answer = 0
    while True:
        nxtCount = bin(nxt)
        nxtCount = str(nxtCount[2:])
        
        nxtCount = nxtCount.count("1")
        
        if nxtCount == oriCount:
            answer = nxt
            break
        else:
            nxt += 1
            
        
    
    return answer