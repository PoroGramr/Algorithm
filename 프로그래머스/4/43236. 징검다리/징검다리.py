def solution(distance, rocks, n):
    rocks.sort()
    rocks.append(distance)
    
    left = 1
    right = distance
    
    answer = 0
    
    while left <= right:
        mid = (left + right) // 2
        
        delete = 0
        prevRock = 0
        
        for rock in rocks:
            dist = rock - prevRock
            
            if dist < mid:
                delete += 1
                if delete > n:
                    break
            else:
                prevRock = rock
        if delete > n:
            right = mid - 1
        else:
            answer = mid
            left = mid + 1
    return answer