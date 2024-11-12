from collections import deque

def bfs(maps,n,m):
    v = [[0] * m for _ in range(n)]
    q = deque()
    q.append((0,0))
    v[0][0] = 1
    
    while q:
        cy, cx = q.popleft()
        
        for py, px in ((0,1), (0,-1), (1,0), (-1,0)):
            ny, nx = cy + py, cx + px
            
            if 0 <= ny < n and 0 <= nx < m and maps[ny][nx] == 1:
                if v[ny][nx] == 0:
                    v[ny][nx] = v[cy][cx] + 1
                    q.append((ny,nx))
                else:
                    if v[ny][nx] > v[cy][cx] + 1:
                        v[ny][nx] = v[cy][cx] + 1
                        q.append((ny,nx))
    if v[n-1][m-1] != 0:
        return v[n-1][m-1]
    else:
        return -1

                    

def solution(maps):
    n = len(maps)
    m = len(maps[0])

    answer = bfs(maps, n, m)
    return answer