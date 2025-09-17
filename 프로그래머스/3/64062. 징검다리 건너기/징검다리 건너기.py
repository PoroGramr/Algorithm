def can_cross(stones, k, people):
    cnt = 0
    for stone in stones:
        if stone - people <= 0:   # 이 돌을 건널 수 없음
            cnt += 1
            if cnt >= k:
                return False
        else:
            cnt = 0
    return True

def solution(stones, k):
    
    low = 0
    high = max(stones)
    
    answer = 0
    while low <= high:
        mid = (low + high) // 2

        if can_cross(stones, k, mid):
            answer = mid           
            low = mid + 1          
        else:
            high = mid - 1         

    return answer + 1