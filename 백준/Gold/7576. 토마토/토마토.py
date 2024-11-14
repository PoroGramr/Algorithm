from collections import deque

def bfs():
    q = deque(tomatos)

    while q:
        cy, cx = q.popleft()

        for py, px in ((0,-1), (0,1), (-1,0), (1,0)):
            ny, nx = cy + py, cx + px

            if 0 <= ny < N and 0 <= nx < M and data[ny][nx] == 0:
                q.append((ny,nx))
                data[ny][nx] = data[cy][cx] + 1


M, N = map(int, input().split())

data = []

for _ in range(N):
    data.append(list(map(int, input().split())))
# 토마토의 좌표를 저장
tomatos = []

# 토마토가 익을수 없는 곳의 수 카운트
noGround = 0

for y in range(N):
    for x in range(M):
        if data[y][x] == 1:
            tomatos.append((y,x))
        elif data[y][x] == -1:
            noGround += 1



bfs()
tomatoCount = 0
maxDay = 0
for y in range(N):
    for x in range(M):
        if data[y][x] >= 1:
            tomatoCount += 1
            maxDay = max(maxDay, data[y][x])


if tomatoCount == N * M - noGround:
    print(maxDay - 1)
else:
    print(-1)


