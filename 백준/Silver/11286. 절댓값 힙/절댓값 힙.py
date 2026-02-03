import heapq

heap = []

N = int(input())

for _ in range(N):
    num = int(input())
    
    if num != 0:
        heapq.heappush(heap,(abs(num), num))
    else:
        if heap:
            ans = heapq.heappop(heap)
            print(ans[1])
        else:
            print(0)
