import sys
import heapq

input = sys.stdin.readline
INF = 10 ** 18


V, E = map(int, input().split())
K = int(input())

graph = [[]for _ in range(V + 1)]
for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v,w))

dist = [INF] * (V + 1)
dist[K] = 0

pq = []
heapq.heappush(pq, (0,K))

while pq:
    cur_dist, u = heapq.heappop(pq)
    
    if cur_dist != dist[u]:
        continue

    for v, w in graph[u]:
        nd = cur_dist + w
        if nd < dist[v]:
            dist[v] = nd
            heapq.heappush(pq, (nd,v))
        

out = []
for i in range(1, V + 1):
    out.append("INF" if dist[i] == INF else str(dist[i]))
print("\n".join(out))