"""
- newScov = mini + (min2 * 2)
- 모든 음식의 scov >= k 
- 몇 번이나 음식 조합을 반복해야할까

- 입력 : scoville 음식 리스트 / k 최소 스코빌지수
- 출력 : 모든 음식이 k 이상이 되기 위한 조합 횟수

반복 : 모든 음식이 k보다 클 때 까지
    - 음식 리스트를 정렬 -> min1, min2 찾기
    - min1 < k
    - newScov = mini + (min2 * 2)
    - newScv -> 음식 리스트
    
항상 정렬하는 대신 -> 음식 리스트르 heap으로 유지해서 min을 빠르게 찾아내자

종료 조건 : len(scoville) == 1
    => -1 출력

n : 1M -> 힙 써야함
"""

import heapq

def solution(scoville, K):

    heap = []
    for scov in scoville:
        heapq.heappush(heap, scov)
    
    # [1, 2, 3, 9, 10, 12]
    
    answer = 0
    
    while heap[0] < K:
        if len(heap) == 1:
            return -1
        
        min1 = heapq.heappop(heap)
        min2 = heapq.heappop(heap)
        
        new = min1 + (min2 * 2)
        
        heapq.heappush(heap, new)
        answer += 1
    
    
    return answer