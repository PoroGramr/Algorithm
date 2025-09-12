import heapq

def solution(n, works):
    answer = 0
    
    heap = [-w for w in works]
    
    heapq.heapify(heap)
    
    
    for _ in range(n):
        large = - heapq.heappop(heap)
        large -= 1
        heapq.heappush(heap,-large)
        
    ori = [-w for w in heap]

    if max(ori) <= 0:
        return 0
    
    for i in heap:
        tmp = -i * -i
        answer += tmp
    return answer