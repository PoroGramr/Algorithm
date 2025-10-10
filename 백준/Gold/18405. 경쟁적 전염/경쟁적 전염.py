from collections import deque

N,K = map(int, input().split())

data = []

for _ in range(N):
    data.append(list(map(int, input().split())))

S, Y, X = map(int, input().split())

virus = []

for i in range(N):
    for j in range(N):
        if data[i][j] !=0:
            # (virus_id, time, y, x)
            virus.append((data[i][j],0,i,j))

virus.sort(key = lambda x : x[0])


q = deque()

for v in virus:
    q.append(v)

dir = ([-1,0], [1,0], [0,-1], [0,1])

while q:
    vid, t, y, x = q.popleft()
    if t == S:
        break
    for dy, dx in dir:
        ny = dy + y
        nx = dx + x
        if 0 <= ny< N and 0 <= nx < N and data[ny][nx] == 0:
            data[ny][nx] = vid
            q.append((vid,t+1,ny,nx))

print(data[Y-1][X-1])