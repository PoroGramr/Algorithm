from collections import deque
import sys

input = sys.stdin.readline

# N : 도시의 개수, M : 도로의 개수, K : 원하는 최단 거리 정보, X : 출발 도시의 번호
N, M, K, X = map(int, input().split())

data = [[] for _ in range(N + 1)]
v = [-1 for _ in range(N + 1)]

for _ in range(M):
    s, e = map(int, input().split())
    data[s].append(e)


q = deque()
q.append(X)
v[X] = 0
while q:
    cur = q.popleft()
    for next in data[cur]:
        if v[next] == -1:
            q.append(next)
            v[next] = v[cur] + 1

answer = []

for check in range(len(v)):
    if v[check] == K:
        answer.append(check)


if answer:
    for i in answer:
        print(i)
else:
    print("-1")


