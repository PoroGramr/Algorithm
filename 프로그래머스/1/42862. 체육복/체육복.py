def solution(n, lost, reserve):
    lost.sort()
    reserve.sort()
    answer = n - len(lost)
    for i in range(1, n+1):
        if i in lost and i in reserve:
            reserve.remove(i)
            lost.remove(i)
            answer += 1
    
    for i in lost:        
        if (i - 1) in reserve:
            reserve.remove(i-1)
            answer += 1
            continue
        elif (i + 1) in reserve:
            reserve.remove(i+1)
            answer += 1
        
    return answer