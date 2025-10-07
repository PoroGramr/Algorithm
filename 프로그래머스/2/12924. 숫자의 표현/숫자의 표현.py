def solution(n):
    answer = 0
    
    for i in range(1, n+1):
        sumVal = 0
        for j in range(i, n + 1):
            sumVal += j
            
            if sumVal == n:
                answer += 1
            elif sumVal > n:
                break
    return answer
