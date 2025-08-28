import heapq

def solution(scoville, K):
    heapq.heapify(scoville)
    answer = 0
    
    while scoville[0] < K:
        if len(scoville) <= 1:
            answer = -1
            break
        min1 = heapq.heappop(scoville)
        min2 = heapq.heappop(scoville)
        
        new = min1 + (min2 * 2)
        
        heapq.heappush(scoville, new)
        answer += 1
        
    return answer