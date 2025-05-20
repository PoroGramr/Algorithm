from collections import deque
import sys

input = sys.stdin.readline
N,M = map(int, input().split())

minKevinNum = 1e9
minNum = -1

adj = [[] for _ in range(N)]

for _ in range(M):
    a,b = map(int, input().split())

    adj[a-1].append(b-1)
    adj[b-1].append(a-1)

for i in range(N):
    visited = [False] * N
    dist = [-1] * N

    queue = deque([i])
    visited[i] = True
    dist[i] = 0

    while len(queue) != 0:
        u = queue.popleft()

        for v in adj[u]:
            if not visited[v]:
                queue.append(v)
                visited[v] = True
                dist[v] = dist[u] + 1
    kevinBacon = sum(dist)

    if minKevinNum > kevinBacon:
        minKevinNum = kevinBacon
        minNum = i 

print(minNum + 1)