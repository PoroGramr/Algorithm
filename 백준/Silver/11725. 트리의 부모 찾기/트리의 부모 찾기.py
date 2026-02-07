from collections import deque

N = int(input())

graph = [[] for _ in range(N + 1)]

for _ in range(N - 1):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (N + 1)
parent = [0 for _ in range(N + 1)]

q = deque()
q.append(1)


while q:
    cur = q.popleft()
    visited[cur] = True
    
    for nxt in graph[cur]:
        if visited[nxt] == False:
            parent[nxt] = cur
            
            q.append(nxt)
            visited[nxt] = True
    


for i in range(2, N + 1):
    print(parent[i])