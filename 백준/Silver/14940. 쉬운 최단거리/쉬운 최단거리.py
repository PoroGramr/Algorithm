from collections import deque

def bfs(y, x):
    q = deque()
    q.append((y, x))

    v[y][x] = 0

    while q:
        cy, cx = q.popleft()
        for py, px in ((0,1), (0,-1), (1,0), (-1,0)):
            ny, nx = cy + py, cx + px

            if 0 <= ny < N and 0 <= nx < M and v[ny][nx] == 0 and data[ny][nx] == 1:
                q.append((ny,nx))
                v[ny][nx] = v[cy][cx] + 1








N, M = map(int, input().split())

data = []

for _ in range(N):
    data.append(list(map(int, input().split())))

sy, sx = 0, 0

for y in range(N):
    for x in range(M):
        if data[y][x] == 2:
            sy, sx = y, x


v = [[0] * M for _ in range(N)]

bfs(sy,sx)
v[sy][sx] = 0
for y in range(N):
    for x in range(M):
        if data[y][x] == 1 and v[y][x] == 0:
            v[y][x] = -1



for row in v:
    print(*row)