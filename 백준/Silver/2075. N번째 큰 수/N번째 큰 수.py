import sys,heapq
input = sys.stdin.readline
heap = []

N = int(input())
for _ in range(N):
    tmp = list(map(int, input().split()))
    
    for t in tmp:
        if len(heap) <= N - 1:
            heapq.heappush(heap, t)
        else:
            if t > heap[0]:
                heapq.heappop(heap)
                heapq.heappush(heap,t)


answer = heap[0]
print(answer)
