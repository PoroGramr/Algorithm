from collections import deque

def bfs(y,x):
    q = deque()
    v[y][x] = data[y][x]
    q.append((y,x))

    while q:
        cy, cx = q.popleft()

        for py, px in ((-1,0),(1,0), (0,-1), (0,1)):
            ny, nx = cy + py, cx + px
            
            # 해당 좌표까지 도달하는 최소값을 방문 리스트에 저장함 
            if 0 <= ny < n and 0 <= nx < n and v[ny][nx] > v[cy][cx] + data[ny][nx]:
                v[ny][nx] = v[cy][cx] + data[ny][nx]
                q.append((ny,nx))
    
    # 최소값 리턴 
    return v[n-1][n-1]

T = int(input())

for t in range(1, T+1):
    n = int(input())

    data = []

    for _ in range(n):
        data.append(list(map(int,input())))
        
    # 방문 리스트의 모든 요소를 최대값으로 설정
    # 방문 리스트에 저장되는 요소들은 해당 좌표까지 도달하는 최소값이 저장
    v = [[float("INF")] * n for _ in range(n)]
    
    # 탐색 시작
    ans = bfs(0,0)

    print(f"#{t} {ans}")