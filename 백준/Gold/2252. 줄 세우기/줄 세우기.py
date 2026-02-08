from collections import deque
import sys

input = sys.stdin.readline

N,M = map(int, input().split())

graph = [[] for _ in range(N + 1)]
indegree = [0 for _ in range(N + 1)]

for _ in range(M):
    A,B = map(int, input().split())
    graph[A].append(B)
    indegree[B] += 1


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


print(*result)
    