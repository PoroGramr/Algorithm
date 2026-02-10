import sys

from collections import deque

input = sys.stdin.readline

N,M = map(int, input().split())

graph = [[] for _ in range(N + 1)]

for _ in range(M):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [-1 for _ in range(N + 1)]

count = 0

for i in range(1, N + 1):
    if visited[i] != -1:
        continue
    else:
        q = deque()
        q.append(i)
        count += 1
        
        while q:
            cur = q.popleft()
    
            for nxt in graph[cur]:
                if visited[nxt] == -1:
                    q.append(nxt)
                    visited[nxt] = 1


print(count)
            