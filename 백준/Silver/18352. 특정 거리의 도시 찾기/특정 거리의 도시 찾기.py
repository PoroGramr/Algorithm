import sys
from collections import deque

input = sys.stdin.readline

N, M, K, X = map(int, input().split())
graph = [[] for _ in range(N + 1)]
distance = [-1] * (N + 1)  # 거리 초기화

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)

# BFS
q = deque([X])
distance[X] = 0

while q:
    current = q.popleft()
    for next_node in graph[current]:
        if distance[next_node] == -1:
            distance[next_node] = distance[current] + 1
            q.append(next_node)

# 정답 찾기
answer = [i for i, dist in enumerate(distance) if dist == K]

if answer:
    print('\n'.join(map(str, sorted(answer))))
else:
    print(-1)
