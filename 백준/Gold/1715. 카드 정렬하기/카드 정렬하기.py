import sys,heapq
input = sys.stdin.readline
heap = []

N = int(input())
for _ in range(N):
    heapq.heappush(heap, int(input()))

answer = 0

while len(heap) > 1:
    a = heapq.heappop(heap)
    b = heapq.heappop(heap)
    
    cost = a + b
    answer += cost
    heapq.heappush(heap,cost)
print(answer)
 
