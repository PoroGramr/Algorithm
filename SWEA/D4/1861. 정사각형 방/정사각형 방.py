from collections import deque

def bfs(y, x):
    if memo[y][x] != 0:
        return memo[y][x]

    q = deque([(y, x)])
    visited = [(y, x)]
    count = 1

    while q:
        cy, cx = q.popleft()
        for dy, dx in ((0,1), (0,-1), (1,0), (-1,0)):
            ny, nx = cy + dy, cx + dx
            if 0 <= ny < N and 0 <= nx < N and data[ny][nx] == data[cy][cx] + 1:
                count += 1
                q.append((ny, nx))
                visited.append((ny, nx))

    for vy, vx in visited:
        memo[vy][vx] = count
    return count

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]
    memo = [[0] * N for _ in range(N)]

    max_count = 0
    max_start = N*N

    for y in range(N):
        for x in range(N):
            if memo[y][x] == 0:
                count = bfs(y, x)
                if count > max_count or (count == max_count and data[y][x] < max_start):
                    max_count = count
                    max_start = data[y][x]

    print(f"#{tc} {max_start} {max_count}")