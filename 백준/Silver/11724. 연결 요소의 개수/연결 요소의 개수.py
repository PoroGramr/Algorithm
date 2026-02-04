from collections import deque
import sys
input = sys.stdin.readline

N,M = map(int, input().split())

graph = [[] for _ in range(N + 1)] 


visited = [-1 for _ in range(N + 1)]

for _ in range(M):
    a,b = map(int, input().split())
    
    graph[a].append(b)
    graph[b].append(a)

count  = 0

for i in range(1, N + 1):
    if visited[i] != -1:
        continue
    
    else:
        count += 1
        
        q = deque()
        q.append(i)
        visited[i] = 1
        
        while q:
            c = q.popleft()
            
            for v in graph[c]:
                if visited[v] == -1:
                    q.append(v)
                    visited[v] = 1

print(count)