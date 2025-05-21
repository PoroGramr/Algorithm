from collections import deque
def bfs(maps,m,n):
    visit = [[0] * n for _ in range(m)]
    q = deque()
    
    q.append((0,0))
    visit[0][0] = 1
    
    while q:
        cy, cx = q.popleft()

        for py, px in ((-1,0), (1,0), (0,-1), (0,1)):
            ny = cy + py
            nx = cx + px
            
            if 0 <= ny < m and 0 <= nx < n and maps[ny][nx] == 1 and visit[ny][nx] == 0:
                q.append((ny,nx))
                visit[ny][nx] = visit[cy][cx] + 1
            
            
    if visit[m-1][n-1] != 0:
        return visit[m-1][n-1]
    else:
        return -1
        
def solution(maps):
    answer = 0
    
    n = len(maps[0])
    m = len(maps)

    answer = bfs(maps, m, n)
    return answer