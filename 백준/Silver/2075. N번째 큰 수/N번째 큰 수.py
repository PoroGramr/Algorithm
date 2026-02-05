import heapq


N = int(input())

q = []
for _ in range(N):
    nums = list(map(int, input().split()))
    for num in nums:
        if len(q) < N:
            heapq.heappush(q, num)
        
        else:
            if q[0] < num:
                heapq.heappop(q)
                heapq.heappush(q, num)

print(q[0])