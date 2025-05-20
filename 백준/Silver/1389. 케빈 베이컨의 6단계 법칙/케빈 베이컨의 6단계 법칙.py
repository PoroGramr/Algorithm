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


for i in range(len(adj)):
    dict = [[] for _ in range(len(adj))]
    dict[i] = 0

    visited = [False] * N

    queue = deque([i])
    visited[i] = True

    while queue:
        current = queue.popleft()
        for n in adj[current]:
            if not visited[n]:
                visited[n] = True
                dict[n] = dict[current] + 1
                queue.append(n)

    kevinNum = sum(dict)

    if minKevinNum > kevinNum:
        minKevinNum = kevinNum
        minNum = i

print(minNum + 1)