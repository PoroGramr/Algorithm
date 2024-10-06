from collections import deque

T = int(input())

INF = 10000
def bfs(y,x):
    q = deque()
    v = [[INF] * N for _ in range(N)]
    
    q.append((y,x))
    v[y][x] = data[y][x]

    while q:
        cy, cx  = q.popleft()

        for py, px in ((-1,0), (1,0), (0,1), (0,-1)):
            ny, nx = cy + py, cx + px
            if 0 <= ny < N and 0 <= nx < N and v[ny][nx] > v[cy][cx] + data[ny][nx]:
                q.append((ny,nx))
                v[ny][nx] = v[cy][cx] + data[ny][nx]
    
    return v[N-1][N-1]

    

for i in range(1,T+1):
    N = int(input())

    data = [list(map(int, input())) for _ in range(N)]
    answer = bfs(0,0)
    print(f"#{i} {answer}")