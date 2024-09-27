from collections import deque

def bfs(c):
    q = deque()
    v = [0 for _ in range(N+1)]
    v[c] = 0
    q.append(g[c])
    
    while q:
        link = q.popleft()
        for ld in link:
            if ld == 1:
                continue
            if v[ld] == 0:
                v[ld] = 1
                q.append(g[ld])
    return sum(v)
            



N = int(input()) # 컴퓨터의 수
M = int(input()) # 연결된 컴퓨터 쌍의 수

g = [[] for _ in range(N+1)]

for _ in range(M):
    a,b = map(int, input().split())
    g[a].append(b)
    g[b].append(a)

for i in range(N + 1):
    g[i].sort()
# [] [2, 5] [1, 3, 5] [2] [7] [1, 2, 6] [5] [4]
answer = bfs(1)
print(answer)