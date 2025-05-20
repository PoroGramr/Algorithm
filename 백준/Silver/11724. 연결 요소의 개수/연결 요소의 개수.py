from collections import deque
import sys

input = sys.stdin.readline
N,M = map(int, input().split())

adj = [[] for _ in range(N)]

for _ in range(M):
  u,v = map(int, input().split())
  adj[u-1].append(v-1)
  adj[v-1].append(u-1)


visited = [False] * N
count = 0

for i in range(N):
  if visited[i]:
    continue
  else:

    count += 1

    queue = deque()
    queue.append(i)
    visited[i] = True

    while(queue):
      u = queue.popleft()

      for v in adj[u]:
        if not visited[v]:
          queue.append(v)
          visited[v] = True


print(count)
