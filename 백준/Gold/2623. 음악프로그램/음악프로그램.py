from collections import deque
import sys

input = sys.stdin.readline

N,M = map(int, input().split())

graph = [[] for _ in range(N + 1)]
indegree = [0 for _ in range(N + 1)]

for _ in range(M):
    
    data = list(map(int, input().split()))
    
    n = data[0]
    
    for i in range(1, n):
        graph[data[i]].append(data[i + 1])

        indegree[data[i + 1]] += 1

# print(graph)
# print(indegree)
q = deque()

for i in range(1, N + 1):
    if indegree[i] == 0:
        q.append(i)


result = []

while q:
    cur = q.popleft()
    result.append(cur)
    
    for nxt in graph[cur]:
        indegree[nxt] -= 1
        if indegree[nxt] == 0:
            q.append(nxt)


if len(result) == N:
    for s in result:
        print(s)
else:
    print(0)


    