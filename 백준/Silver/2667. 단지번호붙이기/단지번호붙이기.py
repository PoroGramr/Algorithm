"""
7
0110100
0110101
1110101
0000111
0100000
0111110
0111000
"""

from collections import deque


def dfs(i,j):
    q = deque()
    v[i][j] = 1
    count = 1
    q.append((i,j))
    while q:
        ci,cj = q.popleft()
        for pi,pj in ((0,1), (0,-1),(1,0), (-1,0)):
            ni, nj = ci + pi, cj + pj
            if 0 <= nj < N and 0 <= ni < N and v[ni][nj] == 0 and data[ni][nj] == 1:
                count += 1
                q.append((ni,nj))
                v[ni][nj] = 1
    return count
        
        
    

N = int(input())

data = [list(map(int, input())) for _ in range(N)]
v = [([0] * N)  for _ in range(N)]
answer = []


for i in range(N):
    for j in range(N):
        if data[i][j] == 1 and v[i][j] == 0:
            answer.append(dfs(i,j))
            
print(len(answer))
answer.sort()
for k in answer:
    print(k)
        
