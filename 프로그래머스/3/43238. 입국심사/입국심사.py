# 모든 사람이 심사를 받는 데 걸리는 시간?

def solution(n, times):
    answer = 0
    left = 0
    right = max(times) * n
    
    while left <= right:
        mid = (left + right) // 2
        checked = 0
        for time in times:
            checked += mid // time 
        
            if checked >= n:
                break
        if checked >= n:
            answer = mid
            right = mid - 1
        else:
            left = mid + 1
        
    return answer